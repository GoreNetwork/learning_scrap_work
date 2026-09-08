// cargo run --bin ssh_tests
//
// Requires `ssh2 = "0.9"` and `dotenvy = "0.15"` in Cargo.toml.
// macOS may need `brew install libssh2 openssl` if the ssh2 build fails.
//
// Secrets are loaded from ~/secrets/rust_ssh_test.env. Create that file with:
//     SSH_HOST=192.168.1.1:22
//     SSH_USER=admin
//     SSH_PASSWORD=hunter2
//     SSH_COMMAND=show version
// (SSH_-prefixed so we don't collide with shell-set vars like $USER)

use ssh2::{KeyboardInteractivePrompt, Prompt, Session};
use std::env;
use std::io::Read;
use std::net::TcpStream;
use std::path::PathBuf;

// A keyboard-interactive handler that answers every server prompt with the
// same password. Needed for devices (F5, many network appliances) that only
// advertise `keyboard-interactive` and reject plain `password` auth.
struct PasswordPrompt(String);

impl KeyboardInteractivePrompt for PasswordPrompt {
    fn prompt<'a>(
        &mut self,
        _username: &str,
        _instructions: &str,
        prompts: &[Prompt<'a>],
    ) -> Vec<String> {
        prompts.iter().map(|_| self.0.clone()).collect()
    }
}

fn main() {
    // Build path to ~/secrets/rust_ssh_test.env (~ isn't auto-expanded in Rust)
    let home = env::var("HOME").expect("HOME env var not set");
    let env_path = PathBuf::from(home).join("secrets/rust_ssh_test.env");

    // Load KEY=value pairs from the file into this process's environment
    dotenvy::from_path(&env_path)
        .unwrap_or_else(|e| panic!("failed to load {}: {e}", env_path.display()));

    let host = env::var("SSH_HOST").expect("SSH_HOST missing in env file");
    let user = env::var("SSH_USER").expect("SSH_USER missing in env file");
    let password = env::var("SSH_PASSWORD").expect("SSH_PASSWORD missing in env file");
    let command = env::var("SSH_COMMAND").expect("SSH_COMMAND missing in env file");
    println! ("Connecting to {host} as {user} and running '{command}'...\n");
    // 1. Open a TCP socket to the device
    let tcp = TcpStream::connect(&host).expect("connect failed");

    // 2. Wrap it in an SSH session and do the SSH handshake
    let mut sess = Session::new().unwrap();
    sess.set_tcp_stream(tcp);
    sess.handshake().expect("handshake failed");

    // 3. Authenticate — try password first, fall back to keyboard-interactive
    // (which F5 BIG-IP and similar appliances require).
    println!("server advertises auth methods: {}", sess.auth_methods(&user).unwrap_or(""));
    if sess.userauth_password(&user, &password).is_err() {
        let mut prompter = PasswordPrompt(password.clone());
        sess.userauth_keyboard_interactive(&user, &mut prompter)
            .expect("keyboard-interactive auth failed");
    }
    assert!(sess.authenticated());

    // 4. Open a channel and run a command
    let mut channel = sess.channel_session().unwrap();
    channel.exec(&command).unwrap();

    let mut output = String::new();
    channel.read_to_string(&mut output).unwrap();
    println!("{output}");

    // 5. Cleanly close
    channel.wait_close().unwrap();
    println!("exit status: {}", channel.exit_status().unwrap());
}

# Rust notes

## Creating a sandbox crate

From the `rust/` directory:

```
cargo new sandbox
```

That creates:

```
sandbox/
├── Cargo.toml      # crate manifest: name, version, edition, dependencies
└── src/
    └── main.rs     # default binary entry point (fn main)
```

`Cargo.toml` is what makes it a Cargo project. Without it, `rustc` sees loose
`.rs` files and rust-analyzer can't load a workspace.

Add `--lib` for a library crate instead of a binary:

```
cargo new sandbox --lib
```

## Running a specific binary: `cargo run --bin <name>`

Cargo auto-discovers two kinds of binary targets:

- `src/main.rs` — the default binary, named after the crate.
- `src/bin/*.rs` — each file is a separate binary named after the file.

So `src/bin/bool_tests.rs` becomes a binary called `bool_tests`. To run it:

```
cargo run --bin bool_tests
```

The `--bin bool_tests` is required whenever the crate has more than one binary
— otherwise Cargo doesn't know which one you meant. If you only have
`src/main.rs`, plain `cargo run` works.

A loose file at `src/bool_tests.rs` (not under `bin/`) is NOT a binary target —
Cargo ignores it and you can't run it directly.

## rust-analyzer inside a non-Rust workspace root

If VSCode is opened at a parent folder that isn't itself a Cargo project,
rust-analyzer errors with `failed to find any projects`. Point it at the
crate manifest via `.vscode/settings.json`:

```json
{ "rust-analyzer.linkedProjects": ["rust/sandbox/Cargo.toml"] }
```

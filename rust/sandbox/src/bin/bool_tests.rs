// cargo run --bin bool_tests


fn main() {
    let a = true;
    let b = false;
    let c = a && b;
    println!("{a} && {b} = {c}");
    let c = a || b;
    println!("{a} || {b} = {c}");
}

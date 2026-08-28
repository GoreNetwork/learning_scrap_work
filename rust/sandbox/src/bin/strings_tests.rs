// cargo run --bin strings_tests


fn main() {
    let a =  "bob";
    let b = "chad";
    let c = format!("{a} {b}");
    println!("{a} + {b} = {c}");
    println!("hello {}", a.to_uppercase()); // There is no f"hello {a.upper()}" equivlent

}

// cargo run --bin range_tests


fn main() {
    let stuff = 1..=5; // inclusive range up to and including 5, [1, ...,5]
    println!("{:?}",stuff);
    for i in stuff {
        print!("{i}");
    }
    print!("\n");
    let stuff = 1..5; // inclusive range up to but not including 5, [1, ...,4]
    println!("{:?}",stuff);
    for i in stuff {
        print!("{i}");
    }
    print!("\n");
    let letters = 'a'..='e'; // inclusive range up to and including e, [a, ...,e]
    println!("{:?}",letters);
    for l in letters {
        print!("{l}, ");
    }
    print!("\n");
}

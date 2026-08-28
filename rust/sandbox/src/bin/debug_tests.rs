// cargo run --bin debug_tests


fn main() {


    let mut numbers = vec![1, 2, 3, 4, 5]; // vec! lets you add items
    numbers.push(6);
    println!("{:?}", numbers);
    //{
    //     :   // format specifier
    //     ?   // debug print
    // }
    println!("{numbers:?}"); // regular print same as above
    println!("{numbers:#?}");  // pprint
       
}

// cargo run --bin array_tests


fn main() {
    let numbers = [1, 2, 3, 4, 5];  // Can't add or change by default, everything must be the same data type.
                                            // if you want different data types you can do something like

                                            // enum Item {    //I think this is a class that can be a sting or an int?
                                            //     Int(i32),
                                            //     Text(String),
                                            // }
    println!("{:?}", numbers);
    let mut numbers = vec![1, 2, 3, 4, 5]; // vec! lets you add items
    numbers.push(6);
    println!("{:?}", numbers);
    print!("first: {}, ", numbers[0]);
    println!("length: {}", numbers.len());
    //let test = vec! []  This doesn't work because it doesn't know the type that will be in it
    let test: Vec<i32> = vec![]; // This works because we are telling it the type that will be in it
    //print!("numbers[0]"); doesn't work

}

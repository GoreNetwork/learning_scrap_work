// cargo run --bin functions_tests


fn print_the_bitch(the_bitch: Vec<i32>) {
    println!("{:?}", the_bitch);
}

fn square(x: i32) -> i32 {
    return x * x; //explisitly returns the value
}

fn cube(x: i32) -> i32 {
    x * x * x //implicitly returns the value of the last expression in the function
                // be sure not to have the ; at the end of the last expression or it will return () instead of the value
}

fn main() {
    let mut numbers = vec![1, 2, 3, 4, 5];  // vec! = growable. [..] would be a fixed-size array — no push.
                                            // if you want different data types you can do something like

                                            // enum Item {    //I think this is a class that can be a sting or an int?
                                            //     Int(i32),
                                            //     Text(String),
    for i in 1..=5{
        numbers.push(i);
    }
    print_the_bitch(numbers);
    println!("{} squared = {}", 5, square(5));
    println!("{} cubed = {}", 5, cube(5));

}

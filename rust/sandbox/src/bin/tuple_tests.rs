// cargo run --bin tuple_tests
// Tuples: fixed-length, and each slot can be a DIFFERENT type.

fn main() {
    // Declare with mixed types. Type annotation is optional; here for clarity.
    let person: (i32, &str, bool) = (42, "bob", true);
    let test = (42, "bob", true);
    println!("{:?}", test);
    println!("guy's name: {}", test.1);
    let (age, name, likes_feet) = test;
    println! ("age: {}, name: {}, likes_feet: {}", age, name, likes_feet);

    // {:?} = Debug format. Works for tuples out of the box.
    println!("{:?}", person);

    // Access individual fields with .0, .1, .2 (positional, not [])
    println!("age = {}, name = {}, active = {}", person.0, person.1, person.2);

    // Destructure into named variables
    let (age, name, active) = person;
    println!("destructured: age={age}, name={name}, active={active}");

    // Tuples can nest and hold anything, including other tuples / vecs
    let mixed = (1, "two", 3.0, vec![4, 5, 6]);
    println!("{:?}", mixed);

    // {:#?} = pretty-printed Debug (one field per line, indented)
    println!("{:#?}", mixed);
}

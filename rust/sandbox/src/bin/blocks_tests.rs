// cargo run --bin blocks_tests
// unit is the default return type if there is no type given
fn main() {
    let multiplier = 2;

    // the block is an isolaoted scope, so the multiplier variable is not accessible here
    let result = {
        println!("Outer block: {multiplier} * 5 = {}", multiplier * 5);
        let multiplier = 3;
        let result = multiplier * 5;
        println!("Inner block: {multiplier} * 5 = {result}");
        3*3 // this value is returned as it's the last expression in the block.  Note the lack of ; on this line
    };
    println!("Outer block: {multiplier} * 5 = {}", multiplier * 5);
    println!("Result from inner block: {result:?}");

    // `match` is also an expression — every arm returns a value and the whole
    // match evaluates to that value, so you can bind it to a variable.
    let flag = true;
    let message = match flag {
        true  => "flag is set",
        false => "flag is unset",
    };
    println!("match result: {message}");

    // Arms can also be full blocks {} if you need multiple statements.
    // The compiler checks that every arm returns the SAME type, AND that
    // you've covered every possible value (exhaustiveness).
    let n = 3;
    let category = match n > 0 {
        true => {
            println!("(computing positive branch)");
            "positive"
        }
        false => "zero or negative",
    };
    println!("{n} is {category}");
}




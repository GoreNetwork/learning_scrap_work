// cargo run --bin match_tests
//
// `match` is Rust's pattern-matching statement.
// Think of it as a supercharged `if/elif/else` from Python.
//
// Shape of every arm:
//     PATTERN => EXPRESSION,
//
// Two big things to know:
//   1. `match` is an EXPRESSION — the whole thing evaluates to the winning
//      arm's value, so you can bind it to a variable with `let x = match ...`.
//   2. `match` is EXHAUSTIVE — the compiler forces you to cover every possible
//      input value, or use a wildcard `_`. If you add a new enum variant later
//      and forget to handle it, the compiler will refuse to build. This is
//      one of Rust's best features — impossible to accidentally miss a case.
//
// Arms are tried TOP-TO-BOTTOM; the first pattern that matches wins.

fn main() {
    // We'll classify an HTTP status code into a human-readable category.
    let status = 404;

    let label = match status {
        // --- 1. Literal pattern ---
        // Matches only when `status` is exactly 200.
        200 => "OK",

        // --- 2. OR pattern (using `|`) ---
        // Matches any one of these values. Read `|` as "or".
        301 | 302 | 307 | 308 => "redirect",

        // --- 3. Range pattern (`..=` is inclusive) ---
        // Matches 100 through 199 inclusive. Use `..` for exclusive upper
        // bound: 100..200 matches 100..=199 but not 200 itself.
        100..=199 => "informational",

        // --- 4. Binding with `@` ---
        // `n @ PATTERN` says "match PATTERN, and also bind the matched value
        // to `n` so we can use it inside the arm". Here we capture the exact
        // status number so we can print it before returning the label.
        // The arm body is a full block `{ ... }` because we have two lines;
        // the last expression (with no `;`) is the value returned by the arm.
        n @ 400..=499 => {
            println!("(saw client error {n})");
            "client error"
        }

        // --- 5. Match guard (`if` condition) ---
        // The pattern `code` matches ANY i32 and binds it to `code`.
        // The `if ...` guard adds a runtime condition that must also be true.
        // Guards run AFTER the pattern matches — so `code` is already bound.
        code if code >= 500 && code < 600 => "server error",

        // --- 6. Wildcard `_` ---
        // Matches anything not caught above. Required here because there
        // are billions of i32 values we haven't handled. Without this line
        // the code would not compile — that's exhaustiveness in action.
        _ => "unknown",  // if it weren't possable to get here unreachable!() would be used here instead of "unknown"
    };

    println!("HTTP {status}: {label}");

    // All arms must return the SAME type. Every arm above returns a &str,
    // so `label` is inferred as &str. Mix in an i32 and it stops compiling.
}

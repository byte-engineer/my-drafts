//   RRRRRRRRRRRRRRRRR   UUUUUUUU     UUUUUUUU   SSSSSSSSSSSSSSS  TTTTTTTTTTTTTTTTTTTTTTT
//   R::::::::::::::::R  U::::::U     U::::::U SS:::::::::::::::S T:::::::::::::::::::::T
//   R::::::RRRRRR:::::R U::::::U     U::::::US:::::SSSSSS::::::S T:::::::::::::::::::::T
//   RR:::::R     R:::::R U:::::U     U:::::U S:::::S     SSSSSSS T:::::TT:::::::TT:::::T
//     R::::R     R:::::R U:::::U     U:::::U S:::::S             TTTTTT  T:::::T  TTTTTT
//     R::::R     R:::::R U:::::U     U:::::U S:::::S                     T:::::T
//     R::::RRRRRR:::::R  U:::::U     U:::::U  S::::SSSS                  T:::::T
//     R:::::::::::::RR   U:::::U     U:::::U   SS::::::SSSSS             T:::::T
//     R::::RRRRRR:::::R  U:::::U     U:::::U     SSS::::::::SS           T:::::T
//     R::::R     R:::::R U:::::U     U:::::U        SSSSSS::::S          T:::::T
//     R::::R     R:::::R U:::::U     U:::::U             S:::::S         T:::::T
//     R::::R     R:::::R U::::::U   U::::::U             S:::::S         T:::::T
//   RR:::::R     R:::::R U:::::::UUU:::::::U SSSSSSS     S:::::S       TT:::::::TT
//   R::::::R     R:::::R  UU:::::::::::::UU  S::::::SSSSSS:::::S       T:::::::::T
//   R::::::R     R:::::R    UU:::::::::UU    S:::::::::::::::SS        T:::::::::T
//   RRRRRRRR     RRRRRRR      UUUUUUUUU       SSSSSSSSSSSSSSS          TTTTTTTTTTT

// Be ready to be a Rustacean.
mod process;

// this is rust programming language.
// Here is 'The Rust Programming language' book really great source https://doc.rust-lang.org/stable/book/title-page.html.
// RUST is a statically typed compiled language.
// Rust include the std library automatically behind the scenes.


// Running the code.
// - First we need to install rust compiler.
// - Create a file with the extension .rs
// - The code starts from the main function.
// - Run compiler and pass the file into it.  | rustc file.rs
// - If the code created via cargo we can use | cargo run 


// Cargo Commends.........................................
// Useful link for cargo book https://doc.rust-lang.org/cargo/index.html.

// cargo new <projectName>                  //. Create the project files.
// crago --version                          //. Get cargo version.
// cargo build                              //. Build the project.
// cargo run                                //. build and run the project.


// Rustup Commends.........................................
// rustup toolchain list                    // List the available rust releases.
// rustup show                              //. show us the versions of the toolchain (rust tools).


// Main function...........................................
// - the code starts from here.
// - We have to write main function in all applications.
fn main(){
    //! Contents.
    variables();
    integers();
    integers_methods(); 
    operators();
    floats();
    booleans();
    chars();
    tuples();
    arrays();
    vectors();
    string_slices();
    functions();                       // ON WORK
    cloures();                         // ON WORK
    user_input();
    print_formatting();
    println!("Done\n");
    // block of code.
}


// General Variables.......................................
// Variables in rust are immutable by default.
// In rust variables can be defined explicitly by (compiler) or implicitly (manually). ? 
// "let" keyword is used to declare a variable.
// "let" keyword is used to stor the variable on the stake.

#[allow(unused)]
fn variables() {

    // We dosen't allowed to declare a variable with `let` keyword in globle scope.
    // Emplicitly defined varible.
    // this variable is exist only on the scope of this function.
    let _x:i32 = 5;                              // Look how easy it is.
    let _x:char = 'A';                           // We over-ride x easly this prosecc known as "shadowing".


    // Constants:
    // We allowed to declare constents in globle scope using `const` keyword.
    // We reccomend to write consts in snake upper case.
    const X: i32 = 23;                           // Consts are avariables but must be known at compile time.
    const PI: f64 = 3.1415;                      // We must anotate the type on the consts and We cannot numtate them.
    const MIN: i32 = 60 * 1;                     // We can use exprisions when declaring constants.
    // Constatent are valid in entire time a program runs.


    // Mutability:
    // We just add a `mut` keyword on the variable type.
    let mut grade:char = 'B';                       // This muttable variable so we can change it.
    println!("after: {grade}");
    grade = 'C';                                    // Re-assign the variable.
    println!("before: {grade}");


    // Shadowing:
    // It means to declare a variable with same name (and type) of ther variable that was declared previously.
    // The second variable well shadow over the first until the scope ends or be shadowed, So the orignal variable is existwhen shadowed.
    // With shadowing we can change the type of the (variable) easly and preserve the same name.
    let org: i32 = 343;                             // ORignale variable.
    let org: char = 'A';                            // This variable will shadow over the previouse one.


    // Mutable referances.                           // This Steps applayed also when functions takes &mut var.
    let mut a = 12;                             // We have to create a mutable variable to get a mutable refence frome it.
    let b = &mut a;                        // Assign the mutable reference for other variable. 
    *b = 122;                                        // Dereferece the variable to change the value other wise we will change the reference.

}
    

// Primitive types.........................................
// We in rust has tow types of primitives.
// Rust has primitive scalar types: (integers, floats, Booleans, and characters).
// Rust has two primitive compound types: (tuples and arrays).




fn integers() {
    // We have several types of integeres.
    // The main signed types are (i8, i32, i64)
    // The main unsigned types are (u8, u32)
    // The defaulte type of integers is `i32`
    // What We can apply for one of this types we can applay it for others.
    // We have a isize and usize which are an integers in pointers size of the architecture if 32 or 64.
    // isize and usize are great for indexing.
    // If the integer over flow in release mode the code will NOT panic, Other wise It will panic. 
    // std library has some methods to handell overflowing in integers.



    // We can write integers in different ways:
    let _i: i32 = 256;                           // decimal
    let _i: i32 = 0xff;                          // hex
    let _i: i32 = 0o337;                         // oct
    let _i: i32 = 0b1111_1111;                   // bin
    let _i: u8 = b'A';                           // char (only u8)


    // declaring unsigned integer variable.
    let var: u8 = 255;
    
    // rotating the bynary 
    let _ = var.rotate_right(1);
    let _ = var.rotate_left(1);


    // finding min and max values.               // We can applay it for all types.
    let _ = i8::MAX;                             // [const] for the MAXIMUM value of the integer.  |  127
    let _ = i8::MIN;                             // [const] for the MINIMUM value of the integer.  | -128

    // Number of bits used the store the type.
    let _ = i8::BITS;                            // [const] for number of bits that used on memory.| 8


}


fn integers_methods() {
    let x: i32 = 32;

    // check the sign.
    let _ = x.is_positive();                     // true
    let _ = x.is_negative();                     // false

    // convert a &str to an integer.
    let _ = i32::from_str_radix("1a", 16).unwrap(); // deal with "1a" as hexadecimal.


    // operators:
    // mathmatical operators. 
    // type must match in all this operators.
    // return value is same as the given parameters.
    // division will round-down for integers type.

    let _ = 2 - 4;                               // Subtraction                   | -2
    let _ = 2 + 4;                               // Addition                      | 6
    let _ = 2 * 4;                               // Multiplication                | 8
    let _ = 2 / 3;                               // division Will round-down for  | 0
    let _ = 2 % 3;                               // reminder                      | 2

}



fn floats() {
    // We have several types of floats.
    // Rust has tow floating point types which are (f64, f32).
    // The defaute flaot type is f64.

    // float variable.
    let _var: f32 = 25.5;
    let _var: f64 = 65.5;                        // Double precesion as well. 

    // getting maximum and minimum values.
    let _ = f32::MAX;
    let _ = f32::MIN;
}


fn booleans() {
    // Booleans can hold true or false.
    // Bools often used in conditions and loops.

    let is_logged_in : bool = false;
    let is_signed_in : bool = true;


    // logical operations.
    let _ = is_logged_in && is_signed_in;        // logical AND.
    let _ = is_logged_in || is_signed_in;        // logical OR.
    let _ = !is_signed_in;                       // logical NOT.

}


fn chars() {
    // chars are a primitives for strings and it represent a `u32` integer.
    // chars in rust can store non-ASCII values because of it's size (four bytes).
    // Chars are identefied by the singel qout around them.


    let _var = 'd';
    let _chr: char = 'Z';                        // with explicit type annotation
    let _cat: char = '😻';                       // can even stor a non-ASCII chars.
}

// Compound Types:

#[allow(unused)]
fn tuples() {
    // Is a general way of grouping together a number of values with a variety of types into one compound type.
    // Tuples has afixed length (size) and it's types determined when declared.


    let _tup: (i32, f64, u8) = (500, 6.4, 1);    // This array contains several types.

    // We can use this method to extract a value from a tuple.
    let tup: (i32, f64, i32) = (500, 6.4, 1);
    let (x, y, z) = tup;

    tup.0;                                       // Accessing the first element.
    tup.1;                                       // Second one.
    tup.2;                                       // And the third.

    // Unit:
    // An empty tuples has a special name which is "unit"
    // Unit represent an empty value or an empty return type.

     let unit = ();

}


fn arrays() {
    // Arrays are a compound primitive type.
    // Elements of the arrays have a fixed type.
    // Unlike arrys in other languages Rust arrays has a fix size and not growable.
    // Arrays are alocated on the stack so thay are fast.
    // We use a [type; length] syntax on the type anotation.
    // rust std provided a growable vectors which are an arrays but thay are growable and alocated on the heap.


    // Declaring an array of 5 `i32` integers. 
    let a: [i8; 5] = [1, 2, 3, 4, 5];
    
    // declaring and intilize an array in the syntax.
    let _: [i8; 5] = [3; 5];                      // =>> [3, 3, 3, 3, 3]
    

    // Accecing values:
    a[0];                                         // Get first element.
    a[1];                                         // The second.
    a[2];                                         // Third one.
    // If we enter an invalid index the program will panic like so.
    // a[5];                                      // Panic

    // Slicing:
    let _: &[i8] = &a[1..3];                     // start => 1  end => 3
    let _: &[i8] = &a[..3];                      // start => 0  end => 3
    let _: &[i8] = &a[1..];                      // start => 1  end => a.len()
    let _: &[i8] = &a[..];                       // start => 0  end => a.len()

    
}


#[allow(unused)]
fn vectors() {
    // Vectors are like arrays but thay are growable and can be changed.
    // Vectors are heab alocated.
    // All elements on the vector must have the same type.
    // vec! macro is used to create a vector and thay have Vec<> type.

    let mut nums: Vec<i32>  = Vec::new();        // Take a vector instance.
    nums.push(10);                               // add `10` as a last element.
    nums.push(20);                               // This method is equavelant for .pushback() in C++.
    nums.push(30);



    // vec![] macro method.
    let chrs: Vec<char> = vec!['a', 's', 'd', 'w'];   // This way is easier for initilization.
    let chrs: Vec<char> = vec!['a'; 4];               // chrs = ['a','a','a','a']


    // accesing elements.
    let _ = &nums[1];                            // Take the second element. 
    let _ = &nums[0..2];                         // Take a slice from the vector.

    let _ = nums.get(1);                  // Using .get() method.
    let _ = nums.pop();                          // Removes the last element and return it.
    let _ = nums.remove(1);               //  Removes and returns the element at the specified index (less eficiente).
 

    // get first and last element.
    let _ = nums.first().unwrap();
    let _ = nums.last().unwrap();


    nums.extend(vec![30,40,50]);            // nums extended to --> [10,30,40,50,];
    nums.sort();
    nums.sort_by(|a, b| a.cmp(b));  // 


    // Some Vector INFO
    let _ = nums.len();                          // Get the vector length.
    let _ = nums.capacity();                     // Returns the capacity (how much memory is allocated).


    let _ = nums.clear();


    // turn the vector to iterator.              // Borrow Each element.
    let _ = nums.iter();                         // Now nums is an iterator. 
    let _ = nums.iter_mut();                     // Borrow  all elements mutably. 
    let _ = nums.into_iter();                    // Move the ownership from the source. 
    
    
}



fn string_slices() {
    // String Slices (&str):
    // - String slices OR (&str) is borow type Therefore, We just can read the date from it.
    // - &str type variable has a fix-size because is stores on the stack.
    // - &str has two components actual data and the length of the string. 
    // - Thay are encode the data using `UTF-8`, So thay cover wide range of chars.
    // - &str variable stores data for read-only operations by default.
    // - String slices can be stored on the stake, So in almost cases string slices are faster than String type.
    // - &str is the default value for strings in general, So if the type does not specified the variable will be &str.
    // - The normal indixing syntax is very avoided on &str. 

    let _my_str = "Hello World!";          // The Compiler will make deal with this as a &str.
    let _my_str: &str = "Rust is huge!";         // Of course we can spesifp the type explicitly.


    // Normal Indexing Complexetis:
    let s = "Hello, world!";
    let _hello = &s[0..5];                 // Slices the first 5 bytes: "Hello"
    let _world = &s[7..12];                // Slices "world"

    // The normal indixing syntax is very avoided on &str.
    let _s = "नमस्ते";                       // "न" takes 3 bytes.
    // let _invalid = &s[0..2];                  // Panics at runtime because 2 is not a valid boundary!


    // indexing and slicing:
    // This is the safe way for indexing.              // using unwarp method is suggested.
    let _ = "once beyond the time ...".chars().nth(3); // Return an option< > more later.
    let _ = "once beyond the time ...".get(5..11);     // Get the char same as an indexing but it returns option.


    // Getting the length.
    let _ = "Go away".len();                           // This method return the length in bytes not the characters .
    let _ = "😊".len();                                // This code will return 4 because "😊" stored in 4 bytes.

    // iterating over the &str.                        // later : About iterators. ??
    let _ = "dev UX is ...".chars().next();            // Return an iterator of the chars.
    let _ = "dev UX is ...".bytes().next();            // Same as chars but returning the bytes (b"") or (int).

    let _ = "\n   my name   ".trim();                  // Removes the white-spaces and '\n' from the.

    let _ = "tell me a story ...".split(' ');          // Split the string based on the parameter given.

    let _ = "We're good".replace("We", "thay");        // Replaces the string slices.

    let _ = "Hi, ...".starts_with("Hi");               // Will return boolean value.

    let _ = "abc".repeat(4);                           // 
}



#[allow(unused)]
fn functions() {
    // This ^ is an example for a function.
    // Functions in rust are taged with `fn` keyword.
    // Rust Reccomend to write functions names (and any other identifirs ) in lower-snake case.
    // Rust Functions can contain other inner functions.
    // inner functions are accesable in the outer function scope.



    fn do_this() { /* block of code */ }         // Functiond definition.  
    do_this();                                   // calling function.


    fn outer() {                                 // Inner function definition.
        fn inner(){}                             // Inner function definition.
        inner();                                 // calling inner functions.        
    }
    // inner();                                  // Error: Function not in scope.


    // Function with parameters
    fn add(a: i32, b: i32) -> i32 {              // We have to specify the parameters type and the retusn type explistly.  
        a + b                                    // No semicolon for returning value
    }                                            // We can also use normal return keyword.


    // Function mutable refrences.
    fn update_value(val: &mut i32) {             // The Function will mutate `val` variable and than will return it to the caller.
        *val += 1;                               // Be careful, this function does not oun `val` variable it just boroww it.
    }


    // Function pointers.
    fn multiply(a: i32, b: i32) -> i32 {a * b}             // Normal function.
    let func: fn(i32, i32) -> i32 = multiply;              // Get the pointer by write the function without it's brakets. 
    println!("{}", func(2, 3));                            // Output: 6   | This like taking a variable refrence. 


}



fn cloures() {
    // Closures are often used as an arguments for a higher order functions.
    // Also used with (map, filter, fold)  
    // Closures in other functions are called lambda functions.
    // It can capture variables from its surrounding environment.
    

    // Syntax
    //                                  ( |  params   | |return| |  body | )
    let plus1 = |x: &mut i32| -> i32   {*x + 1};
    println!("{}", plus1(&mut 34));                        // Call the closure like a normal function.


    // Closures can access the variables from thier scope.
    let x: i32 = 10;
    let add_to_x = |n: i32| x + n;    // Accessing `x`.
    println!("{}", add_to_x(5));                           // Output: 15


    // move keyword
    let x = String::from("SomeThing");             // String slice variable.
    let closure = move || {
        // Closure takes ownership of `x`
        println!("{}", x); };
    // x;                                                  // Error: x is not accesable from this scope.  
    closure();                                             // closure can access `x` and print it. 



    // (map, filter, fold)


}




fn operators() {

    // mathmatical operators:
    // type must match in all this operators.
    // return value is same as the given parameters.
    // division will round-down for integers type.

    let _ = 2 + 4;                               // Addition         | 6
    let _ = 2 - 4;                               // Subtraction      | -2
    let _ = 2 * 4;                               // Multiplication   | 8
    let _ = 2 / 3;                               // division         | 0
    let _ = 2 % 3;                               // reminder         | 2


    // bit-wise operators:
    // bit-wise oprations are just work with integers.
    // bit-wise oprations are use in some algorthms and low-level progaramming.

    let _ = 2 & 1;                               // bit-wise AND      | 0
    let _ = 2 | 1;                               // bit-wise OR       | 3
    let _ = 2 ^ 2;                               // bit-wise XOR      | 0
    let _ = 4 >> 2;                              // shift-right       | 1
    let _ = 1 << 2;                              // shift-left        | 4
    let _ = !255u8;                              // NOT               | 0


    // Equality opererators:
    let i = 1;
    let j = 1;

    let _ = i == j;                              // [ == ] equality operator.
    let _ = i != j;                              // [ != ] unequality operator.

    // logical operators:
    // this operators are work for the boolean values.

    let _ = false && true;                        // logical AND      | false
    let _ = false || true;                        // logical OR       | true
    let _ = !true;                                // NOT              | false


    // Assignment operators.
    // [  =  ] Singel normal assignment.
    // [ +=  ] Addition and assignment.
    // [ -=  ] Subtraction and assignment.
    // [ *=  ] Multiblication and assignment.
    // [ /=  ] Division and assignment.
    // [ %=  ] Reminder and assignment.
    // [ &=  ] Bitwise AND and assignment.
    // [ |=  ] Bitwise OR and assignment.
    // [ ^=  ] Bitwise XOR and assignment.
    // [ >>= ] Shift-right and assignment.
    // [ <<= ] Shift-left and assignment.


    
}



// User Input..............................................


fn user_input() {
    // input()

    let mut buf:String = String::new();

    let _res:usize = std::io::stdin()
        .read_line(&mut buf)
        .unwrap();

}


// Print Macro Formatting..................................

fn print_formatting() {
    // printing results in the terminal is veryh helpful for debuging.
    // Rust uses macros for printting results thay are more fluxible than normal functions.
    // In rust, we have two macros for that { print!(), println!() }
    // All what applaies for println macro applaies for print and eprint macros. 
    // Rust println macro uses formatting smiler to python.
    // We can use format!() in same way but it retunes string intead.

    // Positional Arguments:
    println!("Hello, {}!", "World!");                      // Outputs: "Hello, World!"

    // Positional Index:
    println!("{1} is learning {0}.", "Rust", "SomeOne");   // Outputs: "SomeOne is learning Rust".

    // Named Arguments:
    println!("{language} is amazing.", language="Rust");   // Outputs: Rust is amazing.

    // Width and Alignment:
    // | < | => left-align
    // | > | => right-align
    // | ^ | => center-align
    println!("{:<8}!", "Rust");                            // Outputs: "Rust    !"
    println!("{:>8}!", "Rust");                            // Outputs: "    Rust!"
    println!("{:^8}!", "Rust");                            // Outputs: "  Rust  !"

    // Padding:
    println!("{:*>8}", "Rust");                            // Outputs: "****Rust"
    println!("{:_<8}", "Rust");                            // Outputs: "Rust____"

    // Precision:
    println!("{:.2}", 3.14159);                            // Outputs: "3.14"
    println!("{:.3}", "Rustacean");                        // Outputs: "Rus"

    // Number Formatting:
    // | b  |> binary, add `#` for prefex.
    // | x  |> hexadecimal (lower case), add `#` for prefex.
    // | X  |> hexadecimal (upper case), add `#` for prefex.
    // | o  |> octal
    // | ?  |> debug formatting (for any type).
    // | #? |> debug with indentation mode.

    println!("{:b}", 15);                                  // Outputs: "1111" (binary)
    println!("{:o}", 15);                                  // Outputs: "17" (octal)
    println!("{:x}", 255);                                 // Outputs: "ff" (hexadecimal)
    println!("{:?}", vec![1, 2, 3]);                       // Outputs: "[1, 2, 3]" (debug)

    // {{ and }} for literal { and }.
    println!("Hello {{Rust}}!");                           // Outputs: Hello {Rust}!
}


// INFO----------------------------------------------------
// C++ is a very powerful staticly typed compiled language.
// You can do anything with it.

// Advanced Info-------------------------------------------
// Any thing starts with '#' is a preprocessed action.
// preprocessed actions get evaluated before compiling.
// We can not define a function inside a nother existing function.

/* Running the script--------------------------------------
 * - Download the compiler (g++ / clang++).
 * - There are many compilers but we will use (g++) or (clang).
 * - Create a file with `.cpp`, `.cc`, `.c++` or `.cxx`.
 * - Write in terminal `g++ file_name.cpp`.
 */

// Compiler -----------------------------------------------
// We have 3 main C/C++ compilers { gcc, MSVC, clang }
// MSVC  --> cl.exe                | also in Visual Studio
// gcc   --> g++.exe               | From GNU package
// clang --> clang++.exe           | Modren Uses LLVM technology
// For linking `ld` and `lld`

// simple comend for compiling a file.
//|>> clang++ -o file.exe file.cpp

// Compiler arguments:
// Almost all of this arguments are works with all the compiler.
//| -o <file>       >> For specify the output file without it output will be named a.exe
//| -v              >> Show all the setting of the compiler.
//| -w              >> Remove all wornings.
//|
//| -c              >> To compile the files without linking. | -save-temps flag give it also.
//| -E              >> To generate preprosecor file          | -save-temps flag give it also.
//| -S              >> To generate assimbly file             | -save-temps flag give it also.
//|
//| -std=<standard> >> Specify the C/C++ standard lib | -std=c++17  -std=c11
//|
//| -l<library>     >> Link with specific library.
//| -L<path>        >> Set a library search path.
//| -rpath=<path>   >> Set runtime (dynamic) library search paths.
//| -static         >> Generate a static library (.lib)  | unix (.a)
//| -shared         >> Generate a dynamic library (.dll) | unix (.so)
//|
//| -D<macro>       >> Define a macro (e.g., -DDEBUG).
//| -U<macro>       >> Undefine a macro.
//| -I<path>        >> Add an include path for headers.
//|
//| -O0             >> No optimization (default).
//| -O1             >> Optimize minimally.
//| -O2             >> Moderate optimization.
//| -O3             >> High optimization.
//| -Ofast          >> Maximum speed optimization (may break strict standards).
//| -flto           >> Enable Link Time Optimization (LTO).
//|
//| -m32 -m64       >> Compile for 32-bit or 64-bit architecture.


// Comments------------------------------------------------
// Comments are removed BEFORE preprocessing and replaced with a single space.
// this is in-line comment.
/* this is multiple line comment*/

// Main header file---------------------------------------
// The main header in cpp that includes standard file is <iostream>.
// To import the header file we use #include pre-proseccor keyword.
// We will use learn about it's commends later.
// Our program will start execute front the main function.

// Main library in cpp (std).
#include <iostream>                                             // The compiler bring whatever in iostream and paste it here.

// Without `_`.                                                 // I wrote the underScore for technical reasons.
int _main(void)
{                                                               // From here our code will start executing ( our entry )
    // Put here your block of code.
    return 0;                                                   // Returning 0 means that the program finished executed.
}
// We don't have to return from a main function ( special case for main function ).

// Variables --------------------------------------------------------
// Variables are so important in any programming language.
// Variables in C++ have an easy syntax (type name = value;)
// The C++ is a staticly typed language.
// We type first the type of our variable then the name of the variable.
// We have many different types of variables. {int, double}
// We cannot use same variable name for different variables.


void Variables(void)
{
    // Variable Declaration.
    int var;                                                    // Declares an integer variable named 'age'
    int cont = 25;                                              // Initializes 'age' with value 25

    char a, b, c;                                               // declaring 3 variables at once.
    double d, e = 3.2, f;                                        // Declare and assign a value to e.

    a = b = c = 10;                                             // Assign 10 to all variables.

    // Main Variables Types.                                                                           |_Size_____|_Range_________________
    char      ltr = 'A';                                        // For store a single letter or number.| 1 byte   | ±128
    short     mrk = 12;                                         // For store a short integer.          | 2 bytes  | ±32768
    int       age = 1;                                          // For store integers.                 | 4 bytes  | ±2147483647
    long long tim = 1001;                                       // For store large integers            | 8 bytes  | ±9223372036854775808
    float     pi = 3.14f;                                       // For store single precision floats.  | 4 bytes  | 7  dec
    double    num = 1.5;                                        // For store double precision floats.  | 8 bytes  | 15 dec
    bool      stt = true;                                       // For store a boolean value.          | 1 byte   | 1, 0

    // Increment/decrement the variables.
    age++;                                                      // Increment age.
    age--;                                                      // Decrement age.

    int year1 = age++;                                          // year will not be assigned to an incremented value
    int year2 = ++age;                                          // year will be assigned to an incremented value.

    // We can use sizeof to determine the size of the variable.
    int sz_bool = sizeof(bool); // --> 1 byte
    int sz_int = sizeof(int);  // --> 4 bytes

    // prefixes

    // signed & unsigned
    signed int   temp;                                           // Ints are signed by default.
    unsigned int length;                                         // This variable can't hold negative numbers ( With this method we can maximize the range of the variable in the positive side. Range-> 0-->4294967294 ).

    // const                                                     // Just for user safety. Read only value.
    const int constant = 23;                                     // Will raise error if the value changed.



    // Litrals 
    1.0;                // double 
    4e2;                // double
    3.141'592;          // double, single quotes ignored (C++14)
    1.0f;               // float
}


// Standard input and output-----------------------------------------
// We can use `cout` to 'print' characers into the terminal.
// We use cin to read user input from the terminal.
// This two classes are exist in iosream header.
// `cout` is an instance from ostream class.
// `cin` is an instance from istream class.

#include <string> // for getline() 

void standardIO()
{
    int var1 = 0;
    int var2 = 0;
    std::string name; 

    // cout
    std::cout << "this is great day!\n";                        // Printing string to the terminal. 
    std::cout << var1 << std::endl;                             // We can use std::endl  instead of '\n'


    // cin
    std::cin >> var1;                                           // Puts the input into `var`.
    std::cin.clear();                                           // Is recomended the clear the standard input c stream. (ostream) 
    std::cin.ignore(100, '\n');                                 // We ignor any additional unwanted characters (100 char) to '\n'

    // We can use cin with multible variables
    std::cin >> var1 >> var2;                                   // User can enter values seperated with any white spaces {' ', '\n', '\t'}

    if (std::cin >> var1) {}                                    // If there are any errors it will return false.

    // We can use getLine() to allow the user to input a space ' '
    std::getline(std::cin, name);                               // this function from string module.
    //                                                          // We can use more than one variable for each line. getline(cin,...)


}



// Arrays -----------------------------------------------------------
// Arrays are a zero base indexed.
// Arrays has a fixed size in C++.

void CStyledArrays()
{
    int var;

    int nums[6] = { 1, 2, 3, 4, 5, 6 };                           // Array of integers.
    int NUMs[6]{ 1, 2, 3, 4, 5, 6 };                              // other syntax.             | Valid only in C++
    int numb[]{ 1, 2, 3, 4, 5, 6 };                               // Compiler determines size. | Valid only in C++

    // Two dimensional array.
    int location[3][3] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };

    // indexing
    var = nums[0]; // First element.
    var = nums[1]; // Second element.

    var = location[1][2]; // result => 6
}

// Array------------------------------------------------------------- 
// This array solves the problems of c-stye arrays (above).
// Arrays are alocated on the stake so thay are fast.
// The length is not stored on the array but it just substituted at compile time.
// Arrays are NOT growable.

#include <array>

void Array()
{
    int res;

    // syntax --> array <type, size> name = { v,a,l,u,e,s };
    std::array<int, 4> numbers = { 1, 2, 3, 4 };

    // Array methods
    res = numbers.size();                                  // get the size of the array.
    res = numbers.front();                                 // get first element.
    res = numbers.back();                                  // get last element.
    res = numbers.at(2);                                   // get an element of a specific index.
    res = numbers.empty();                                 // Check if the array is empty and return boolean value.
    numbers.fill(12);                                      // fill whole array with ten.
}

// Casting Variables-------------------------------------------------
// Casting variables means to convert a variable from type to another.
// Compiler does casting automatically.
// We can perform manual casting.
// We have C-style Casting and Function style casting.

void Casting()
{
    // automatic casting.
    int num0 = 10;
    double dnum0 = num0;                                   // Implicit conversion from int to double

    // C-style casting.
    int num1 = 11;
    double dnum1 = (double)num1;

    // Function style.
    int num2 = 12;
    double dnum2 = double(num2);

    // Static casting
    // In this method we cast the variable at compilation time.
    int num = 10;
    double dnum = static_cast<double>(num);                // Safer cast in C++.

    // Dynamic casting
    // This type primarily used in classes and pointers.
    printf("A: %d\nB: %d\n", num1, num2);                  // printf function from C std (stdio.h)
}

// Numbers representations------------------------------------------

void NumbersRepresentations()
{

    int binary = 0b1001;                                        // Binary.
    int hex = 0xabcd;                                           // Hexi-decimal.
    int decemal = 12;                                           // Normal number.
}


// Strings ----------------------------------------------------------
// Strings in C++ are handled in two ways which are (C-style, by cpp-std library)
// We can write strings in C-style which is direct characters list (char[]).
// Also We can use string class from standard library as a variable type.


void CStyleStrings()
{

    //  C-style method.
    //  - This is creates an array of characters to create a string.
    //  - The array must be null-terminated '\0' (done automaticaly).
    //  - Operations like concatenation and length checking need manual functions (e.g., strcat, strlen from the <cstring> library).
    //  - This method create a fixed size string.
    //  - We can't concatenate arrays directly.
    char user[] = "somebody";                                   // We have to use double quotes "" .

    // We can specify the number of the elements in the beginning.
    char pass[5] = "1234";                                      // We have 5 elements on the array {'1', '2', '3', '4', '\0'}

}


#include <string>

void String()
{

    // String class method.
    // This method solves previous method problems.
    // This method considered as a modern C++ style.
    // Strings in this method are dynamic. (not fixed size)
    // string is a class and has a very useful methods.
    // We can use '+' for concatenation.
    // This is very useful methods { length(), substr(), find(), append() }

    // std::string      || Sequance of `char`s
    //  std::wstring    || Sequance of `wchar_t`s


    std::string res;
    std::string Wisdom1 = "Don't fight someone who has nothing to lose";
    std::string shop = "something ";
    std::string owner = "something else";

    // concatenation.
    std::string sum = shop + owner;                             // Result => "something something else"
    shop += owner;                                              // Result => "something something else"
    shop[0] = 'S';                                              // Result => "Something something else"

    // accessing elements 
    char fst = shop[0];
    char snd = shop.at(1);

    // Get The size.
    int size;
    size = shop.size();                                         // Result => 10
    size = shop.length();                                       // Same as size.


    // Substrings using `.substr()`
    res = Wisdom1.substr(5, 6);                                 // Result: "fight" (start at index 5, length 6)
    res = Wisdom1.substr(20);                                   // From index 20 to the end ("who has nothing to lose")

    // toupper & tolower                                        // Changing string case (No built-in function in standard C++)
    for (char& ch : shop) ch = toupper(ch);                     // Convert to upper case

    std::string Value = std::to_string(0.2);                    // parsing double to string.
    double val = std::stod(Value);                              // parsing string to double.

}


// Boolean Operators-------------------------------------------------
// this operators are return `true` or `false`.

void booleanOperators()
{
    bool state0 = 2 < 1;                                        // Less operator.
    bool state1 = 2 <= 2;                                       // Less or equal operator.
    bool state2 = 1 == 1;                                       // Equal operator.
    bool state3 = 2 != 1;                                       // NOT equal operator.

    bool state4 = !true;                                        // logical NOT.
    bool state5 = true && false;                                // logical AND.
    bool state6 = true || false;                                // logical OR.

}


void bitWiseOperators()
{
    int bitWise0 = ~1;                                          // NOT bit-wise operator.
    int bitWise1 = 1 & 0;                                       // AND bit-wise operator.
    int bitWise2 = 1 | 0;                                       // OR  bit-wise operator.
    int bitWise3 = 1 ^ 0;                                       // XOR bit-wise operator.

    int bitWise4 = 1 << 2;                                      // left-shift bit-wise operator.
    int bitWise5 = 1 >> 2;                                      // right-shift bit-wise operator.
}

// Functions---------------------------------------------------------
// Functions prevent us from rebeating.
// We have to specify the return type first.
int Multiply(int a, int b)
{                                    // Simple function.
    return a * b;
}

// Calling the function.
int result = Multiply(3, 55);                                   // We store the result in a variable.

// We can Write the header of the function just to prevent compilation errors.
int Multiply(int a, int b);                                     // Over load.


// If statment-------------------------------------------------------
// No thing strange with if statement in cpp.


void ifStatement()
{

    bool condition = true;                                      // true is an integer (usually 1) false is just a zer0.
    // Normal If statement.
    if (condition) {                                            // We can get rid 0f the curly barkcets (if our code in one line) and Will work just fine.
        // ... do something
    }

    // Branching if
    if (condition) {
        // D0 some thing.
    }
    else if (condition) {                                     // Actually we don't have any 'if else' saperate keyword! it's just a compination between 'if' keyword and 'else' keyword. 
        // Do some thing else. 
    }
    else {
        // if All conditions are false do this block of code.
    }

}

// Ternary If Statement----------------------------------------------
// syntax --> (condition)? true : false;


void ternaryIfStatement()
{
    bool condition = true;

    char l = condition ? 'T' : 'F';                                // T if True  and  F if False.
}

// Switch & Case------------------------------------------------------
// We use switch and case to avoid using if and else statements.
// Thay often used with enums.

void Switch()
{
    int option = 1; 

    switch (option) 
    {
        case 1:
            std::cout << "Color is Red\n";
            break;
        case 2:
            std::cout << "Color is Green\n";
            break;
        case 3:
            std::cout << "Color is Blue\n";
            break;
        default:
            std::cout << "Unknown color\n"; 
    }
}




// Loops-------------------------------------------------------------
// We have 3 loops in C++ which are {for , while, do-while}.
// Loops in C++ are extremally flexible.

// Control flow:
// - break;    --> To exit from the loop.
// - continue; --> To go to next iteration (skipping current iteration).
// - return; --> used in functions the exit from the function and return it's value.

void loops()
{
    bool condition = false;

    // for loop 
    for (int i = 0; i < 5; i++)                          // For rebeating 5 times.
    {
        // Do Some thing.
    }

    // While loop
    while (condition)
    {
        // Do some thing.
    }

    // Do-while loop
    do
    {
        // Do some thing
    } while (condition);
}


// Pointers----------------------------------------------------------
// A pointer is an 'integer' variable stores a block ( addresses ) of memory.
// Pointers types are meanless.
// Pointers types are exist just to display data to the user.
// We can create a pointer with no type ( void ptr* ).
// To return the value of the pointer block we have to specify a type.
// We have double pointers and trible pointers.

void RawPointers()
{
    // A variable is a data stored in a spesfic address on a memory.
    // Addresses stored on a variable called pointer.
    int var = 10;                                               // Regular integer variable.

    // '*' operator means that the variable is a pointer. ( store an address )
    int* ptr;                                                   // Declaring a pointer to an integer.

    // '&' operator used to get the address of tha variable.
    ptr = &var;                                                 // Pointer stores the address of 'var'

    // Dereferencing the pointer to get the value of 'var'
    int value = *ptr;                                           // value == var

    // Changing the value of 'var' via the pointer.
    *ptr = 20;                                                  // Some times we use pointers to change the variables.

    // Moves to the next integer's ( or any other type ) memory location (size of int is usually 4 bytes)
    ptr++;

    int* ptr1 = &var;                                           // Pointer to var
    int** ptr2 = &ptr;                                          // Pointer to pointer

    // Constant pointers.

    // a. Pointer for constant data.
    const int* ptr3 = &var;                                     // Now we can not change 'var' via pointer.
    //  *ptr3 = 32;                                             // Error because Data changed.

    // b. Constant pointer.
    int const* ptr4 = &var;                                     // Now the pointer ( address ) is constant.
    // ptr4 = &otherVar                                         // error because address changed.

    // c. Contant pointer for constant data.
    const int* const ptr5 = &var;
}
// Refrences---------------------------------------------------------
// Refernce is an alternative name for an already existing variable.
// type& indecate to the reference.

void References()
{
    int x = 10;                                                 // Regular integer variable.
    int& ref = x;                                               // ref is a reference to x
    ref = 20;                                                   // This changes x to 20

    // References & Functions.
    // We use references to a void coping a large a mount of data ot the scope f the function.
}


// Error Exeptions---------------------------------------------------
// In C++ We use try and catch keyword.

void ErrorHandling()
{

    try 
    {
        exit(1);
    }
    catch(std::runtime_error& e)
    {
        std::cout << "Some Error!" dsdl << std::endl;
    }
}




// Files Handelling--------------------------------------------------
// include the header.
#include <fstream>

void FileHandling()
{
    // Main Header files for file-handling:
    // * fstream   ==> combination of both ofstream and ifstream.

    // file handling operations:
    // * open()  – to create a file.
    // * read()  – to read the data from the file.
    // * write() – to write new data to file.
    // * close() – to close the file.

    // create and open a file.
    std::fstream file("data.txt", std::ios::out);
    file << "Hello, Bilal!" << std::endl;
    file.close();                                               // Close the file
}

// Anonomus Scope----------------------------------------------------
// Just works inside the functions.
// Used to sparate variables and functions scope. 
// this method used in librarys. 

void AnonomusScope()
{
    int var;
    // Scope 'A'
    {
        // this variable is not visible outside this barakits.
        int x;
        int y;
    }                                  // In this braket all scope variables will be removed. (Exept if thay allocated on the heap)

    // Scope 'B'
    {
        // this a difference scope.
        int x;
        var++;                      // var visible here.
        // y = 2;                   // Error: y is NOT visible in this scope.
    }
}


// Function overloading----------------------------------------------
// Functions with different list of parameters called function over loading. 
// Overloading allows to change the behavier of the function depending on the function.
// This style is exist in many programming languages.
// All overloaded functions must have same return type.

int f(void) { return 0; }                                            // Function with no parameters
int f(int x) { return x; }                                           // Overloaded function with one int parameter
int f(int x, int y) { return x+y; }                                  // Overloaded function with one two parameter.


void OverLoading()
{
    f();                 // We calling First "f" function. 
    f(2);                // We calling Second "f" function.
    f(2, 3);             // We calling Third "f" function.
}


// Constant Exeprisions----------------------------------------------
// We have two types of costant exepresions { variables, functions }
// Constant functions (and variables) are subestituted at compile time.
// We `constexpr` is used to turn a function or variable into constant exprsion.
// constexpr variables are better than (#define)s because we can debug them.

constexpr float squarArea(float l) { return l*l; }                  // this will turned into litral float value at compile time.

void ConstantExpresions()
{
    constexpr int number = 3*3;                                     // This is better than const variables bacause it garateed to be substituted at compile time. 
}

// User-defined Litrals----------------------------------------------
// Used in units conversions, class instantiations and more.
// We have some types are valid for this custom litrals.
//________________________
//| unsigned long long   |      >> Not all types are supported for User-defined litrals. 
//| long double          |
//| const char*, size_t  |      >> The second parameter is for the size of the chars.
// We can return any valid C++ type. 

// This litral converts meters to centimetrs.
double operator"" _cm(long double cm) { return cm / 100.0; }         // We should mark this function as constexpr.

void UserDefinedLitrals()
{
    double inMeters = 1.0_cm;   // there are many uses for this advantage.
}


// Enums------------------------------------------------------------
// Enumerations are an integers wraped in same names to support the code readablety.
// `enum` keyword is used to define enum collection.

enum colors
{
    RED,                           // this will equal 0.
    BLUE = 12,                     // We can give them a value explictly.
    GREEN                          // This will continue the enumiration | it equals 13. 
};                                 // Do not forget simecolon. 

void Enums()
{
    int color = RED;

    if (color == RED)             // easy for the reader to under stand.
        ;// Do some thing
}

// Structs-----------------------------------------------------------
// Structs (structures) are a set of variables groped to gether.
// struct's varibles (members) are defaulte to be public unlike classes.
// Structs has all OOP features but they used to grop data and small implementations. 
// structs support methods, constructors, destructors, ...
// Structs uses curly brackets ended with semicolon.

struct Group {
    int count;                                                       // public by default
    std::string names[3];                                            // public by default
};

void structs()
{
    // assign values for the struct
    Group friends {3, {"poul", "Bell", "Joe"}};                      // We can deal with stricts as a types.

    // Other method.
    friends.count = 5;                                               // Setting variables individually 

    // Accecing structs
    friends.count;                                                   // use dots to access struct members.
    friends.names;
}


/* Classes-----------------------------------------------------------
 * Thay are the C++ imlementation of OOP.
 * Thay have all modren OOP features.
 * Camel case naming convention is used to name classes.
 * Classes are ended with semicolon.
 * `m_` is used for private member variables. 
 * Class member variables are private by defaulte.
 * We can use { public, private, protected } kaywords to manage the member variables accesablity.
 * The class constructor is a method named with class name and does not has return type. (acually it return the class it self)
 * Constructorcan have paramters which used as a class inputs.
 * Destructors are functions (or methods) called when The class dies (deallocated).
 * Destructors have the same class name but beggined with `~` <==> ~ClassName
 * static keyword is a variable shared with all instenses.
 */

class Person                                               // This the main syntax for C++ classes. 
{
public:
    char* firstName;                                       // This the class atributes ( Variables ) 
    void someMethod(){}                                    // Defining methods as a normal funcion.
};


class Weather
{
public:                                                    // public vaibles and methods
    float windSpeed = 3;

protected:
    char protectedVar;                                     // Accessed from dereved class (Chiled)

private:
    int m_secureNumber;                                    // The convention is to prefix any private variable 'm_' refaring to member variable
};



void Classes()
{
    Person Joe;                                            // Taking an instance from the class.
    Joe.firstName = "Joe";                                 // We can assign values for instance variables
    Joe.someMethod();                                      // Calling methods.


    // Encapsulation
    Weather today;
    today.windSpeed;                                       // Accissing a public variable.
    // today.protectedVar;                                 // This variable is only accessable on it's class on any derived class from it.
    // today.secureNumber;                                 // Not accessable exept from it's class.
}

// Constructors-----------------------------------------------------
// Thay are used to initilize the class values.
// We can Define mutible constructors for the class (over loads)
// The constructor can be implemented outside the class.

class Cat
{
public:                                                    // Cinstructors should be public other wise we can not construct an instenses form the class.  
    Cat() {}                                               // this is the defalute constructor.
    Cat(std::string name)                                  // this constructor used if we provide one string argument.
    {
        m_name = name;
    }

    Cat(std::string name, int age)                         // I beleave this systax is more eficiant. 
    :m_name(name), m_age(age)  {}                          // This syntaxis commonly used to initlize variables 

    Cat(std::string name, int age, std::string color)      // Constructor for three arguments.  
    : Cat(name, age)                                       // We can re-use previose constructor. 
    {
        m_color = color;                                   // We have to assign additional explicitly.
    }

private:
    std::string m_name;
    int m_age;
    std::string m_color;
};


void Constructors()
{
    Cat katty = {"Katty"};                                 // Using one argument constructor.
    Cat Spot = Cat("Spot", 1, "white");                    // Using the three argument constructor.

}

// Operators OverLoading---------------------------------------------
// When we deal with operators inside class we does not affact the globle operator.
// We can affact the globle operators by writing `operator` functions in globle scope.
// We can create our oun operators using ""# syntax.
// We cannot Overload this operators { sizeof, typeid, `.`, `::`, `?:` }


// Ordinary class.
class Value
{
public:
    Value(float value)                                     // Constructor.
    : m_value(value) {}

    // This is the main syntax for operator overloading
    Value operator+(const Value& other)                    // Here is `+` overloading
    {
        return m_value + other.value();
    }

    Value operator-(const Value& other)                    // `-` overloading
    {
        return m_value - other.value();
    }
 
    float value() const { return m_value; }                // Simple getter.
private:
    float m_value;                                         // Praivate float value.
};



void OperatorOverloading()
{
    Value val1(0.5);                                       // Instancing classes.
    Value val2(1.5);

    Value val3 = val1 + val2;                              // Now we can implement addition and subtraction.
    Value val4 = val1 - val2;
}

// Reference---------------------------------------------------------

int main() {
    Variables();
    standardIO();
    CStyledArrays();
    Array();
    Casting();
    NumbersRepresentations();
    CStyleStrings();
    String();
    booleanOperators();
    bitWiseOperators();
    ifStatement();
    ternaryIfStatement();
    Switch();
    loops();
    RawPointers();
    References();
    FileHandling();
    AnonomusScope();
    ConstantExpresions();
    UserDefinedLitrals();
    Enums();
    structs();
    Classes();
    OverLoading();
    OperatorOverloading();
    Constructors();
}
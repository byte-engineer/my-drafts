
#############     #####         #####  #######################  ######          ######          ###########           #########        ######
###############    #####       #####   #######################  ######          ######       ##################       ##########       ######
#####      #####    #####     #####    #######################  ######          ######   ########         ########    ###########      ######
#####      #####      ##### #####              ######           ######          ######  #######             #######   ###### ######    ######
#####     #####         #######                ######           ######################  #######              #######  ######  ######   ######
#############            #####                 ######           ######################  #######              #######  ######   ######  ######
#####                    #####                 ######           ######          ######   #######            #######   ######     ##### ######
#####                    #####                 ######           ######          ######    ########        ########    ######      ###########
#####                    #####                 ######           ######          ######       ##################       ######       ##########
#####                    #####                 ######           ######          ######          ###########           ######        #########

#Intro-----------------------------------------------------------------

#|> Python scripting interpretative programming langauge.
#|> Python have a great comunity and large support.
#|> Python have an easy syntax and nise error handelling.
#|> Python used in many applications like AI, web developing, desktop apps, Others.

#Run the code----------------------------------------------------------

#|> Download python from there oficial website
#|> Don't forget to add python to the bath. 
#|> Create a file (file_name.py)
#|> When you choose your file name DON'T use spaces.
#|> You can create a file in VScode by writing this commend in CMD => code file_name.py
#|> Write python script in the file.
#|> Save the file.
#|> Open the terminal.
#|> You can use the following shortcut to open the terminal if you use VScode as a text editor => (ctrl + ~)
#|> GO to directory which your file located.
#|> Use this commend in terminal to change directory => cd path_to_your_file.
#|> To run the code write in terminal => python file_name.py

#Print-----------------------------------------------------------------

#|> We use print() to display text (string).
#|> It print new line(\n) in the end by defult.
#|> We can use print() also to write on files. (later on the course)

print("Hello! ")                                                       # Result => "Hello! "
print("Hello", "World")                                                # We can input many inputs at once.
print("Hi " * 3)                                                       # Rebeat it 3 times.       |Result => "Hi Hi Hi"
print("Hi ", end= "!!")                                                # End by defult = "\n"     |Result => "Hi !!"
print("Hi", "my", "friend", sep= ", ")                                 # Seprator by defult = " " |Result => "Hi, my, friend"
print("Force it", flush= True)                                         # To force the output to flushed it immediately.Try to do this commend if the function dosn't work.

#Comments--------------------------------------------------------------

# this is comment!                                                     # Add hash to make comment.
# print("Hi guys! ")                                                   # We can use comment to prevent code form running.
"""This is not commend"""                                              # This is non-assigned string(text).

#Data types------------------------------------------------------------

#|> We use built-in function called type() to detrim the type of data.
#|> Data types in python [ints, floats, strings, lists, tuples, sets, dictionarys]
#|> All data in python are objects.
#|> We will dive in all this types later on course.

type(-10)                                                              # Result => "int"   |Integer number.
type(1.075)                                                            # Result => "float" |Floating point number.
type(True) ; type(False)                                               # Result => "bool"  |Boolean value.
type("Python")                                                         # Result => "str"   |String.
type([1, 2, 3, 4, 5, 6])                                               # Result => "list"  |List.
type((1, 2, 3, 4, 5, 6))                                               # Result => "tuple" |Tuple.
type({1, 2, 3, 4, 5, 6})                                               # Result => "set"   |Set.
type({"One" : 1, "Two" : 2, "Three" : 3})                              # Result +> "dict"  |Dictionary.

#Variables-------------------------------------------------------------

#|> In python you don't need to detrim the type of variable.
#|> You can think of variables as a space in memory.
#|> We can use letters (A-Z) or (a-z) and underscores.
#|> We can NOT start with numbers or special charecters like "!@#$%^&*()-+=".
#|> We can include numbers in the middel of variable.
#|> Some words are reserved so we can't use it as a variable.

My_first1_variable = "Hello ,World!"                                   # Assign "Hello ,World!" to my variable.
print(My_first1_variable)                                              # Result => "Hello ,World!".
a, b, c = 1, True, "nice"                                              # We can assign multiple variables in one time.

help("keywords")                                                       # We use this commend to print out reserved words in the language.


#Ecape characters------------------------------------------------------

# newline
print("this is \nnew line")                                            # Will print "new line" in new line.

# Backslash                                                            # Generaly backslash escape any element after it.
print("there is great language called \"Python\"")                     # Use backslash it escape double quotes and single qoutes.Result => "there is great language called "Python""

# Backspace
print("Hello,\b World!")                                               # Perform backspace so it delete the comma |Result => "Hello World!"

# tab
print("This is\ttap")                                                  # tap by defult equals several spaces.         |Result => "This is tap"

# Hex characters
print("\x48\x65\x6C\x6C\x6F")                                          # We write Hexadecimal value for ASCII character.

#Strings---------------------------------------------------------------

text1 = "Hi "
text2 = "my friend."
essay = \
"""
Hi my ferinds, 
today I will program in python
thank you.
"""                                                                    # We can perform multiple line string by using three double or single quots.

# Concatenation
full_text = text1 + text2                                              # We use + to merge two strings.

#Indexind and slicing--------------------------------------------------

#|> Our strings are ordered by indexs.
#|> Python use (Zero Base Indexing) that is mean the first character has index zero.
#|> Indexing allow for us to accesse any character of string.
#|> Slicing allow us to accesse many characters of string at once.

Wisdom1 = "Don't fight someone who has nothing to lose"

# Indexing (Access singel character)
Wisdom1[0]                                                               # Index[0]   => "D"  , We start count from zero.
Wisdom1[9]                                                               # Index[9]   => "h"

Wisdom1[-1]                                                              # Index[-1]  => "s"  , For negatives we start counting from the last.
Wisdom1[-37]                                                             # Index[-37] => "f"

# Slicing (Access multiple characters)                                   # Syntax --> srting[start:end:steps] end not included.
Wisdom1[5: 11]                                                           # Result => "fight"
Wisdom1[-15: -8]                                                         # If we write a negetive values it will start counting from the last. |Result => "nothing"

Wisdom1[: 11]                                                            # If start not written it will start from zero.                       |Result => "Don't fight"
Wisdom1[20:]                                                             # If end not written it will go the all the way to the end.           |Result => "who has nothing to lose"
Wisdom1[:]                                                               # Full string.

Wisdom1[::2]                                                             # Third value is for steps so in this case it will ignore first character and include the second and all the way to the end.
Wisdom1[::3]                                                             # It will ignore first two characters and include the third and complete all the way to the end.

#String methods---------------------------------------------------------

Wisdom2 = "  life has a large spaces..!  "
Counter = "1,2,3,4,5,6,7,8"

len("Learn python")                                                     # It measures the length of the string.     |Result => 12

# strip() rstrip() lstrip()
Wisdom2.strip()                                                         # Will remove spaces from both sides.
Wisdom2.rstrip()                                                        # Will remove spaces from right side.
Wisdom2.lstrip()                                                        # Will remove spaces from lift side.

Wisdom2.split("!.")                                                     # Will remove all "." and "!" from first and end of the string.

# zfill()                                                               # Filling string by adding zeros on the lift
"10".zfill(3)                                                           # Result => "010"

# title()                                                               # Make the first letter on every word in apper case.
Wisdom2.title()                                                         # Result => "Life Has A Large Spaces..!  "

# capitalize()                                                          # It just make the first character in apper case.
Wisdom2.capitalize()                                                    # Result => "Life has a large spaces..!"

# apper() lower()                                                       # Convert all the characters in upper case.
Wisdom2.upper()                                                         # Result => "  LIFE HAS A LARGE SPACES..!"
"DONT SMOKE!".lower()                                                   # Result => "dont smoke!"

# split() rsplit()                                                      # Split the string according to certian seprator and but it on a list, syntax => str.split(seprator, number splits).
Wisdom2.split()                                                         # By defult the seprator set to space " "|Result => ['life', 'has', 'a', 'large', 'spaces..!']
Counter.split(",")                                                      # Result => ['1', '2', '3', '4', '5', '6', '7', '8'], Set seprator to ",".
Counter.split(",", 3)                                                   # Result => ['1', '2', '3,4,5,6,7,8'], We have two splits.
Counter.rsplit(",", 3)                                                  # It start from the right instead of lift |Result => ['1,2,3,4,5', '6', '7', '8']

# center() rjust() ljust()                                              # Insert characters after and before the string, Syntax => str.center(final string length, "filler")
"Delete".center(10)                                                     # Result => "  Delete  "
"Dont Delete".center(15, "^")                                           # Result => "^^Dont Delete^^"
"Delete".rjust(10, "-")                                                 # Result => "Delete----"  
"Delete".ljust(10, "-")                                                 # Result => "----Delete"


# count()                                                               # count number of repetitions, syntax => str.count("target", start, end) --> int
Wisdom2.count("a")                                                      # Result => 4

# swipcase()                                                            # swips the case of string.
"bE CAREFUL".swapcase()                                                 # Result => "Be careful"

# startswith() endswith()                                               # Cheak if the string start/end with certian character, syntax => str.startwith("target", start, end)
"Nice".startswith("N")                                                  # Result => True
"God game".endswith("e")                                                # Result => True

# index() find()                                                        # find the index for certian character, index("substring", start, end)
Wisdom2.index("l")                                                      # Result => 2  |if there is no result we will get error.
Wisdom2.find("o")                                                       # Result => -1 |if there is no result we will get -1.

# expandtaps()                                                          # Control tap size.
"Python\trespect\ttaps".expandtabs(3)                                   # Every tap will equal 3 spaces.

# islower() isupper()                                                   # Cheak if the string upper or lower
"HELLO".isupper()                                                       # Result => True
"hello".islower()                                                       # Result => True

# isnumeric() isalpha() isalnum()                                       # Cheak if string number/lphabtic/both.
"13".isnumeric()                                                        # Result => True 
"13".isalpha()                                                          # Result => True 
"13".isalnum()                                                          # Result => True 

# replace()                                                             # from it's name it replace string with other string
"one two three one two three".replace("one", "1")                       # Result => "1 two three 1 two three"
"one two three one two three".replace("one", "1", 1)                    # It will replace first "one" only

# join()                                                                # Convert list to string.
"-".join(["my", "name", "is", "..."])                                   # Result => "my-name-is-..."

#String formating------------------------------------------------------

option2 = "Science"
option1 = "Money"
year = 1980
score = 10000000000
ratio = 0.75

# Concatenation method
print("hello I love " + option2 + " and " + option1)                    # this method only accept strings

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
## place holders method
#|> This method also used in C.
#|> This method use different holder place for different data types:
#|> %s --> String
#|> %d --> Integere
#|> %f --> Float

print("%s and %s unlock any door" % (option2, option1))                 # Result => "Science and Money unlock any door
print("I born in %d,Iam younger than %f poeple!" % (year, ratio))       # Result => "I born in 1980,Iam younger than 0.750000 poeple!"

print("this a float number %.3f with three decimal places." % ratio)    # float control   |Result => "this a float number 0.750 with three decimal places."
print("Will print first three characters %.3s" % option1)               # string truncate |Result => "Will print first three characters Mon" 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
## Formate method
#|> {:s} --> String
#|> {:d} --> Integere
#|> {:f} --> Float

print("{} and {} unlock any door".format(option2, option1))                  # Result => "Science and Money unlock any door
print("I born in {:d},Iam younger than {:f} poeple!".format(year, ratio))    # Result => "I born in 1980,Iam younger than 0.750000 poeple!"

print("this a float number {:.3f} with three decimal places.".format(ratio)) # float control   |Result => "this a float number 0.750 with ttree decimal places."
print("Will print first three characters {:.3s}".format(option1))            # string truncate |Result => "Will print first three characters Mon" 
print("my score is: {:_d} or {:,d}".format(score, score))                    # Result => "my score is: 10_000_000_000 or 10,000,000,000"

# syntax --> {index:.num|type} --> .format(variable)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
## Version 3.6+ method

print(f"I love {option1}")                                              # Latest way to format |Result => "I love Money"

#Nunbers---------------------------------------------------------------

#|> We have tree types of numbers: Integers, floats and complex numbers
#|> We can convert types to others.

# Integers
23                                                                      # Examples for integers 
-55

# floats
1.52                                                                    # Examples for floatss 
-8.0

# complex numbers
5+2J                                                                    # Examples for complex numbers
-3.4+4J

# convertions
int(23.7)                                                               # To convert to integer. |Result => 23
float(3)                                                                # To convert to float.   |Result => 3.0
complex(8.5)                                                            # To convert to complex. |Result => 8.5+0j

#Arithmetic operations-------------------------------------------------

#|> Addition       ---> [+]
#|> Subtraction    ---> [-]
#|> Multiplication ---> [*]
#|> Division       ---> [/]
#|> Exponent       ---> [**]
#|> Modulus        ---> [%]
#|> Floor Division ---> [//]

1 + 54                                                                  # Result => 55
5 - 70                                                                  # Result => 65
11 * 10                                                                 # Result => 110
70 / 5                                                                  # Result => 14.0
8 ** 2                                                                  # Result => 49
9 % 6                                                                   # Result => 3
9 // 6                                                                  # Result => 1

#Lists------------------------------------------------------------------

#|> Lists are mutable so we can edit them easly.
#|> Lists are not ararys.
#|> Lists can contain any type of data inside it.
#|> We use zero base indexind to access any element on the list.
#|> We can access many elements at once by using slicing.

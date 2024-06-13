
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
#|> We can use letters (A-Z) or (a-z) and undersResults.
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

print(r"I wanna to write \n without escaping")                         # No escapes will be implemented also called "raw string".
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

Wisdom2.strip("!.")                                                     # Will remove all "." and "!" from first and end of the string.

# zfill(int)                                                            # Filling string by adding zeros on the lift
"5".zfill(3)                                                            # Result => "005"
"45".zfill(3)                                                           # Result => "045"
"645".zfill(3)                                                          # Result => "645"

# title()                                                               # Make the first letter on every word in apper case.
Wisdom2.title()                                                         # Result => "Life Has A Large Spaces..!  "

# capitalize()                                                          # It just make the first character in apper case.
Wisdom2.capitalize()                                                    # Result => "Life has a large spaces..!"

# apper() lower()                                                       # Convert all the characters in upper case.
Wisdom2.upper()                                                         # Result => "  LIFE HAS A LARGE SPACES..!"
"DONT SMOKE!".lower()                                                   # Result => "dont smoke!"

# split(str, int) rsplit(str, int)                                      # Split the string according to certian seprator and but it on a list, syntax => str.split(seprator, number splits).
Wisdom2.split()                                                         # By defult the seprator set to space " "|Result => ['life', 'has', 'a', 'large', 'spaces..!']
Counter.split(",")                                                      # Result => ['1', '2', '3', '4', '5', '6', '7', '8'], Set seprator to ",".
Counter.split(",", 3)                                                   # Result => ['1', '2', '3,4,5,6,7,8'], We have two splits.
Counter.rsplit(",", 3)                                                  # It start from the right instead of lift |Result => ['1,2,3,4,5', '6', '7', '8']

# center(int, str) rjust(int, str) ljust(int, str)                      # Insert characters after and before the string, Syntax => str.center(final string length, "filler")
"Delete".center(10)                                                     # Result => "  Delete  "
"Dont Delete".center(15, "^")                                           # Result => "^^Dont Delete^^"
"Delete".rjust(10, "-")                                                 # Result => "Delete----"  
"Delete".ljust(10, "-")                                                 # Result => "----Delete"


# count(str)                                                            # count number of repetitions, syntax => str.count("target", start, end) --> int
Wisdom2.count("a")                                                      # Result => 4

# swipcase()                                                            # swips the case of string.
"bE CAREFUL".swapcase()                                                 # Result => "Be careful"

# startswith(str) endswith(str)                                         # Cheak if the string start/end with certian character, syntax => str.startwith("target", start, end)
"Nice".startswith("N")                                                  # Result => True
"God game".endswith("e")                                                # Result => True

# index(str) find(str)                                                  # find the index for certian character, index("substring", start, end)
Wisdom2.index("l")                                                      # Result => 2  |if there is no result we will get error.
Wisdom2.find("o")                                                       # Result => -1 |if there is no result we will get -1.

# expandtaps(int)                                                       # Control tap size.
"Python\trespect\ttaps".expandtabs(3)                                   # Every tap will equal 3 spaces.

# islower() isupper()                                                   # Cheak if the string upper or lower
"HELLO".isupper()                                                       # Result => True
"hello".islower()                                                       # Result => True

# isnumeric() isalpha() isalnum()                                       # Cheak if string number/lphabtic/both.
"13".isnumeric()                                                        # Result => True 
"13".isalpha()                                                          # Result => True 
"13".isalnum()                                                          # Result => True 

# replace(str, str)                                                     # from it's name it replace string with other string
"one two three one two three".replace("one", "1")                       # Result => "1 two three 1 two three"
"one two three one two three".replace("one", "1", 1)                    # It will replace first "one" only

# join()                                                                # Convert list to string.
"-".join(["my", "name", "is", "..."])                                   # Result => "my-name-is-..."

#String formating------------------------------------------------------

option2 = "Science"
option1 = "Money"
year = 1980
sResult = 10000000000
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
print("my sResult is: {:_d} or {:,d}".format(sResult, sResult))                    # Result => "my sResult is: 10_000_000_000 or 10,000,000,000"

# syntax --> {index:.num|type} --> .format(variable)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
## Version 3.6+ method

print(f"I love {option1}")                                              # Latest way to format |Result => "I love Money"
print(f"I love {option1:.3}")                                           # Result => "I love Mon"

#Nunbers---------------------------------------------------------------

#|> We have tree types of numbers: Integers, floats and complex numbers
#|> We can convert types to others.
#|> We cannot convert other types to complex.

# Integers
23                                                                      # Examples for integers 
-55

# floats
1.52                                                                    # Examples for floats
-8.0

# complex numbers
5+2J                                                                    # Examples for complex numbers
-3.4+4J

# convertions
int(23.7)                                                               # To convert to integer. |Result => 23
float(3)                                                                # To convert to float.   |Result => 3.0
complex(8.5)                                                            # To convert to complex. |Result => 8.5+0j

#Arithmetic operations-------------------------------------------------

#|> Addition       ---> [+ ]
#|> Subtraction    ---> [- ]
#|> Multiplication ---> [* ]
#|> Division       ---> [/ ]
#|> Exponent       ---> [**]
#|> Modulus        ---> [% ]
#|> Floor Division ---> [//]

1 + 54                                                                  # Result => 55
5 - 70                                                                  # Result => -65
11 * 10                                                                 # Result => 110
70 / 5                                                                  # Result => 14.0
8 ** 2                                                                  # Result => 49
9 % 6                                                                   # Result => 3
9 // 6                                                                  # Result => 1

#More Advansed operations-----------------------------------------------

# string conversion
ord("A")                                                                # It convert string character to ASCII/Unicode| Result => 65
chr(128522)                                                             # It convert ASCII/Unicode to string character| Result => "😊"

# bitwise operations
0b0101                                                                  # Binary representation of 5 in decimal.
0x3fff                                                                  # Hexadecimal representation of 16383 in decimal.
0o5642                                                                  # Octal representation of 2978 in decimal.

bin(23)                                                                 # convert the decimal number to binary.    |Result => 0b10111
hex(1024)                                                               # convert the decimal number to hexadecimal|Result => 0x3ff
oct(42)                                                                 # convert the decimal number to octal      |Result => 0o52

~6                                                                      # NOT operation in binary.                 |Result => -7
2 & 4                                                                   # AND operation in binary.                 |Result => 0
8 | 5                                                                   # OR operation in binary.                  |Result => 13
3 ^ 9                                                                   # XOR opration in binary.                  |Result => 10
3 << 1                                                                  # Lift shift by 1 bits.                    |Result => 6   0011 --> 0110
6 >> 1                                                                  # Right shift by 1 bits.                   |Result => 3   0110 --> 0011

#Lists------------------------------------------------------------------

#|> Lists are mutable so we can edit them easly.
#|> lists are orderd and Unique.
#|> Lists are not ararys.
#|> Slicing and indexing in lists very same in strings.
#|> To create a list We put our data between square brackets "[]" and sprate elements by using comma ",".
#|> Lists can contain any type of data inside it.
#|> We use zero base indexind to access any element on the list.
#|> We can access many elements at once by using slicing.

data = [325 , "list", True, 5.75, "One", 21]                            # this a list. lists can contain any type of data.
composit = [["One", "Two", "Three"], [1, 2, 3]]                         # lists can contain other lists.
empty = []                                                              # impty list.

# slicing and Indexing

data[0]                                                                 # Result => 325
data[-2]                                                                # Result => "One"

data[1 :4]                                                              # Result => ["list", True, 5.75]
data[::1]                                                               # Whole list.
data[::2]                                                               # Result => [325, True, 'One']

composit[0]                                                             # Result = ["One", "Two", "Three"]
composit[0][-1]                                                         # Result = "Three"
composit[0][-1][2]                                                      # Result = "r"

# list editing

data[-1] = False                                                        # Edited list => [325 , "list", True, 5.75, "One", False]
data[0:4] = ["Deleted"]                                                 # Edited list => ['Deleted', 'One', False]
data[-2:] = []                                                          # Edited list => ['Deleted']

#List methods-----------------------------------------------------------

students = ["Beatriz", "Charissa", "January", "Tyrell", "Demi", "Red"]
newstudents = ["Harry", "Ron"]
numbers = ["One", "Two",3 ,1 ,2 ,3]

# appaend(element)
students.append("Brayden")                                              # Add "Bryden" To the list and put it in the last.

# extend(list)
students.extend(newstudents)                                            # Estend a list with other list. |students = ['Beatriz', 'Charissa', 'January', 'Tyrell', 'Demi', 'Red', 'Brayden', 'Harry', 'Ron'] 

# remove(element)
students.remove("January")                                              # It removes "January" but this method can remove ONE element form the list.

# reverse()
students.reverse()                                                      # Result = ['Ron', 'Harry', 'Brayden', 'Red', 'Demi', 'Tyrell', 'Charissa', 'Beatriz']

# sort(reverse= bool)                                                   # It works for numbers also but not numbers mixed with stings.
students.sort(reverse= False)                                           # Result => ['Beatriz', 'Brayden', 'Charissa', 'Demi', 'Harry', 'Red', 'Ron', 'Tyrell']
students.sort(reverse= True)                                            # Result => ['Tyrell', 'Ron', 'Red', 'Harry', 'Demi', 'Charissa', 'Brayden', 'Beatriz']

# copy()
copiedNum = numbers.copy()                                              # copiedNum => ["One", "Two",3 ,1 ,2 ,3]

# count(element)
numbers.count(3)                                                        # number 3 rebeated two times |Result => 2

# index
students.index("Demi")                                                  # If not founded We get error |Result => 4


# clear()
students.clear()                                                        # students => [] 

# insert(index, element)                                                # Insert element before index.
numbers.insert(2, "Three")                                              # Result => ['One', 'Two', 'Three', 3, 1, 2, 3]

# pop(index)
numbers.pop(3)                                                          # It will return (numbers[3]) and remove it from the list.

#Tuples-----------------------------------------------------------------

#|> Tuple are immutable data typy
#|> Tuples are ordered and indexed.
#|> We put our data between two parenthesis.
#|> We can remove parenthesis and it will still Tuple
#|> We cannot delete or add elementts in tuples.
#|> Tuples can have different data types.
#|> Aperators used in lists and strings are also available in Tuples.

Rand = ("llama", "Go", 93, 29.999, False, False)                        # This a Tuple.
oneELement = 'C++',                                                     # This is a Tuple with one element.
alpha = 'A', 'B', 'C'                                                   # We can write tuples without parenthesis.

Rand[1]                                                                 # Rusult => "Go"
Rand[1: 4]                                                              # Rusult => ("Go", 93, 29.999)
Rand[1:: 2]                                                             # Result => ('Go', 29.999, False)

# Rand[4] = True                                                        # We will get Type error. Because Tuples are immutable.

# We can use count() and index() with tuples
Rand.count(False)                                                       # Result => 2
Rand.index(29.999)                                                      # Result => 3

# Tuple Destruct
first, second, third = alpha                                            # first = 'A'   second ='B'   third = 'C'

#Sets------------------------------------------------------------------- 

#|> Sets are immutable data type.
#|> Sets are Not ordered.
#|> We put our data between two curly braces.
#|> Set items is Unque So we cannot rebeat the same element twice.
#|> Set support immutable data only (numpers, strings, tuples).
#|> We cannot use indexing and slicing in Sets.

SetA = {1, 1, "One", "One", True, False}                                # Result => {'One', 1, False} |True removed because it equivalent to 1 which is already in the set.
SetC = {}                                                               # Empty Set.
SetB = {'a', 'b'}
SetD = {1, 2, 3}
SetE = {4, 5, 6}
SetG = {"Nice", "Good", "Exellent", "Awesome"}
SetH = {"Outstanding", "Exellent", "Nice"}


# clear()
SetB.clear()                                                            # Removes all elements from the set.

# union(set or more)
SetD.union(SetE)                                                        # Result => {1, 2, 3, 4, 5, 6}
SetD | SetE                                                             # Other syntax.

# update
SetA.update(SetE)                                                       # Update SetA with it self and union of others.

# add(one element)
SetB.add('C')                                                           # Add 'C' To SetB.

# copy()
SetF = SetE.copy()

# reomve(element)
SetF.remove(6)                                                          # Removes one element from the Set, But it generate error if not found.

# dicard(element)
SetF.discard(7)                                                         # Same remove but it not generate errors.

# pop()
SetA.pop()                                                              # Return random element form the set and delete it.

# diffrance(set) difference_update(set)                                 # Return the elenemts that exest in first but not second.
SetG.difference(SetH)                                                   # It will return {'Good', 'Awesome'}
SetG - SetH                                                             # Second syntax.
SetG.difference_update(SetH)                                            # SetG will equal {'Good', 'Awesome'}

# inetersection(set) inetersection_update(set)                          # Return the elenemts that exest in both sets.
SetG = {"Nice", "Good", "Exellent", "Awesome"}
SetH = {"Outstanding", "Exellent", "Nice"}
 
SetG.intersection(SetH)                                                 # It will return {'Nice', 'Exellent'}
SetG & SetH                                                             # Second syntax.
SetG.intersection_update(SetH)                                          # SetG will equal {'Nice', 'Exellent'}

# symetric_difference(set)  symetric_difference_update(set)             # Return the elenemts that NOT exest in both sets.
SetG = {"Nice", "Good", "Exellent", "Awesome"}
SetH = {"Outstanding", "Exellent", "Nice"}

SetG.symmetric_difference(SetH)                                         # It will return {'Awesome', 'Outstanding', 'Good'}
SetG ^ SetH                                                             # Second syntax.
SetG.symmetric_difference_update(SetH)                                  # SetG will equal {'Awesome', 'Outstanding', 'Good'}

#Dectionary-------------------------------------------------------------

#|> Dictionary items are enclosed in curly baces.
#|> Dictionary containces Key : Value
#|> Dictionary Key must be immutable data type(numpers, strings, tuples).
#|> Dictionary can be any type of data.
#|> Dictionary is not ordered but we can access the values using the keys.
#|> We can NOT rebeat the Keys in Dictionarys.

User = {                                                                # This a dictionary.
    "name"      : "Unknown"                                ,
    "age"       : 29                                       ,
    "hobbies"   : ["Programming", "3D Modeling", "Reading"],
    "occupation": "Truth seeker"
}

Grid = {                                                                # This a two-dimensional dictionary.
    'row1': {'col1': 1, 'col2': 2, 'col3': 3},
    'row2': {'col1': 4, 'col2': 5, 'col3': 6},
    'row3': {'col1': 7, 'col2': 8, 'col3': 9}
}

# Extract the data 
User["age"]                                                             # Result => 29
User.get("age")                                                         # Same result.

Grid["row2"]["col3"]                                                    # Result => 6
Grid.get("row2").get("col3")

Grid['row4'] = {'col1': 10, 'col2': 11, 'col3': 12}                     # I add a new element to the dictionary.
Grid.update({'row5' : {'col1': 13, 'col2': 14, 'col3': 15}})            # Other syntax.

#Dictionary methods-----------------------------------------------------

# keys()  values()
User.keys()                                                             # Return all keys   => ['name', 'age', 'hobbies', 'occupation']
User.values()                                                           # Return all values => ['Unknown', 29, ['Programming', '3D Modeling', 'Reading'], 'Truth seeker']

# copy()
user = User.copy()                                                      # Shallow copy.

# setdefault(key ,value)
User.setdefault("name" ,"Known")                                       # Return => "Unknown"
User.setdefault("country" ,"World")                                    # Will add this item to dictionary.

# popitem()
User.popitem()                                                         # Return last element in the dictionary and Remove it from the dictionary.

# items()
User.items()                                                           # Result => [('name', 'Unknown'), ('age', 29), ('hobbies', ['Programming', '3D Modeling', 'Reading']), ('occupation', 'Truth seeker')]

# fromkeys(keys, values)
a = (1, 2, 3 ,4)
b = ("One", "Two")
dict.fromkeys(a, b)                                                     # Result => {1: ('One', 'Two'), 2: ('One', 'Two'), 3: ('One', 'Two'), 4: ('One', 'Two')}

# clear()
User.clear()                                                            # Remove all items in the dictionary.

#Boolean----------------------------------------------------------------

#|> Boolean can be only True or False.
#|> All this Comparison Operators generate boolean values(< > <= <= == !=).
#|> We can convert most data types to boolean values.
#|> We have Three boolean operators(and, or, not).

100 <  200  # True
100 >  200  # False
200 >= 200  # True
200 <= 200  # True
100 == 200  # False
100 != 200  # True

# Conversion
bool(False)     # All this return False, Otherwise True.
bool(0)
bool('')
bool([])
bool(())
bool({})

# and
True and True # True                                                    # True if both inputs are True.

# or
True or False # True                                                    # True if one of inputs is True.

# not
not True    # False                                                     # Invert the input.
not False   # True

#Assignment Operators---------------------------------------------------

var = 12                                                                # Assign 12 to var.

var +=  1                                                               # var = var + 1
var -=  1                                                               # var = var - 1
var *=  1                                                               # var = var * 1
var /=  1                                                               # var = var / 1
var **= 1                                                               # var = var ** 1
var %=  1                                                               # var = var %  1
var //= 1                                                               # var = var // 1

#Type Conversion--------------------------------------------------------

bool(23)                                                                # Result => True
int(23.5)                                                               # Result => 23
str(23)                                                                 # Result => "23"
list((23, 24, 25))                                                      # Result => [23, 24, 25]
tuple([23, 24, 25])                                                     # Result => (23, 24, 25)
set([23, 24, 25])                                                       # Result => {23, 24, 25}
dict((("A", 1), ("B", 2), ("C", 3)))                                    # Result => {'A': 1, 'B': 2, 'C': 3} |We can use nisted lists also.

#User input-------------------------------------------------------------

#|> To get data from the user.
#|> User can enter a strings in the terminal.

Response = input("Enter Data: ")                                        # Returns the data that user enter as string.

#Control Flow-----------------------------------------------------------

#|> Control flow is one of the most important subjects in any programing langauge.
#|> In python there is three main control flow commands which are (if, elif, else).
#|> We can change the code path by control flow conditionals.

firstcondition = True
secondcondition = True

# if  elif else
if firstcondition :
    print("firstCondition is True")
elif secondcondition :
    print("second condition is True and first is not")
else:
    print("no True condition")

# short if
print("first Condition is True" if firstcondition else "condition false") # It not support (elif)                  

#Membership-------------------------------------------------------------

#|> in
#|> not in

name = "great person"
colors = ['red', 'blue', 'pink']

'g' in name                                                             # True
'red' in colors                                                         # True

#While loop-------------------------------------------------------------

#|> It execute the code bellow it till condition not be True.

X = 1
while X < 10:
    print(f"#{X}", end= "")
    X += 1
else :
    print("Loop done! ")                                                 # If the loop interrupted (breaked) this code will be executed.

#For loop----------------------------------------------------------------

#|> for item in iterable_object:
#       some thing to do with item.
#|> break    => Exit from the loop.
#|> continue => Stop current iteration.
#|> pass     => To escape (ignor) the whole conditional.

iterable_object = ['nice', 'great', 'awesome', 'good']

employees = {
    'John Doe'     : 'Software Engineer',
    'Jane Smith'   : 'Data Scientist'   ,
    'Alice Johnson': 'Product Manager'  ,
    'Robert Brown' : 'UX Designer'      ,
    'Emma Davis'   : 'DevOps Engineer'
}

for item in iterable_object:                                             # For loop in list.
    print(item)
    if item == 'awesome':
        break
else :
    print("Loop done! ")                                                 # If the loop interrupted (breaked) this code will be executed.

for name, job in employees.items():                                      # For loop in dictionary.
    print(f"* {name} hes job {job}.")

#Function And Return-----------------------------------------------------

#|> A Function is A Reusable Block Of Code Do A Task.
#|> A Function Run When You Call It.
#|> A Function Create To Prevent DRY (don't rebeat yourself).
#|> A Function Accept Elements as inputs When You Call It Called [Arguments]
#|> A Function returns Element To Deal With Called [Parameters]
#|> A Function Can Return Data After Job is Finished.
#|> A Function Can Do The Task Without Returning Data.
#|> There's A Built-In Functions and User Defined Functions.

def function_name():                                                     # Creating a function.
  return "Hello Python From Inside Function"                             # Function contant.

print(function_name())                                                   # Calling a function.

# Parameters And Arguments 
#|> def                     => Function Keyword [Define]
#|> say_hello()             => Function Name
#|> name                    => Parameter
#|> print(f"Hello {name}")  => Task
#|> say_hello("Ahmed")      => Calling the function |Ahmed is The Argument

def say_hello(n):

  print(f"Hello {n}")

say_hello("Daived")

#Packing and unpacking---------------------------------------------------

#|> We use Unpacking when don't know number of items that we going to use.
#|> *args => arg1, arg2, arg3
#|> Type of Unpacked arguments is a tuple

# tuples unpacking
def sum(factor, *numbers):                                               # We can enter any number of items that We want.
    Result = 0
    for i in numbers:                                                    # We almost use for loop to use unpacked items.
        Result += i
    return Result * factor

# dictionary unpacking
def skills(**skills):
    for key ,value in skills.items():
        print(f"{key} => {value}")

skills(HTML= '90%', CSS= '40%', JS= '10%')                              # As a user input. 
skills(**employees)                                                     # As a dictionary variable.

#Default parameters------------------------------------------------------

#|> User might not enter requared data to the function, So We set a default value to prevent errors.
#|> We must put the variables that has a default value in last of inputs of the function.

def favourite_color(color= "White"):                                     # We set a default value for color.
    print(f"your favourite color is: {color}")

# Globle and local variables---------------------------------------------

Testvar = 4                                                              # This is a globle variable.
def test():
    localvar = 3                                                         # Local variable.
    global Testvar                                                       # calling a globlr variable.
    Testvar = 39                                                         # Over write a globle variable.

#Function Recursion------------------------------------------------------

#|> Function inside itself called Recursion function.

def factorial(n):                                                        # Example
    if n == 0 or n == 1:                                                 # Base case: if n is 0 or 1, return 1
        return 1
    else:                                                                # Recursive case: call the function with n-1
        return n * factorial(n - 1)

#Lambda function---------------------------------------------------------

#|> It Has No Name
#|> You Can Call It Inline Without Defining It.
#|> You Can Use It In Return Data From Another Function.
#|> Lambda Used For Simple Functions and Def Handle The Large Tasks.
#|> Lambda is One Single Expression not Block Of Code.
#|> Lambda Type is Function.

def say_hello(name, age) : return f"Hello {name} your Age Is: {age}"     # Ordinary function.
hello = lambda name, age : f"Hello {name} your Age Is: {age}"            # lambda function.

# hello     => To store the result.
# "lambda"  => lable for define a lambla function.
# age, name =>  arguments of function.  

# Files Handling---------------------------------------------------------

#|> In Windows "\n" contains two characters.

#|> "a" Append  Open File For Appending Values, Create File If Not Exists.
#|> "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists.
#|> "w" Write   Open File For Writing, Create File If Not Exists.
#|> "x" Create  Create File, Give Error If File Exists.

import os                                                                # import module that contains some functions.(about this subject later in the course)

os.getcwd()                                                              # Returns current working directory also Written in CMD. |Result => c:\Users\####\Desktop\bilal\files\Codes\Python
os.path.abspath(__file__)                                                # absolute path for this file.                           |Result => c:\Users\####\Desktop\bilal\files\Codes\Python\Draft.py
os.path.dirname(os.path.abspath(__file__))                               # Name of the folder that hold this file                 |Result => c:\Users\####\Desktop\bilal\files\Codes\Python

# open('file_path', 'mode')

# Reading
file = open(r"c:\Users\Hp\Desktop\bilal\files\Codes\Python\Draft\myfile.txt", 'r') # Open a file in read mode.

file                                                                     # Returns all file data but not the contant.
file.name                                                                # Returns file name.
file.mode                                                                # Returns file mode.
file.encoding                                                            # Returns file encoding.

file.read()                                                              # Returns all the contant of the file.
file.read(5)                                                             # Read first 5 bytes.
file.readline()                                                          # Returns first line.
file.readline()                                                          # Returns second line.
file.readline(6)                                                         # Returns first 6 characters from third line.
file.readlines()                                                         # Retern a list  |Result => ['hello guys\n', 'How are you.\n', 'this is tips:\n', '-1 nice\n', '-2 good\n', '-3 exellent\n', '-4 outstanding\n']

file.seek(5)                                                             # Move the cursor to position after fifth character.
print(file.read())                                                       # Result => All string after fifth character.


# Writing
file = open(r"c:\Users\Hp\Desktop\bilal\files\Codes\Python\Draft\writefile.txt", 'w')   # Open a file in write mode, If not found will create.

file.write("How are you? \nAre you fine.\n")                                      # Over write Data with this new data In otherway It will delete whole data and write this new data.
file.writelines(["Go\n", "python\n", "C++\n" ])                                   # Will write this data to the file.

# Appending
file = open(r"c:\Users\Hp\Desktop\bilal\files\Codes\Python\Draft\writefile.txt", 'a')   # Open a file in append mode, If not found will create.
file.write("C\n")                                                                 # Add "C" without overwrite old data.
file.truncate(5)                                                                  # It will delete all characters except first 5 bytes after cursor.
file.tell()                                                                       # It Reterns the position of the cursor. |Notic: "\n" concidered as two characters.

#Some built-In functions-------------------------------------------------  

#|> all()
#|> any() 
#|> id()
#|> sum()
#|> round()
#|> range()
#|> abs()
#|> pow()
#|> min()
#|> max()
#|> slice()
#|> help()

check = [1, 2, 3, 4, 5]
Best = 34

# all(iterable object) 
all(check)                                                               # If all elements of check are True the function will return True.|Result => True

# any(iterable object)
any(check)                                                               # If at least one element True it will return True  |Result => True

# id(variable)
id(Best)                                                                 # It return the memory Adrress of the variable in memory.|Result => 140703970434520

# sum(irerable)
sum(check)                                                               # Result => 15

# round(number, decimal places)
round(30.269, 1)                                                         # Result => 30.3

# range(start, end, steps)                                               # If we don't one argument, will be considered as end.
list(range(5))                                                           # Result => [0, 1, 2, 3, 4]
list(range(1, 10, 2))                                                    # Result => [1, 3, 5, 7, 9]

# abs(number)
abs(-128)                                                                # Result => 128  |abslute value

# pow(base, exp, modulus)
pow(2, 5)                                                                # (2 ** 5)        => 32
pow(2, 5, 10)                                                            # (2 ** 5) % 10   => 2

# min(item, item, item, or iterator)
min(2, 3)                                                                # Result => 2 |minimum value.
min(check)                                                               # Result => 1

# max()
max(2, 3)                                                                # Result => 3 |maximum value.
max(check)                                                               # Result => 5

# slice(start, end, steps)
check[slice(1, 3, 1)]                                                    # Result => [2, 3]

help(print)                                                              # Returns Info about the function inside it.


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

#Map-------------------------------------------------------------------

#|> We use map when we want to generate Iterable object that from other iterable object.
#|> Map() acsept function and iterable object.

frinames = ["Doe", "Daived", "Jone"]

def formatnames(name):
    return f"- {name} -"

list(map(formatnames, frinames))                                       # Return => [['- Doe -', '- Daived -', '- Jone -']

list(map(lambda name: f"- {name} -", frinames))                        # Return => [['- Doe -', '- Daived -', '- Jone -'] |same result


#Filter----------------------------------------------------------------

#|> Filter Take A Function + Iterator.
#|> Filter Run A Function On Every Element.
#|> The Function Can Be Pre-Defined Function or Lambda Function.
#|> Filter Out All Elements For Which The Function Return True.
#|> The Function Need To Return Boolean Value So it convert result to boolean.


myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]
myTexts = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman"]

def checkNumber(num):
  return num > 10

def checkName(name):
  return name.startswith("O")
#                                                                      # Results in for loop 
filter(checkNumber, myNumbers)                                         # 19, 20, 100
filter(checkName, myTexts)                                             # "Osama", "Omer", "Omar", "Othman"
filter(lambda name: name.startswith("A"), myTexts)                     # "Ahmed"

#Reduce----------------------------------------------------------------

#|> Reduce Take A Function + Iterator.
#|> Reduce Run A Function On First and Second Element And Give Result.
#|> Then Run Function On Result And Third Element.
#|> Then Run Function On Rsult And Fourth Element And So On.
#|> Till One ELement is Left And This is The Result of The Reduce.
#|> The Function Can Be Pre-Defined Function or Lambda Function.

def sumAll(num1, num2):
    return num1 + num2

numbers = [1, 8, 2, 9, 100]

from functools import reduce

reduce(sumAll, numbers)                                                # ((((1 + 8) + 2) + 9) + 100)
reduce(lambda num1, num2: num1 + num2, numbers)                        # Result => 120

#Iterable & Iterator-----------------------------------------------------

#|> Iterable date type in python are (string, list, ...).
#|> We can convert iteralbe to iterator by using iter() function.
#|> We can go to next element in our iterable by using next() function.
#|> For loop call iter() automaticely behind the scene.

lang = "python"

itrlang = iter(lang)                                                     # Return => iterator
next(itrlang)                                                            # Result => 'p'
next(itrlang)                                                            # Result => 'y'
next(itrlang)                                                            # Result => 't'
next(itrlang)                                                            # Result => 'h'
next(itrlang)                                                            # Result => 'o'
next(itrlang)                                                            # Result => 'n'
# next(itrlang)                                                          # Result => error: Stopiteration


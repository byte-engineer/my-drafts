
#############     #####         #####   #########################  ######             ######          ###########           #########        ######
###############    #####       #####    #########################  ######             ######       ##################       ##########       ######
#####      #####    #####     #####     #########################  ######             ######   ########         ########    ###########      ######
#####      #####      ##### #####                ######            ######             ######  #######             #######   ###### ######    ######
#####     #####         #######                  ######            #########################  #######              #######  ######  ######   ######
#############            #####                   ######            #########################  #######              #######  ######   ######  ######
#####                    #####                   ######            ######             ######   #######            #######   ######     ##### ######
#####                    #####                   ######            ######             ######    ########        ########    ######      ###########
#####                    #####                   ######            ######             ######       ##################       ######       ##########
#####                    #####                   ######            ######             ######          ###########           ######        #########


#INTRO-----------------------------------------------------------------

#|> Python scripting interpretative programming langauge.
#|> Python have a great comunity and large support.
#|> Python have an easy syntax and nise error handelling.
#|> Python used in many applications like AI, web developing, desktop apps, Others.

#RUN THE CODE----------------------------------------------------------

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

#PRINT-----------------------------------------------------------------

#|> We use print() to display text (string).
#|> It print new line(\n) in the end by defult.
#|> We can use print() also to write on files. (later on the course)

print("Hello! ")                                                       # Result => "Hello! "
print("Hello", "World")                                                # We can input many inputs at once.
print("Hi " * 3)                                                       # Rebeat it 3 times.       |Result => "Hi Hi Hi"
print("Hi ", end= "!!")                                                # End by defult = "\n"     |Result => "Hi !!"
print("Hi", "my", "friend", sep= ", ")                                 # Seprator by defult = " " |Result => "Hi, my, friend"
print("Force it", flush= True)                                         # To force the output to flushed it immediately.Try to do this commend if the function dosn't work.

#COMMENTS--------------------------------------------------------------

# this is comment!                                                     # Add hash to make comment.
# print("Hi guys! ")                                                   # We can use comment to prevent code form running.
"""This is not commend"""                                              # This is non-assigned string(text).

#DATATYPES-------------------------------------------------------------

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

#VARIABLES-------------------------------------------------------------

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


#ECAPE_CHARACTERS------------------------------------------------------

# newline
print("this is \nnew line")                                            # Will print "new line" in new line.

# Backslash                                                            # Generaly backslash escape any element after it.
print("there is great language called \"Python\"")                     # Use backslash it escape double quotes and single qoutes.

# Backspace
print("Hello,\b World!")                                               # Perform backspace so it delete the comma |Result => "Hello World!"

# tab
print("This is\ttap")                                                  # tap by defult equals One spaces.         |Result => "This is tap"

# Hex characters
print("\x48\x65\x6C\x6C\x6F")                                          # We write Hexadecimal value for ASCII character.


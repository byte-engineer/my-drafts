# Draft\Librarys\OS.py

import os

path = r"C:\Users\Hp\Desktop\bilal\files\Codes\Python\Draft\REQs"



os.system("cls")                    # Commend In the termenal.

os.listdir(path)                    # return a list contains all dirctories and files in the path. 
os.mkdir(path+r"\new")              # create a new dirctory.
os.rmdir(path+r"\new")              # Remove dirctory.
os.remove(path)                     # Removes a file

# Curren working directory (CWD)
os.chdir("Draft")                   # Change current working dirctory.
os.getcwd()                         # Returns current working directory.

os.path.isfile(path)                # returns bool
os.path.isdir(path)                 # returns bool


# CPU number
os.cpu_count()                      # Return the number of CPUs (cores).|On my case => 8

# Get path
os.path.abspath(__file__)           # Return absulote path of this file.
__file__                            # Other sytax. | Not recomended

# exists
os.path.exists(path)                # Cheak if the path exist.

# get Directory name
os.path.dirname(path)               # Get the directory name.

# Base name
os.path.basename(path)              # Return the base name of the path. |Output => "REQs"

os.path.splitext(path)              # ['folder/file', '.txt'] 
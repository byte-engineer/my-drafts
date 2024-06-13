#Modules----------------------------------------------------------------

#|> Module is A File Contain A Set Of Functions.
#|> You Can Create Your Own Modules.
#|> All my modules are in (C:/Users/Hp/AppData/Local/Programs/Python/Python312)
#|> This is the oficial wepsite for built-In modules(https://docs.python.org/3/py-modindex.html).


# Importing
#| import (module_name)                                                  Import a module on my code.
#| from (module_name) import (function_name)                             Import a function from amodule.
#| module_name.function_name()                                           Call a function from pre-imported module, bracis are included.
#| function_name()                                                       Call a pre-imported function, bracis are included. 
# NOTIC: bracis are ONLY for claration.

# Examples
import math                                                              # math is built-In module in python.
from math import isqrt                                                   # isqrt is a function inside math module.
math.sin(30)                                                             # We using a function inside math module.
isqrt(25)                                                                # We using pre-imported function.

#External Packages-------------------------------------------------------

#|> We download External Packages from internet by using (pip) python packages manager.
#|> We search about external packages form (https://pypi.org/)

# PIP                                  If We have any problems with permisan We can add (--user).
# pip --version                        To chuck if pip exist.
# pip list                             List all installed packages with thair versions.
# pip install (package)                Install new package.
# pip install (package) --upgrade      Upgrade package.

# To check the contant of any module/package.
# dir(module/package)
print(dir(math))

# termcolor, pyfiglet-----------------------------------------------------
# External packages
import termcolor      # For more info: https://pypi.org/project/termcolor/
import pyfiglet       # for More info use this command (pyfiglet -h).

print(pyfiglet.figlet_format("python", font= "times"))                                     # Python ASCII art in termimal .
print(termcolor.colored("python", color= "yellow"))                                        # yellow python in terminal.

print(termcolor.colored(pyfiglet.figlet_format("python", font= "slant"), color= "yellow")) # compine those together.

#date & time--------------------------------------------------------------
# Built-In module
import datetime

# Current time & date 
datetime.datetime.now()                                                   # Returns current date & time  |Result => 2024-06-13 10:55:18.785626
datetime.datetime.now().year                                              # Returns current year         |Result => 2024
datetime.datetime.now().month                                             # Returns current month        |Result => 6
datetime.datetime.now().day                                               # Returns current day          |Result => 13
datetime.datetime.now().time().hour                                       # Returns current hour         |Result => 10
datetime.datetime.now().time().minute                                     # Returns current hour         |Result => 55
datetime.datetime.now().time().second                                     # Returns current hour         |Result => 18

# Specific Date
birthday  = datetime.datetime(1973, 4, 25)                                # Returns our Date in object.  |This all obligatory data.
lastparty = datetime.datetime(2014, 6, 11, 19, 33, 5, 2345)               # Returns our Date in object.
greatday  = datetime.datetime(2024, 8, 6)

lastparty - birthday                                                      # We can subtract the time.    |Result => 15022 days, 19:33:05.002345
(lastparty - birthday).days                                               # Just returns the Days.

# Date formating

greatday.strftime("%A")                                                   # day abbreviation name.                   |Result => Tue
greatday.strftime("%b")                                                   # Month abbreviation name.                 |Result => Aug
greatday.strftime("today is: %d, %B, %Y")                                 # We can compime all together              |Result => "today is: 06, August, 2024"
greatday.strftime("%x")                                                   # For more info in https://strftime.org/   |Result => 08/06/24







 
print(greatday.strftime("today is: %d, %B, %Y"))
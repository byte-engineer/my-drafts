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
greatday.strftime("today is: %d, %B, %Y")                                 # We can compine all together              |Result => "today is: 06, August, 2024"
greatday.strftime("%x")                                                   # For more info in https://strftime.org/   |Result => 08/06/24

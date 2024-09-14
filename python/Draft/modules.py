# termcolor, pyfiglet-----------------------------------------------------
# External packages
import termcolor      # For more info: https://pypi.org/project/termcolor/
import pyfiglet       # for More info use this command (pyfiglet -h).

print(pyfiglet.figlet_format("python", font= "times"))                                     # Python ASCII art in termimal .
print(termcolor.colored("python", color= "yellow"))                                        # yellow python in terminal.

print(termcolor.colored(pyfiglet.figlet_format("python", font= "slant"), color= "yellow")) # compine those together.

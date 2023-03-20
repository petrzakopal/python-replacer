import re # import of library
import argparse # for parsing command line arguments

# colorama for colors, easier than init class, maybe later
# source: https://github.com/tartley/colorama
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init(autoreset=True) # autoreset color on new line

# class with additional styles
class style:
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
 


argParser = argparse.ArgumentParser() # new object

argParser.add_argument("-if", "--inputfile", help="your input file") # adding argument

args = argParser.parse_args() # parsing args

# print("args=%s" % args) # shwo namespace

print("args.inputfile=%s" % args.inputfile) #prints args


dataName = args.inputfile

# checking if dataName was set as an input arg
if not dataName:
    # if it was not set as an argument, wait for user input
    print(style.BOLD+Fore.RED + "You did not select file with -if select file to transform now:"+style.END)
    dataName=input()


print("You have selected "+ dataName + " as an input file.\n")

#read input file hardcoded
# fin = open("data.txt", "rt")
fin = open(dataName, "rt")

#read file contents to string
data = fin.read()

# data = data.replace('máš', 'mášánek') # replaces every occurence of "máš" even in string "nemáš"
# data = re.sub(r'\bmáš\b', 'mášánek', data) # replaces only exact match of word
# word defined for python for \b: Matches the empty string, but only at the beginning or end of a word. A word is defined as a sequence of word characters.
# r before string means raw info here: https://docs.python.org/3/library/re.html

data = re.sub(r';', ',', data) # replaces every occurence of ;

#close the input file
fin.close()
#open the input file in write mode

fin = open("data.txt", "wt")
#overrite the input file with the resulting data

fin.write(data)

#close the file
fin.close()

print(Fore.YELLOW + "Replacement completed. Exiting program now.")

# build file with PyInstaller as follows
# python3 -m PyInstaller -F replace.py  

#update
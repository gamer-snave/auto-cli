#!/usr/bin/env python
import webbrowser
import sys
import re 

#User should choose between the two options
def search():
    print ("Choose between the two options")
    print ("1. Search on Google")
    print ("2. Search on Github")

# choice =("Enter your choice: ")
    choice = input("Enter your choice: ")

#If user chooses to search on Google
    if choice == "1":
        search = input("Enter your search: ")
        webbrowser.open("https://www.google.com/search?q=" + search)

#If user chooses to search on Github
    elif choice == "2":
        search = input("Enter your search: ")
        webbrowser.open("www.github.com/search?q=" + search)

    else:
        print ("Enter a valid choice")

# search()

#Check system arguments.

def automate():
    arg = sys.argv[1]
    if len(arg) > 4:
        website_link=arg
# Check if the website link is in the correct format using regex
    if not re.match('^(http|https)://' , website_link):
        print('Please enter a valid website link.')
        search()
    else:
        sys.exit()

    if arg == 'ai':
        arg = 'beta.openai/playground.com'
    elif arg == 'gh':
        arg = 'github.com'
    elif arg == 'yt':
        arg = 'youtube.com'
    else:
        print('Please enter a valid website link or keyword.')
        sys.exit()

# Open the website link in the default browser
    webbrowser.open(arg)

automate()

if __name__=='__main__':
    if len(sys.argv) < 1:
        #show help
        print('Usage:auto -s [Commad] -a [Argument]')
        if sys.argv[1] == "s":
            search()
        else:
             if sys.argv[1] == "a":
                automate()

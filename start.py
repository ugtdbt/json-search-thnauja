#! /usr/bin/python3.6
import components.inputvalue as inputvalue
import components.search as search
import components.fields as fields

def main():
    # Type 'quit' to exit at any time, Press 'Enter' to continue
    inputvalue.inputValueStart()

    # Main Menu
    menuItem = inputvalue.inputMainMenu()

    # If 1 or 2
    if menuItem == "1":
        search.start()
        main()
    elif menuItem == "2":
        fields.start()
        main()

main()
exit()
# End
import components.config as config

def inputValueStart():
    print("Type 'quit' to exit at any time, Press 'Enter' to continue")
    inputsvalue = input()
    if inputsvalue == "quit":
        exit()
    elif inputsvalue == "":
        return inputsvalue
    else:
        inputValueStart()


def inputMainMenu():
    print("""

        Select search options:
        * Press 1 to search Zenddesk
        * Press 2 to view a list of searchable fields
        * Type 'quit' to exit

    """)
    inputsvalue = input()
    if inputsvalue == "quit":
        exit()
    elif inputsvalue == "1" or inputsvalue == "2":
        return inputsvalue
    else:
        inputMainMenu()

def inputSearch():
    print("Select 1) Users or 2) Tickets 3) Organizations")
    inputsvalue = input()
    if inputsvalue == "quit":
        exit()
    elif inputsvalue == "1":
        return inputsvalue
    elif inputsvalue == "2":
        return inputsvalue
    elif inputsvalue == "3":
        return inputsvalue
    else:
        inputSearch()


def inputItem(searchId):
    print("Enter search term")
    inputsvalue = input()
    if inputsvalue == "quit":
        exit()
    elif searchId == "1" and inputsvalue in config.Userskey:
        return inputsvalue
    elif searchId == "2" and inputsvalue in config.Ticketskey:
        return inputsvalue
    elif searchId == "3" and inputsvalue in config.Organizationskey:
        return inputsvalue
    else:
        print("Invalid search term")
        inputItem(searchId)
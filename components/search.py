import components.inputvalue as inputvalue
# import ijson
import json

def start():
    searchId = inputvalue.inputSearch()
    itemId = inputvalue.inputItem(searchId)
    print("Enter search value")
    searchValue = input()

    if searchId == "1":
        json_filename = "./jsonfiles/users.json"
    elif searchId == "2":
        json_filename = "./jsonfiles/tickets.json"
    elif searchId == "3":
        json_filename = "./jsonfiles/organizations.json"

    
    f = open(json_filename, "r")
    objects = json.loads(f.read())
    for item in objects:
        if ( (type(item[itemId]) is not list and str(item[itemId]) == searchValue) or ( type(item[itemId]) is list and searchValue in str(item[itemId]) ) ):
            print("-------------------------------------------------------------------------------------")
            for key, value in item.items():
                print('{}{}{}'.format(key, ' '*(30-len(str(key))), value))
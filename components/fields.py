import components.config as config
import components.inputvalue as inputvalue
def start():
    print("""
----------------------------------------------------
Search Users with""")
    for userkey in config.Userskey:
        print(userkey)
    print("""----------------------------------------------------
Search Tickets with""")
    for ticketkey in config.Ticketskey:
        print(ticketkey)
    print("""----------------------------------------------------
Search Organizations with""")
    for organizationkey in config.Organizationskey:
        print(organizationkey)
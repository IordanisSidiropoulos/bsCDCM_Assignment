"""
#
# File            : 5_Dictionaries.py
# Created          : 19/01/2023 2:45 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Available under GNU Public License (GPL)
# Description     : Dictionaries
#
"""

if __name__ == "__main__":
    campuses = {}
    contacts = {"Iordanis.Sidiropoulos": 4536, "Antonella.Scanu": 2398, "Mikri.Eleni": 7648, "Info": 1234}
    contact_address = {"Iordanis.Sidiropoulos": "SevillePlace", "Antonella.Scanu": "Dublin 1",
                       "Mikri.Eleni": "Grand Canal", "info": "Ireland"}

    print(contacts)
    print(contact_address)

    print(contacts["Iordanis.Sidiropoulos"])  # print value for a given key
    contacts["Valerio Pizzas"] = 3210  # Create a new item in the dictionary
    print(contacts)  # We can see the new addition of Valerio Pizzas

    print(len(contact_address))  # Prints just the length/number of items
    # included in that list
    del contact_address["info"]  # deletes a value from the dictionary
    print(contact_address)

    print("Mikri.Eleni" in contacts)  # True or false
    address_item1 = contact_address.popitem()  # get the lost item in the list
    print(contact_address)  # The last itm is missing now
    print(address_item1)  # We can print it standalone
    # contact_name, contact_campus = contact_address.popitem()
    # Deletes the last item by separating its values
    print(contact_address)

    print("\n")  # Merging dictionaries |
    class_group1 = {"Pat": 12345, "Iordanis": 66666}
    class_group2 = {"Antonella": 67777, "Mikri": 20012}
    full_class = class_group1 | class_group2  # oly in new 3.9 Python update
    print(full_class)

    # Example using update |=
    full_class |= {"Jim Staxtos": 88888}  # Updates - new value in
    full_class |= {"Pat": 11001}  # Updates - changing ID
    print(full_class)

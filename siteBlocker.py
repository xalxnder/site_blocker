# Looking to block distracting websites? This script allows users to add or remove sites from their host file.
# Author: Xavier Alexander
# Import regex module
import re

# Elevate privelages for sudo access.
from elevate import elevate
elevate(graphical=False)

# Figure out if the user wants to add or remove a site from the host file
user_input = input(
    "Would you like to add or remove a site from your host file? ")


# Function to add site from host file.
def add_site():
    # Get input from user.
    user_input_add = input("What site would you like to block?: ")
    # Open host file, and check to see if string is already there.
    with open('/etc/hosts', 'r') as file:
        lines = file.read()
        result = re.search(rf'\b{user_input_add}\b', lines)
        while result:
            file.seek(0)
            user_input_add = input(
                "Site is already being blocked. What site would you like to block?: ")
            result = re.search(rf'\b{user_input_add}\b', lines)
        else:
            with open('/etc/hosts', 'a+') as file:
                file.write(
                    f"\n127.0.0.1\t{user_input_add}.com\n127.0.0.1\twww.{user_input_add}.com\n127.0.0.1\thttps://www.{user_input_add}.com")

# Function to remove site from host file.


def remove_site():
    user_input_remove = input("What site would you like to remove? ")
    with open('/etc/hosts', 'r+') as file:
        new_output = []
        # pattern = re.compile(r'\bworldstar\b')
        lines = file.readlines()
        for i in lines:
            new_output.append(i)
            if user_input_remove in i:
                new_output.remove(i)
            print(i)
        file.seek(0)
        file.writelines(new_output)
        file.truncate()
    with open('/etc/hosts', 'r') as file:
        print(file.read())


if user_input == 'add':
    add_site()
elif user_input == 'remove':
    remove_site()
else:
    print('You did not make an approptiate choice. Exiting..')

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

site_name = input("What is the name of the site ")


class SiteBlocker:
    """ A model for our site blocker program """

    def __init__(self):
        self.user_input = user_input

# Function to add site from host file.
    def add(self):
        # Open host file, and check to see if string is already there.
        with open('/etc/hosts', 'r') as file:
            lines = file.read()
            # Checking to find anything that matches site_name
            result = re.search(rf'\b{site_name}\b', lines)
            while result:
                # Set Reference point to beginning of file
                file.seek(0)
                used_site_name = input(
                    "Site is already being blocked. What site would you like to block?: ")
                result = re.search(rf'\b{used_site_name}\b', lines)
            else:
                with open('/etc/hosts', 'a+') as file:
                    file.write(
                        f"\n127.0.0.1\t{site_name}.com\n127.0.0.1\twww.{site_name}.com\n127.0.0.1\thttps://www.{site_name}.com")

    # Function to remove site from host file.
    def remove(self):
        with open('/etc/hosts', 'r+') as file:
            new_output = []
            # pattern = re.compile(r'\bworldstar\b')
            lines = file.readlines()
            for i in lines:
                new_output.append(i)
                if site_name in i:
                    new_output.remove(i)
                print(i)
            file.seek(0)
            file.writelines(new_output)
            file.truncate()
        with open('/etc/hosts', 'r') as file:
            print(file.read())


site_blocker = SiteBlocker()

if user_input == 'add':
    site_blocker.add()
elif user_input == 'remove':
    site_blocker.remove()
else:
    print('You did not make an approptiate choice. Exiting..')

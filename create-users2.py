#!/usr/bin/python3
# INET4031
# Aisha Salad
# 3/25/25

import os       # Used to run operating system commands
import re       # Used for regular expressions to match lines
import sys      # Used to read lines from st

# Function to read the user file and create accounts
def process_user_file(filename, dry_run):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # Remove extra spaces and newlines

            if not line or line.startswith('#'):
                # Skip empty lines or lines that start with #
                if dry_run:
                    print(f"Skipping line: {line}")
                continue  

            fields = line.split(':')  # Split the line into parts

            if len(fields) != 5:
                # If there aren't exactly 5 parts, it's an error
                if dry_run:
                    print(f"Error: Line does not have enough fields - {line}")
                continue  

            # Get the user's details
            username = fields[0]  
            password = fields[1]  
            fullname = f"{fields[3]} {fields[2]},,,"  # First name, last name, formatted for Linux
            groups = fields[4].split(',')  # Groups are separated by commas

            # Command to create the user account
            command = f"sudo useradd -m -c \"{fullname}\" {username}"
            if dry_run:
                print(f"Dry-run: Would create user: {username}")
            else:
                os.system(command)
                print(f"User {username} created.")

            # Command to set the user's password
            password_command = f"echo \"{username}:{password}\" | sudo chpasswd"
            if dry_run:
                print(f"Dry-run: Would set password for {username}")
            else:
                os.system(password_command)
                print(f"Password set for {username}.")

            # Add user to groups if any are listed
            for group in groups:
                if group != "-":  # "-" means no group
                    group_command = f"sudo usermod -aG {group} {username}"
                    if dry_run:
                        print(f"Dry-run: Would add {username} to group {group}")
                    else:
                        os.system(group_command)
                        print(f"{username} added to group {group}.")

# Ask if the user wants to do a test run or actually create accounts
if __name__ == "__main__":
    dry_run_input = input("Run in dry-run mode? (Y/N): ").strip().upper()
    dry_run = dry_run_input == 'Y'
    process_user_file("create-users.input", dry_run)






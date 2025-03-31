#!/usr/bin/python3

# INET4031
# Aisha Salad
# 3/25/25
# 3/25/25
# Used to run operating system commands, Used for regular expressions to match lines
import os
import re
import sys


def main():
    for line in sys.stdin:
	# Skip lines that start with '#' (these are comments in the input file)
        match = re.match("^#",line)

        # Split the line into parts using ':' as a separator
        fields = line.strip().split(':')

	# If the line is a comment or doesn't have exactly 5 parts, skip it
        if match or len(fields) != 5:
            continue
	# Get user details from the line, The username, The password, Stores user info 
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # Get the groups the user should be added to
        groups = fields[4].split(',')

	# Create a new user account
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
	# Run the command to add the user
        #print cmd
        os.system(cmd)
	
	 # Set the password for the new user
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        
	# Run the command to set the password
        #print cmd
        os.system(cmd)

        for group in groups:
	# Adding the user  to groups
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()

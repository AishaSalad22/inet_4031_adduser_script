# inet_4031_adduser_script
Program Description
 - This script makes adding users to a Linux system easier by doing the work for you. Instead of typing multiple commands for each user, the script reads user details from a file and runs the necessary system commands automatically.

How Users Are Normally Added 
  - If you were to add users manually.
  - Create the user account 
  - Set the user's password
  - Add the user to a group

Input file format
 - username - The login name the user will use.
 - password - The user's password.
 - last_name - The user's last name.
 - first_name - The user's first name.
 - Group
 - Any line that starts with # is ignored.

Running the Script
   - chmod a+x create-users.py
   - ./create-users.py < create-users.input
   - This tells the script to read the create-users.input file and create users based on the information inside.


Dry Run Mode
   - commonted out the "os.cmd()"
  - The script will print the commands it would run, but it won’t actually create any users or modify anything. This helps you check for mistakes before applying changes.






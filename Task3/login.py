import os
import getpass

def login():
    #Taking input
    user=input("Enter User:")
    password=getpass.getpass("Enter Password:")

# Specify the file path
    file_path = r"C:\Users\user\Pictures\Task3\passwd.txt"

    try:
        with open(file_path, 'r') as passwd:
            
            # Check if the entered username and password match any user entry
            for line in passwd:
                 if line.count(':') >= 2:
                     stored_username, _, stored_password = line.strip().split(':')
                     if user == stored_username and password == stored_password:
                         print("Access granted.")
                         return

        # If the loop completes without finding a match, deny access
        print("Access denied.")
    
    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    login()
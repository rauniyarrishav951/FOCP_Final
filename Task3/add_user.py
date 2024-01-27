import os

# Prompt the user for input
new_username = input("Enter new username: ")
real_name = input("Enter real name: ")
password = input("Enter password: ")

# Specify the file path
file_path = r"C:\Users\user\Pictures\Task3\passwd.txt"

try:

    existing = set()
    with open(file_path, 'r') as passwd:
        for line in passwd:
            username = line.split(':')[0]
            existing.add(username)

    # Check if the new username already exists
    if new_username in existing:
        print(" This Username is already there. Can You please choose a different username.")
    else:
         
        # Create a new user entry
         new_user_entry = f"{new_username}:{real_name}:{password}\n"

        # Append the new user entry to the file
    with open(file_path, 'a') as passwd:
      passwd.write(new_user_entry)

    print("User Created.")
except FileNotFoundError:
    print(f'Cannot open "{file_path}"!')
except Exception as e:
    print(f'An error occurred: {e}')














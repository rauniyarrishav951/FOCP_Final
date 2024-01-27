
def delete():

    #Taking input
    user=input("Enter User:")

     #Provide the sprcified path
    file_path = r"C:\Users\user\Pictures\Task3\passwd.txt"

    # Open the file in read mode to check for the user
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Flag to check if the user was found
    user_found = True

    # Open the file in write mode to update without the user
    with open(file_path, 'w') as file:
        for line in lines:
            # Assuming each line contains username and other data, separated by a delimiter (e.g., comma)
            current_username = line.split(',')[0].strip()

            if current_username == user:
                user_found = True
            else:
                file.write(line)

    # Display a message based on whether the user was found or not
    if user_found:
        print(f"User '{user}' removed successfully.")
    else:
        print(f"User '{user}' not found. Nothing was changed.")

delete()

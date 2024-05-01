# Script that it executes some operations on a file

import os

menu = """
    1. Create a file and populate it
    2. Append text at the end of the file
    3. Read the file
    4. Remove the file
"""

print(menu)
choice = input("\nWhich option do you choice? ")

if choice == "":
    print("Warning!! You must put at least an option!")
else:
    fileName = input("\nType the file name: ")

    if fileName == "":
        print("Warning!! You must put also a file!")
    else:    
        if choice == "1":
            content = input("\nType the content that you want insert in the file: ")

            with open(fileName, "w") as file:
                file.write(content)
            
            print("The content has been inserted!")
        elif choice == "2":
            if os.path.exists(fileName) == True:
                content = input("\nType the content that you want append to the file: ")

                with open(fileName, "a") as file:
                    file.write("\n" + content)

                print("The content has been added!")
            else:
                print("Warning!! The file '" + str(fileName) + "' doesn't exist yet!")
        elif choice == "3":
            if os.path.exists(fileName) == True:
                with open(fileName, "r") as file:
                    content = file.read()
                    print("\n" + str(content))
            else:
                print("Warning!! The file '" + str(fileName) + "' doesn't exist yet!")
        elif choice == "4":
            if os.path.exists(fileName) == True:
                os.remove(fileName)
                print("The file has been removed!")
            else:
                print("Warning!! The file '" + str(fileName) + "' doesn't exist yet!")
        else:
            print("Warning!! This option isn't recognized by this program!")
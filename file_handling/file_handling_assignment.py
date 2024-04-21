# This file was created to practice file handling methods write, read, append, open, close e.t.c

try:
    # File Creation:
    with open("my_file.txt", "w") as myfile:
        myfile.write("This is a text file\nIt is located in this folder\nThe folder is located in Room 103")

    # File Reading and Display:
    with open("my_file.txt", "r") as myfile:
        read_myfile = myfile.read()
    print(read_myfile)

    # File Appending:
    with open("my_file.txt", "a") as append_file:
        append_file.write("\nAn additional statement1 is added\nAnother new line 2\nThe file will be finally closed")
    
except (FileNotFoundError, PermissionError) as e:
    # Exceptions
    print("Check if the file is present and check it has required permissions")

finally:
    # Print all file content
    myfile = open("my_file.txt", "r")
    print("------> " + "File Content After append:")
    print(myfile.read())
    myfile.close()
# Python File Open
'''
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:
1. "r" - Read - Default value. Opens a file for reading, error if the file does not exist
2. "a" - Append - Opens a file for appending, creates the file if it does not exist
3. "w" - Write - Opens a file for writing, creates the file if it does not exist
4. "x" - Create - Creates the specified file, returns an error if the file exists
'''

f = open("demo_file.txt") # For reading
print(f.read())
f.close()

f = open("write_file.txt", "w") # For Writing


# Python file Writing
f = open("demo_file.txt", "a")
f.write("Now the file have more content.")
f.close()

# Python Create a new file
f = open("my_file.txt", "x")
f.write("Hello World")
f.close()


# Python Delete File
import os 
os.remove("demo_file.txt") 

if os.path.exists("demo_file.txt"):
  os.remove("demo_file.txt")
else:
  print("File is not exists")

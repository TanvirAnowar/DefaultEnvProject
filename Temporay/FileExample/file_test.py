# This script reads the content of 'content.txt' and prints it to the console.

def read_file(file_path):

        with open(file_path, 'r') as file:
            content = file.read()
            print(content)

# read_file('content.txt')

def append_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(f'\n{content}')
        
# append_file('content.txt', '6 This is the appended content')
# read_file('content.txt')

def write_line_in_file(file_path, content):
    with open(file_path, 'a') as file:
        file.writelines(content)
        
# write_line_in_file('content.txt', ['9 This is the appended content \n','8 This is the appended content \n'])
# read_file('content.txt')

#? File path
import os

print(os.getcwd())
print(os.path.abspath('content.txt'))





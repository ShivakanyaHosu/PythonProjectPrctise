import os

print(os.getcwd())  # returns the current working directory

# list files in the current directory

files = os.listdir('.')
print(f"files in the current directory: {files}")

files1 = os.listdir('/Users/')
print(f"files in the current directory: {files1}")

# os.mkdir('test1')# create new directory

file_exist = os.path.exists('test1')
print(file_exist)

print(os.name)  # posix(mac) nt(windows)

# os.rmdir('test1') # remove directory
try:
    full_path_directory = os.getcwd() + "/example.txt"
    print(full_path_directory)

    file = open(full_path_directory)
except Exception as e:
    print(e)

finally:
    print("this code will be executed anyhow")

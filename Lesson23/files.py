# r = Read
# a = Append
# w = Write
# x = Create

import os

# Read - error if it doesn't exist
f = open('names.txt')

# print(f.read()) # Read entire file at once
# print(f.read(4)) # Read first 4 characters of the file
# print(f.readline())  # Read entire line at once
# print(f.readline())  # Read entire line at once

for line in f:
    print(line)

f.close()


try:
    f = open('does_not_exist_file.txt')
    print(f.read())
except:
    print('Error occur while reading the file, File might not exist')
finally:
    f.close()


# Append - creates the file if it doesn't exist
f = open("names.txt", "a")
f.write("\nNeil")
f.close()


f = open("names.txt")
print(f.read())
f.close()


# Write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()


# Two ways to create a new file

# 1.Opens a file for writing, creates the file if it does not exist
f = open('new_file.txt','w')
f.write('Newly created file with approach one')
f.close()

# 2.Creates the specified file, but returns an error if the file exists
if not os.path.exists('dave.txt'):
    f = open('dave.txt','x')
    f.write('something')
    f.close()


# Delete a file

# avoid an error if it doesn't exist
if os.path.exists('dave.txt'):
    os.remove('dave.txt')
else:
    print('The file you wish to delete does not exist')

# with has built-in implicit exception handling
# close() will be automatically called
with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
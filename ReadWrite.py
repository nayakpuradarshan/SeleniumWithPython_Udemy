
file = open('test.txt')

# read contect of the file
# print(file.read())

# read one single line
# print(file.readline())


# print line by line using readline

"""
line = file.readline()
while line!="":
    print(line)
    line = file.readline()
"""

values = ["abc", "bcdd", "cat", "dog", "elephant"]
for line in file.readline():
    print(line)

file.close()

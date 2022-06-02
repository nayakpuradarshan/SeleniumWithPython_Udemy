
"""
# first way of reading the file
file = open('test.txt')
file.close()
"""

# read the file and store all the lines in list and revest lis

# ssecond way of reading the file
with open('test.txt', 'r') as reader:
    content = reader.readline()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)



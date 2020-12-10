# File Objects

# Reading from a file
with open('file.txt', 'r') as f:  # r -> read
    print(f'File name : {f.name}')
    print(f'File mode : {f.mode}')
    # contents = f.read()  # dumps all the contents
    # print(contents)
    # f.readline() reads one line at a time
    lines = f.readlines()  # returns the lines of the file as a list. if used after f.read() it returns an empty list.
    print(f'Total Lines: {len(lines)}')
    for line in lines:  # can also directly used for line in f
        print(line.lstrip(), end='')  # to prevent the extra new line character, pass '' in the end delimiter

# Reading the file in chunks
with open('file.txt') as f2:
    chunk_size = 5
    contents = f2.read(chunk_size)
    f2.seek(5)  # start reading form the 5th character
    while len(contents) > 0:
        print(contents, end=f'*')
        contents = f2.read(chunk_size)  # start from the next chunk.

# Writing to a file
with open('newfile.txt', 'w') as f3:
    f3.write('f')
    # f.seek(num) can be used to write / overwrite



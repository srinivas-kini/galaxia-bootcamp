import time


def make_file_copy(file_to_copy):
    f_contents = ''
    with open(file_to_copy, 'r') as orig_file:
        f_contents = orig_file.read()  # dump the contents

    with open(f'copy_of_{file_to_copy.replace(".txt", "")}.txt {time.time()}', 'w') as copy:
        copy.write(f_contents)  # write the contents into new file


if __name__ == '__main__':
    make_file_copy('file.txt')

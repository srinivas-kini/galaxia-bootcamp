import os


# Print the directory structure, given the root file path
def print_dir_tree(root):
    for dirs in os.listdir(root):
        file_path = os.path.join(root, dirs)
        if os.path.isfile(file_path):
            print(file_path)
        else:
            print_dir_tree(file_path)

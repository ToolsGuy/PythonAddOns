# This python script has several methods for Copy operation

import os
import shutil

# Copy a file or directory from source to destination
def copy_with_output(source, destination, *, follow_symlinks=True):
    if not os.path.exists(os.path.dirname(destination)):
        os.makedirs(destination)
    print('  Copy ' + source)
    print('    to ' + destination)
    shutil.copy2(source, destination)


# Walk through a folder tree and copy files from source to destination.
#   source          absolute path where the files and directories are copied from
#   destination     absolute path where the files and directories are copied to
def copytree(source, destination):
    for source_dir, dirs, files in os.walk(source):
        dest_dir = source_dir.replace(source, destination)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        for file in files:
            source_file = os.path.join(source_dir, file)
            dest_file = os.path.join(dest_dir, file)
            copy_with_output(source_file, dest_file)

# This method copies directories and files from source to destination and ignores files and directories according to the pattern
# given by ignore_patterns
def copytree_with_ignore(source, destination, *ignore_patterns):
    shutil.copytree(source, destination, ignore=shutil.ignore_patterns(*ignore_patterns), copy_function=copy_with_output)
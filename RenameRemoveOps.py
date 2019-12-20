import os
import fnmatch
import shutil

# Remove folder and all its subfolders, then create the folder again
def cleanup_dir(folder):
    if os.path.exists(folder):
        print('Cleanup folder {}'.format(folder))
        shutil.rmtree(folder, ignore_errors=False)

    print('Create new folder {}'.format(folder))
    os.makedirs(folder)

# Rename a directory or file
def rename(source, destination):
    print('  Rename ' + source)
    print('      to ' + destination)
    os.rename(source, destination)

# Recursively remove set of files.
#   target_dir: Absolute directory from which files need to be removed, e.g. D:/Sources/
#   file_list:  provide a common seperated values with regex patterns matching file names, e.g. ['*.Doc*', '*proj*']
def remove_files(target_dir, file_list):
    for rootDir, subdirs, filenames in os.walk(target_dir):
        for oneFilepattern in file_list:
            for filename in fnmatch.filter(filenames, oneFilepattern):
                try:
                    os.remove(os.path.join(rootDir, filename))
                    print('Deleting file -'+ os.path.join(rootDir, filename))
                except OSError:
                    print("Error while deleting file")
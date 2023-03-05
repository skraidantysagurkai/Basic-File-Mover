import os

'''
    Note: Some os functions work only on Unix or Windows OS.
    This script should work for both OSs, however if any problems arise please consult os documentation
    https://docs.python.org/3/library/os.html
'''

# Parameters that can be changed
ExtensionLocation = {
    'jpg': 'JPG Files',
    'jpeg': 'JPEG Files',
    'png': 'PNG Files',
    'HEIC': 'HEIC Files',
    'pdf': 'PDF Files',
    'xlsx': 'Excel Files',
    'doc': 'Word Files',
    'pptx': 'PowerPoint Files'
}

path_from = '/Users/rokassabaitis/Downloads'
path_to = '/Users/rokassabaitis/Documents'


def checkdir():
    for value in ExtensionLocation.values():
        if value not in os.listdir(path_to):  # Making directories if they don't exist
            os.mkdir(path_to + '/' + value)


def movefiles():
    for key in ExtensionLocation.keys():
        for file in os.listdir(path_from):
            if '.dmg' in file.lower():  # Removing unused .dmg files
                removefiles(file)
                continue
            elif f'.{key}' not in file.lower():  # Checking if a file isn't .something
                continue

            oldpath = path_from + '/' + file
            newpath = path_to + '/' + ExtensionLocation[key] + '/' + file
            os.rename(oldpath, newpath)


def removefiles(file):
    os.remove(path_from + '/' + file)


checkdir()
movefiles()

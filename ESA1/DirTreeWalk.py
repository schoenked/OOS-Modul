#!/usr/bin/env python3.7

# IMPORTS
import hashlib
import os
import sys

# FUNCTIONS
def walkTree(path, level=0):
    if path.endswith('\\'):
        path = path[:-1]
    
    try:
        list=os.listdir(path)
    except FileNotFoundError as err:
        print(err.strerror)  
        quit()

    for elem in list:
        elemPath=path + "\\" + elem
        #hashing 
        try:
            md5=hashlib.md5()
            with open(elemPath, 'rb') as f:
                while True:
                    data = f.read(65536)
                    if not data:
                        break
                    md5.update(data)
            print('{}{}\t{}\t{}'.format(level*"  ", elem.ljust(16), elemPath, md5.hexdigest()))
        except IOError as e:
            print('{}{}\t{}'.format(level*"  ", elem.ljust(16), elemPath, elem))
            walkTree(elemPath, level + 1)
                           
def help():
    print('''
usage: DirTreeWalk.py [-h] path



positional argument:

  path        path to show



optional arguments:

  -h, --help  show this help message and exit
    ''')

# MAIN
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if (sys.argv[1] == '-h'):
            help()
            quit()
        walkTree(sys.argv[1])
    else:
        help()

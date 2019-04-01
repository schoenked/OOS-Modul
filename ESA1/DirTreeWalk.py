#!/usr/bin/env python3.7

# IMPORTS
import hashlib
import os

# FUNCTIONS
def walkTree(path, level=0):
    if path.endswith('\\'):
        path = path[:-1]

    list=os.listdir(path)
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
                    

# MAIN
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(sys.argv[1])
        walkTree(sys.argv[1])

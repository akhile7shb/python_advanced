from os import read, remove
from re import search

# 1.file read
# 2.file write
# 3.file append
# 4.file search
# 5.file remove
# 6.exit
def file_read():
    file_name=input('enter the file name')
    f=open(file_name,'r')
    content=f.read()
    print(content)

def file_write():
    name=input('enter the file name')
    f=open(name,'w')
    content=input('enter the content for write')
    f.write(content)

def file_append():
    name=input('enter the file name')
    f=open(name,'a')
    content=input('enter the content for append')
    f.write(content)

def file_search():
    name=input('enter the file name')
    f=open(name,'r')
    content=f.read()
    c=input('enter the word')
    if c in content:
        print('present')
    else:
        print('not present')

def file_remove():
    import os
    name=input('enter the file name')
    os.remove(name)
while(1):
    print('file driven file operation')
    print('1.file read')
    print('2.file write')
    print('3.file append')
    print('4.file search')
    print('5.file remove')
    print('6.exit')

    ch=int(input('enter the choice'))

    if ch==1:
        file_read()
    elif ch==2:
        file_write()
    elif ch==3:
        file_append()
    elif ch==4:
        file_search()
    elif ch==5:
        file_remove()


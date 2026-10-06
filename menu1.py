# while(1):
#     print('1.option1')
#     print('2.option2')
#     print('3.exit')
#
#     ch=int(input('enter your choice'))
#     if ch==1:
#         print('hello')
#
#     elif ch==2:
#         print('hi')
#
#     else:
#         exit()


# 1.file read
# 2.file write
# 3.file append
# 4.file search
# 5.file remove
# 6.exit

def file_read():
    file_name=input('enter filename')
    f=open(file_name,'r')
    content=f.read()
    print(content)
def file_write():
    file_name=input('enter filename')
    f=open(file_name,'w')
    content=input('enter the content')
    f.write(content)
def file_append():
    file_name=input('enter filename')
    f=open(file_name,'a')
    content=input('enter filename')
    print(content)
def file_search():
    file_name=input('enter filename')
    f=open(file_name,'r')
    content=f.read()
    word=input('enter the word to be searched')
    if word in content:
        print('word found')
    else:
        print('not found')
def file_remove():
    import os
    file_name=input('enter filenmae')
    os.remove(file_name)
    print('file',file_name,'is deleted')

while(1):
    print('menu driven-file operation')
    print('1.file read')
    print('2.file write')
    print('3.file append')
    print('4.file search')
    print('5.file remove')
    print('6.exit')

    ch=int(input('enter your choice'))

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
    else:
         exit()



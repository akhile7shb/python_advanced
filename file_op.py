from os.path import split

f=open('mark.txt','r')
s=f.readlines()
print(s)
f1=open('names.txt','r')
for i in s:
    l=i.split()
    print(l)
    if(int(l[1]>75)):
        f.write(l[0]+'\n')
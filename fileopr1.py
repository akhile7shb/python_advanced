# f=open('a.txt','r')
# #read
# # content=f.read()
# content=f.readlines()
# print(content)
from file_read import content

#1write a program to read a text file and displays the number of lines in a file

# f=open('a.txt','r')
# # content=f.read()
# content=f.readlines()
# print(len(content))


#write a program to display the number of words in a file

# f=open('a.txt','r')
# s=f.read()
# print(s.split())

#write a program to update the second line in a file
#
# f=open('a.txt','r')
# # content=f.read()
# content=f.readlines()
# content[1]='dbms\n'
# f.close()
# f=open('a.txt','w')
# f.writelines(content)
# f.close()


#write a program to display the last 5 lines in a file

# f=open('a.txt','r')
# content=f.readlines()
# print(content[-3:])


#program to search a particular word in a file
#
# f=open('a.txt','r')
# content=f.read()
# if ('python' in content):
#     print('found')
# else:
#     print('not found')


#reverse the line in a content

# f=open('a.txt','r')
# content=f.readlines()
# rev=content[::-1]
# f=open('a.txt','w')
# f.writelines(rev)


# #find the number of letters,digits,and spaces in a file
#
# f=open("k.txt","r")
# content=f.read()
#
# lcount=0
# dcount=0
# scount=0
#
#
#
# for i in content:
#     if(i.isalpha()):
#         lcount+=1
#     elif(i.isdigit()):
#         dcount+=1
#
#     elif(i.isspace()):
#         scount+=1
#     else:
#         pass
#
# print("Number of letters",lcount)
# print("Number of digits",dcount)
# print("Number of spaces",scount)

#reverse the lines in a

# f=open("k.txt","r")
# content=f.readlines()
#
# rev=content[::-1]
# f=open("k.txt","w")
# f.writelines(rev)



# A file totalstudents.txt contains the names of all students in a class,
# and a file passedstudents.txt contains the names of students who passed.txt the exam.
# Write a Python program to:
# Read the names from both files.
# # Find the students who did not pass.
# # Write their names to a new file named failedstudents.txt, one name per line.
# #
# f1=open('total.txt',"r")
#
# l1=f1.readlines()
# print(l1)
# f2=open("passed_students.txt","r")
# l2=f2.readlines()
# print(l2)
# f3=open("failed_students.txt","w")
#
# for i in l1:
#     if i not in l2:
#
#         f3.write(i)
#
# #
#
# # Two files, swiggy.txt and zomato.txt.txt, contain the names of food items ordered from each platform.
# # Write a Python program to read words from swiggy.txt and zomato.txt.txt, combine them, and count how many times each word appears. Store the result in a dictionary and print it
#
# f1=open('zomato.txt',"r")
# s1=f1.read().split()
# print(s1)
# #
# #
# f2=open('swiggy.txt',"r")
# s2=f2.read().split()
# print(s2)
# #
# #
# items=s1+s2
# print(items)
#
# d={}
#
# for i in items:
#     d[i]=items.count(i)
#
# print(d)
#
#



# A file marks.txt contains the names and marks of students as shown below:
# Anu 80
# Rahul 65
# Meera 90
# Arun 70
# Write a Python program to read the file and write the names of students who scored more than 75 marks into a file named names.txt.


# f=open("mark.txt","r")
#
# s=f.readlines()
# print(s)
# f3=open('names.txt','w')
# for i in s:
#     #print(l)
#     l=i.split()
#     if(int(l[1])>75):
#         f.write(l[0]+'\n')

f=open('k.txt','a')
f.write('python')
f=open('total_students.txt','w')

students_list=['aadhil\n','akhilesh\n','snehal\n','ajith uncle\n','vinayak\n','sachin\n']
f.writelines(students_list)

u=open('passed_students.txt','w')
passed_students=['aadhila\n','akhilesh\n','snehal\n']
u.writelines(passed_students)

i=open('failed_students.txt','w')
failed_students=['ajith\n']
i.writelines(failed_students)

q=open('swiggy.txt','w')
swiggy_foods=['chicken biryani\n','shawai\n','mandhi\n','shawarma\n']
q.writelines(swiggy_foods)
z=open('zomato.txt','w')
zomato_foods=['chicken biryani\n','mandhi\n','fried rice\n','chicken biryani\n','chicken biryani\n','mandhi\n']
z.writelines(zomato_foods)

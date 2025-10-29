score= float(input("enter your marks"))#takes input value from user
grade=""
if(score>=90 and score<=100):#first grade to be optimised
   grade ="A"
   print("your grade is A")
elif(score<= 89 and score>=75):#second grade to optimimsed
    grade = "B"
    print("your grade is B")
elif(score<=74 and score>=50):#third grade to be optimised
    grade = "C"
    print("your grade is C")#fourth grade to be optimised
elif(score<=50):
    grade = "fail"
    print("fail")
else:#eror value handlling
    print("invalid input")

name= str(input("enter your name"))
print("hello", name, "your grade is-", grade)#gives output nwith name and grade

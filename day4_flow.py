score= float(input("enter your marks"))
grade=""
if(score>=90 and score<=100):
   grade ="A"
   print("your grade is A")
elif(score<= 89 and score>=75):
    grade = "B"
    print("your grade is B")
elif(score<=74 and score>=50):
    grade = "C"
    print("your grade is C")
elif(score<=50):
    grade = "fail"
    print("fail")
else:
    print("invalid input")

name= str(input("enter your name"))
print("hello", name, "your grade is-", grade)
name=input("enter your name")
age=input("enter your age")
score=float(input("enter your score"))
grade=""
if(score>=90 and score<=100):
    grade="A"
    print("A")
elif(score>=75 and score<=89):
    grade="B"
    print("B")
elif(score>=50 and score<=74):
    grade="C"
    print("C")
else:
    grade="fail"
    print("your grade will be", grade)

nums=[1, 2, 3, 4 , 5]
for val in range(1, 5):
    print(val, "->", val**2)

k = 1
while k <= 10:
    print("i will be consistent")
    k+=1

user ={
    "name": name,
    "age" : age,
    "grade": grade,
}
print(user)

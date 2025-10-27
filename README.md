#this section is about list and tuples 
num = []#empty list created
num1= input("enter 1st num")
num2= input("enter 2nd num")
num3= input("enter 3rd num")
num4= input("enter 4th num")
num5= input("enter 5th num")#5 user input taken
num.append(num1)
num.append(num2)
num.append(num3)
num.append(num4)
num.append(num5)#5inputs added to the empty list
print(num)

print(num[0])
print(num[4])#print for the first and last element of list

total= sum(num)
print(total)#total sum of all elements

num.sort()
print(num)#sorts the list in ascending order(not told by you what order so i chose ascending)

tup = tuple(num)
print(type(tup))#changes list into tuple

#tjis section is about dictionary
dict= {
   "name": str(input("enter your name")),
   "age": int(input("enter your age")),
   "city": str(input("enter your city")),
}
print(dict)#dictonory created and input taken from user

#this section is about if else logic
age= int(input("enter your age: "))#user input for age

if(age<=18):
    print("minor")#command to check
elif(age>= 18 and age<=59):
    print("adult")#command to check if 1st command isnt true
elif(age>=60):
    print("senior citizen")#ommand to check if 2nd command isnt true
25/10/25
"Day1- complete - python enviorment ready"
I'll surely do it!!!

26/10/25
"day2- complete - "learned about interactive shell(REPL) anad how it differs from running scripts directly 
im on it!!!!

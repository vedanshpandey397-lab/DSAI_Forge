def calc_avg(a, b, c):
    avg = (a+b+c)/3
    return avg

def get_grade(avg):
    if avg>=90:
        return "A"
    elif avg>=75:
        return "B"
    elif avg>=50:
        return "C"
    else:
        return "fail"
    
name = input('enter your name: ')
a = float(input("enter 1st marks: "))
b = float(input("enter 2nd marks: "))
c = float(input("enter 3rd marks: "))

average = calc_avg(a, b, c)
grade = get_grade(average)

print("student", name)
print("average", average)
print("grades", grade)
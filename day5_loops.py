# day5_loops.py

# For loop example: print numbers 1–10 and their squares
for val in range(1, 11):
    print("Number:", val, "| Square:", val ** 2)

# While loop example: multiplication table
i = 1
num = int(input("\nEnter a number: "))
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

# Punishment loop 😅
k = 1
while k <= 10:
    print("I will not skip my daily forge again!")
    k += 1
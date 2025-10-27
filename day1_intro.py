user_info= {
   "name": str(input("enter your name")),
   "age": int(input("enter your age")),
   "city": str(input("enter your city")),
}

for key, value in user_info.items():
    print(f"{key}:{value}")#dictonory created and input taken from user

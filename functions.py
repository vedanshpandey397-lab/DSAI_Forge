movies= []
for i in range(1,6):
    movie = input(f"enter a movie name {i}:")
    movies.append(movie)

def show_movies(movie_list):
    num = 1
    for items in movie_list:
        print(num, ".", items)
        num +=1

show_movies(movies)

choice = input("do you want to add more movies? reply with y/n")

if choice == "y":
    name = input("enter a movie: ")
    movies.append(name)
    show_movies(movies)

elif choice == 'n':
    print("goodbye")

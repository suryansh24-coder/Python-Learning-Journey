movie1 = input("Enter your 1st favourite movie : ")
movie2 = input("Enter your 2nd favourite movie : ")
movie3 = input("Enter your 3rd favourite movie : ")
lis = [movie1,movie2 , movie3]
print(lis)
print(type(lis))
# using methode 2 :-
movies = []
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)
# Using 3rd methode :-
movies.append(input("Enter your 1st favourite movie : "))
movies.append(input("Enter your 2nd favourite movie : "))
movies.append(input("Enter your 3rd favourite movie : "))
print(movies)



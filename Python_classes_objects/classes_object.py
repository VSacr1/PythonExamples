class Movies: 
    genre = "Comedy"

    time = "2 hours"

    def isfilmgood(self): 
        print("True")

shrek = Movies()
bee_Movie = Movies()

bee_Movie.time = 1.3

print(bee_Movie.time)

print(shrek.time)
print(shrek.genre)
shrek.isfilmgood()

bee_Movie.isfilmgood()
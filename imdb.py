import requests
from bs4 import BeautifulSoup

#This program uses imdb top 250 to pick the best movie to watch. The cart used can be changed by changing the URL.
#Code might not work on other URLs.

URL = "https://www.imdb.com/chart/top/"
page = requests.get(URL)

#Creating BeautifulSoup object using the html code from the website.
soup = BeautifulSoup(page.content, "html.parser")
#We need the element that has "styleguide-v2" as id. This can be seen by inspecting the website.
results = soup.find(id="styleguide-v2")

#We obtain the titles of the movies on the list. The element and the class name can be found by inspecting the html code.
movie_elements = results.find_all("td", class_="titleColumn")
#We do the same for the ratings of the movies.
rating_elements = results.find_all("td", class_="ratingColumn imdbRating")

#We make lists of the data and remove everything that is not needed.
movienames = []
movieratings = []

for movie_element in movie_elements:
    lines = movie_element.find_all("a")
    for line in lines:
        moviename=line.get_text()
        movienames.append(moviename)

for rating_element in rating_elements:
    lines = rating_element.find_all("strong")
    for line in lines:
        movierating=line.get_text()
        movierating = float(movierating)
        movieratings.append(movierating)

#We make a dictionary with the title of the movie being the keyword and the movies rating as the value.

rank = 0
movies = {}
for moviename in movienames:
    movies.update({moviename : movieratings[rank]})
    rank +=1



#We ask the user the movies it is interested in. We check if the movie is in the list.
# Atleast one movie is needed to proceed.

print("Input the movies you are interested in. When you are done, type "+ repr("decide for me")+".")
options = []
i = 1
while True:
    option = input("Option" + str(i)+":" )
    if option == "decide for me":
        if options == []:
            print("You have to enter a valid movie!")
            continue
        break
    elif option in movienames:
        options.append(option)
        i +=1
    else:
        print("Movie not on the list, try again. Check spelling.")


#We make a dictionary using the selected movies and their ratings.

selected_movies = {}

for option in  options:
    selected_movies.update({option : movies[option]})

#We rank the dictionary, best rated movie comes first when we reverse the dictionary.
#Using the sorted function reversing should also be possible, couldn't get it to work.
# List of the keys for dictionary are helpful for accessing the items.

ranking = dict(sorted(selected_movies.items(), key=lambda item: item[1]))
res = dict(reversed(list(ranking.items())))
list_of_keys = list(res.keys())

#We print the results for the user.
print("According to imdb, "+ list_of_keys[0] + " is the best movie, it has received the rating " + str(res[list_of_keys[0]])+ ". \nHere are all the movies ranked:")

for movie in res:
    print(movie+" "+str(res[movie]))
print("Have a nice movie night!")













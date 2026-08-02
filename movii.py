import pandas as pd

movies = pd.read_csv("movies.csv")

movie = input("Enter movie name: ")

selected = movies[movies["title"].str.contains(movie, case=False)]

genre = selected.iloc[0]["genres"]

recommendations = movies[movies["genres"] == genre]

print("\nRecommended Movies:")

for movie in recommendations["title"]:
    print(movie)

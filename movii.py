from flask import Flask, render_template, request
import requests

app = Flask(__name__)

TMDB_API_KEY = "6f6cda2298b50c6b1fe312bc9df90f8e"


def search_movies(movie_name):

    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": TMDB_API_KEY,
        "query": movie_name
    }

    response = requests.get(url, params=params)

    data = response.json()

    movies = []

    for movie in data.get("results", [])[:10]:

        poster = ""

        if movie.get("poster_path"):
            poster = (
                "https://image.tmdb.org/t/p/w500"
                + movie["poster_path"]
            )

        movies.append({
            "title": movie.get("title", "N/A"),
            "rating": movie.get("vote_average", "N/A"),
            "year": movie.get("release_date", "N/A")[:4]
            if movie.get("release_date")
            else "N/A",
            "poster": poster
        })

    return movies


@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    if request.method == "POST":

        movie_name = request.form["movie"]

        recommendations = search_movies(movie_name)

    return render_template(
        "index.html",
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)
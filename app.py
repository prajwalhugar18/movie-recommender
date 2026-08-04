from flask import Flask, render_template, request

from movii import (
    search_movie,
    search_actor,
    search_genre,
    search_year,
    trending_movies,
    top_rated_movies,
    search_language,
    get_trailer,
    get_movie_details,
    get_similar_movies
)
app = Flask(__name__)

genres = {
    "Action": 28,
    "Adventure": 12,
    "Comedy": 35,
    "Crime": 80,
    "Drama": 18,
    "Fantasy": 14,
    "Horror": 27,
    "Romance": 10749,
    "Sci-Fi": 878,
    "Thriller": 53
}
languages = {
    "English": "en",
    "Hindi": "hi",
    "Kannada": "kn",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
    "Korean": "ko",
    "Japanese": "ja"
}

@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    if request.method == "POST":

        search_type = request.form.get("search_type")

        query = request.form.get("query")

        if search_type == "movie":
            recommendations = search_movie(query)

        elif search_type == "actor":
            recommendations = search_actor(query)

        elif search_type == "genre":
            recommendations = search_genre(
                genres.get(query, 28)
            )

        elif search_type == "year":
            recommendations = search_year(query)

    return render_template(
        "index.html",
        recommendations=recommendations
    )
@app.route("/trending")
def trending():

    return render_template(
        "index.html",
        recommendations=trending_movies()
    )


@app.route("/toprated")
def top_rated():

    return render_template(
        "index.html",
        recommendations=top_rated_movies()
    )


@app.route("/language/<lang>",methods=["GET","POST"])
def language(lang):

    return render_template(
        "index.html",
        recommendations=search_language(
            languages.get(lang, "en")
        )
    )
@app.route("/trailer/<int:movie_id>")
def trailer(movie_id):

    return get_trailer(movie_id)
@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):

    details = get_movie_details(movie_id)

    return render_template(
        "details.html",
        movie=details
    )

@app.route("/similar/<int:movie_id>")
def similar(movie_id):

    recommendations = get_similar_movies(
        movie_id
    )

    return render_template(
        "index.html",
        recommendations=recommendations
    )
if __name__ == "__main__":
    app.run(debug=True)
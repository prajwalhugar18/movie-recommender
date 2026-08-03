from flask import Flask, render_template, request
from movii import search_movies

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    if request.method == "POST":

        movie_name = request.form.get("movie")

        recommendations = search_movies(movie_name)

    return render_template(
        "index.html",
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)
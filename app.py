from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

movies = pd.read_csv("movies.csv")

@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    if request.method == "POST":

        movie = request.form["movie"]

        selected = movies[movies["title"].str.contains(movie, case=False)]

        if not selected.empty:

            genre = selected.iloc[0]["genres"]

            recs = movies[movies["genres"] == genre]

            recommendations = recs["title"].head(5).tolist()

    return render_template(
        "index.html",
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)
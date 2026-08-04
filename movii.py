import requests

TMDB_API_KEY = "6f6cda2298b50c6b1fe312bc9df90f8e"


def format_movies(movie_list):

    results = []

    for movie in movie_list[:20]:

        poster = ""

        if movie.get("poster_path"):
            poster = (
                "https://image.tmdb.org/t/p/w500"
                + movie["poster_path"]
            )

        results.append({
            "id": movie.get("id"),
            "title": movie.get("title", "N/A"),
            "rating": movie.get("vote_average", "N/A"),
            "year": movie.get("release_date", "")[:4]
            if movie.get("release_date")
            else "N/A",
            "poster": poster,
            "overview": movie.get(
                "overview",
                "No description available"
            )
        })

    print("Movies found:", len(results))
    return results


def search_movie(movie_name):

    url = "https://api.themoviedb.org/3/search/movie"

    data = requests.get(
        url,
        params={
            "api_key": TMDB_API_KEY,
            "query": movie_name
        }
    ).json()

    return format_movies(data.get("results", []))


def search_actor(actor_name):

    person_url = "https://api.themoviedb.org/3/search/person"

    data = requests.get(
        person_url,
        params={
            "api_key": TMDB_API_KEY,
            "query": actor_name
        }
    ).json()

    if not data.get("results"):
        return []

    actor_id = data["results"][0]["id"]

    credits_url = (
        f"https://api.themoviedb.org/3/person/"
        f"{actor_id}/movie_credits"
    )

    credits = requests.get(
        credits_url,
        params={"api_key": TMDB_API_KEY}
    ).json()

    return format_movies(
        credits.get("cast", [])
    )


def search_genre(genre_id):

    url = "https://api.themoviedb.org/3/discover/movie"

    data = requests.get(
        url,
        params={
            "api_key": TMDB_API_KEY,
            "with_genres": genre_id,
            "sort_by": "popularity.desc"
        }
    ).json()

    return format_movies(
        data.get("results", [])
    )


def search_year(year):

    url = "https://api.themoviedb.org/3/discover/movie"

    data = requests.get(
        url,
        params={
            "api_key": TMDB_API_KEY,
            "primary_release_year": year,
            "sort_by": "popularity.desc"
        }
    ).json()

    return format_movies(
        data.get("results", [])
    )


def trending_movies():

    url = "https://api.themoviedb.org/3/trending/movie/week"

    data = requests.get(
        url,
        params={
            "api_key": TMDB_API_KEY
        }
    ).json()

    return format_movies(
        data.get("results", [])
    )


def top_rated_movies():

    url = "https://api.themoviedb.org/3/movie/top_rated"

    data = requests.get(
        url,
        params={
            "api_key": TMDB_API_KEY
        }
    ).json()

    return format_movies(
        data.get("results", [])
    )


def search_language(language):

    url = "https://api.themoviedb.org/3/discover/movie"

    data = requests.get(
        url,
        params={
            "api_key": TMDB_API_KEY,
            "with_original_language": language
        }
    ).json()

    return format_movies(
        data.get("results", [])
    )


def get_trailer(movie_id):

    url = (
        f"https://api.themoviedb.org/3/movie/"
        f"{movie_id}/videos"
    )

    data = requests.get(
        url,
        params={
            "api_key": TMDB_API_KEY
        }
    ).json()

    for video in data.get("results", []):

        if video.get("site") == "YouTube":

            return (
                "https://www.youtube.com/watch?v="
                + video["key"]
            )

    return ""
def get_similar_movies(movie_id):

    url = (
        f"https://api.themoviedb.org/3/movie/"
        f"{movie_id}/similar"
    )

    data = requests.get(
        url,
        params={"api_key": TMDB_API_KEY}
    ).json()

    return format_movies(
        data.get("results", [])
    )
def get_movie_details(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    data = requests.get(
        url,
        params={"api_key": TMDB_API_KEY}
    ).json()

    return data
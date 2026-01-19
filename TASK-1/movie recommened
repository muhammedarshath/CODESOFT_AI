import pandas as pd
import numpy as np

# Dataset
movies = {
    "Movie": ["Titanic", "Avatar", "Inception", "Interstellar", "The Matrix", "Gladiator", "The Dark Knight", "Forrest Gump", "The Godfather", "Shawshank Redemption"],
    "Genre": ["Romance, Drama", "Action, Adventure, Fantasy", "Action, Sci-Fi", "Sci-Fi, Drama", "Action, Sci-Fi", "Action, Drama", "Action, Crime, Drama", "Drama, Romance", "Crime, Drama", "Drama"]
}

df = pd.DataFrame(movies)
vocab = sorted(set(g for genres in df["Genre"] for g in genres.split(", ")))

def genre_vector(genres):
    g_set = set(genres.split(", "))
    return np.array([1 if g in g_set else 0 for g in vocab])

vectors = np.array([genre_vector(g) for g in df["Genre"]])

def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def recommend(movie_name, n=3):
    if movie_name not in df["Movie"].values:
        return None
    
    idx = df[df["Movie"] == movie_name].index[0]
    target_vec = vectors[idx]
    similarities = [(df["Movie"][i], cosine_similarity(target_vec, vectors[i])) for i in range(len(df)) if i != idx]
    similarities.sort(key=lambda x: x[1], reverse=True)
    return [movie for movie, sim in similarities[:n]]

# User Interface
print("--- Movie Recommendation System ---")
user_input = input("Enter a movie name: ")
result = recommend(user_input)

if result:
    print(f"Recommended for you: {', '.join(result)}")
else:
    print("Movie not found. Please check your spelling.")

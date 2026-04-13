"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from cProfile import label

from src.recommender import load_songs, recommend_songs

def run_profile(label: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    max_score = 5.0 if user_prefs.get("likes_acoustic") else 4.0
    recommendations = recommend_songs(user_prefs, songs, k=k)

    print("\n" + "=" * 40)
    print(f"  {label}")
    print("=" * 40)
    for i, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"\n#{i} {song['title']} by {song['artist']}")
        print(f"   Score : {score:.2f} / {max_score:.2f}")
        print(f"   Why   : {explanation}")
    print()

def main() -> None:
    songs = load_songs("data/songs.csv") 

    profiles = [
        ("Pop / Happy (Default)", {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.80,
            "likes_acoustic": False
        }),
        # ("High-Energy Pop", {
        #     "favorite_genre": "pop",
        #     "favorite_mood": "happy",
        #     "target_energy": 0.90,
        #     "likes_acoustic": False
        # }),
        # ("Chill Lofi", {
        #     "favorite_genre": "lofi",
        #     "favorite_mood": "focused",
        #     "target_energy": 0.40,
        #     "likes_acoustic": False
        # }),
        # ("Deep Intense Rock", {
        #     "favorite_genre": "rock",
        #     "favorite_mood": "intense",
        #     "target_energy": 0.91,
        #     "likes_acoustic": False
        # }),
        # # Edge case: high energy but sad mood
        # ("Conflicted Listener", {
        #     "favorite_genre": "folk",
        #     "favorite_mood": "sad",
        #     "target_energy": 0.90,
        #     "likes_acoustic": True
        # }),
        # # Edge case: genre not in catalog
        # ("Niche Taste", {
        #     "favorite_genre": "metal",
        #     "favorite_mood": "angry",
        #     "target_energy": 0.95,
        #     "likes_acoustic": False
        # }),
    ]

    for label, user_prefs in profiles:
        run_profile(label, user_prefs, songs)

    # Starter example profile
    # user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    # user_prefs = {
    # "favorite_genre": "lofi",
    # "favorite_mood": "focused",
    # "target_energy": 0.40,
    # "likes_acoustic": False
    # }

    # user_prefs = {
    # "favorite_genre": "pop",
    # "favorite_mood": "energetic",
    # "target_energy": 0.90,
    # "likes_acoustic": False
    # }
    
    # user_prefs = {
    # "favorite_genre": "folk",
    # "favorite_mood": "relaxed",
    # "target_energy": 0.30,
    # "likes_acoustic": True
    # }
    
    # user_prefs = {
    # "favorite_genre": "synthwave",
    # "favorite_mood": "moody",
    # "target_energy": 0.70,
    # "likes_acoustic": False
    # }

    # recommendations = recommend_songs(user_prefs, songs, k=5)

    # print("\nTop recommendations:\n")
    # for rec in recommendations:
    #     # You decide the structure of each returned item.
    #     # A common pattern is: (song, score, explanation)
    #     song, score, explanation = rec
    #     print(f"{song['title']} - Score: {score:.2f}")
    #     print(f"Because: {explanation}")
    #     print()

    # print("\n" + "=" * 40)
    # print("  Top Recommendations")
    # print("=" * 40)
    # for i, rec in enumerate(recommendations, start=1):
    #     # You decide the structure of each returned item.
    #     # A common pattern is: (song, score, explanation)
    #     song, score, explanation = rec
    #     print(f"\n#{i} {song['title']} by {song['artist']}")
    #     print(f"   Score : {score:.2f} / 4.50")
    #     print(f"   Why   : {explanation}")
    # print("\n" + "=" * 40)


if __name__ == "__main__":
    main()

from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        """Initializes the Recommender with a list of Song objects."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns the top k songs for a given user profile using weighted scoring."""
        # TODO: Implement recommendation logic
        """Returns the top k songs for a given user profile using weighted scoring."""
        def score(song: Song) -> float:
            total = 0.0
            if song.genre == user.favorite_genre:
                total += 1.0
            if song.mood == user.favorite_mood:
                total += 1.0
            total += 2.0 * (1 - abs(user.target_energy - song.energy))
            if user.likes_acoustic and song.acousticness > 0.6:
                total += 0.5
            return total

        sorted_songs = sorted(self.songs, key=score, reverse=True)
        return sorted_songs[:k]
        ## return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a plain language explanation of why a song was recommended."""
        # TODO: Implement explanation logic
        """Returns a plain language explanation of why a song was recommended."""
        reasons = []
        if song.genre == user.favorite_genre:
            reasons.append(f"genre match ({song.genre})")
        if song.mood == user.favorite_mood:
            reasons.append(f"mood match ({song.mood})")
        energy_proximity = 2.0 * (1 - abs(user.target_energy - song.energy))
        reasons.append(f"energy proximity (+{energy_proximity:.2f})")
        if user.likes_acoustic and song.acousticness > 0.6:
            reasons.append(f"acoustic match ({song.acousticness:.2f})")
        return ", ".join(reasons) if reasons else "general match based on your profile"
        ## return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Returns a (score, reasons) tuple.
    """
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["favorite_genre"]:
        score += 1.0
        reasons.append(f"genre match (+1.0)")

    if song["mood"] == user_prefs["favorite_mood"]:
        score += 1.0
        reasons.append(f"mood match (+1.0)")

    energy_proximity = 2.0 * (1 - abs(user_prefs["target_energy"] - song["energy"]))
    score += energy_proximity
    reasons.append(f"energy proximity (+{energy_proximity:.2f})")

    if user_prefs.get("likes_acoustic") and song["acousticness"] > 0.6:
        score += 0.5
        reasons.append(f"acoustic match (+0.5)")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored.append((song, score, explanation))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
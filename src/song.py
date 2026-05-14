"""This module contains the Song class which represents an individual song."""
from utils import red, rst

red = "\033[91m"
rst = "\033[0m"

class Song:
    """Represents an individual song in the music library."""

    def __init__(self, title, artist, genre, mood, energy_level, favorite=False, play_count=0):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.mood = mood
        self.energy_level = energy_level
        self.favorite = favorite
        self.play_count = play_count

    def display_info(self):
        """Returns a formatted row. All strings are truncated to keep columns perfectly aligned."""
        fav_status = f"{red} ❤︎{rst}" if self.favorite else "  "
        
        disp_title = (self.title[:25] + '..') if len(self.title) > 28 else self.title
        disp_artist = (self.artist[:15] + '..') if len(self.artist) > 18 else self.artist
        disp_genre = (self.genre[:13] + '..') if len(self.genre) > 16 else self.genre
        disp_mood = (self.mood[:7] + '..') if len(self.mood) > 10 else self.mood

        return (f"{fav_status} {disp_title:<28} │ {disp_artist:<18} │ "
                f"{disp_genre:<16} │ {disp_mood:<10} │ "
                f"{self.energy_level:>2}/10  │ {self.play_count:<5}")

    def play_song(self):
        """Simulates playing the song by incrementing the play count."""
        self.play_count += 1

    def toggle_favorite(self):
        """Toggles the favorite status of the song."""
        self.favorite = not self.favorite

    def to_dict(self):
        """Converts the song object to a dictionary for JSON serialization."""
        return {
            "title": self.title,
            "artist": self.artist,
            "genre": self.genre,
            "mood": self.mood,
            "energy_level": self.energy_level,
            "favorite": self.favorite,
            "play_count": self.play_count
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Song object from a dictionary."""
        return cls(
            title=data["title"],
            artist=data["artist"],
            genre=data["genre"],
            mood=data["mood"],
            energy_level=data["energy_level"],
            favorite=data["favorite"],
            play_count=data["play_count"]
        )

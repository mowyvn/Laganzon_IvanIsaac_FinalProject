"""This module handles music library management functions."""
import random
from song import Song
from file_handler import save_data, load_data

class MusicLibrary:
    """Represents the entire music collection and manages all logic."""

    def __init__(self):
        self.songs = []
        self.load_data()

    def add_song(self, new_song):
        """
        Adds a new song only if the title and artist combination is unique.
        Returns True if added, False if duplicate.
        """
        is_duplicate = any(
            s.title.lower() == new_song.title.lower() and 
            s.artist.lower() == new_song.artist.lower() 
            for s in self.songs
        )

        if not is_duplicate:
            self.songs.append(new_song)
            return True
        
        return False

    def remove_song(self, title):
        """Removes a song by title and returns True if successful."""
        song_to_remove = next((s for s in self.songs if s.title.lower() == title.lower()), None)
        if song_to_remove:
            self.songs.remove(song_to_remove)
            return True
        return False

    def display_songs(self, song_list=None):
        """Displays a given list of songs or all songs."""
        target_list = song_list if song_list is not None else self.songs
        if not target_list:
            print("No songs to display.")
            return
        print(f"\n{' ':2} {'TITLE':^28} │ {'ARTIST':^18} │ {'GENRE':^16} │ {'MOOD':^10} │ {'ENERGY'} │ {'PLAYS':^5}")
        print("─" * 102)
        
        for i, song in enumerate(target_list, 1):
            print(song.display_info())

    def search_song(self, keyword):
        """Searches songs by partial keyword match across attributes."""
        keyword = keyword.lower()
        # Using list comprehension for filtering
        results = [
            song for song in self.songs
            if keyword in song.title.lower() or
               keyword in song.artist.lower() or
               keyword in song.genre.lower() or
               keyword in song.mood.lower()
        ]
        return results

    def recommend_songs(self, mood):
        """Returns a random recommendation based on a requested mood."""
        matching_songs = [s for s in self.songs if s.mood.lower() == mood.lower()]
        if matching_songs:
            return random.choice(matching_songs)
        return None

    def sort_songs(self, criteria):
        """Sorts songs based on given criteria using lambda functions."""
        if criteria == 'title':
            self.songs = sorted(self.songs, key=lambda s: s.title.lower())
        elif criteria == 'artist':
            self.songs = sorted(self.songs, key=lambda s: s.artist.lower())
        elif criteria == 'energy':
            self.songs = sorted(self.songs, key=lambda s: s.energy_level, reverse=True)
        elif criteria == 'plays':
            self.songs = sorted(self.songs, key=lambda s: s.play_count, reverse=True)
        elif criteria == 'favorites':
            self.songs = sorted(self.songs, key=lambda s: not s.favorite)

    def calculate_statistics(self):
        """Calculates and returns listening statistics using dictionaries."""
        if not self.songs:
            return None

        most_played = max(self.songs, key=lambda s: s.play_count)
        
        genre_counts = {}
        mood_counts = {}
        total_energy = 0

        for song in self.songs:
            genre_counts[song.genre] = genre_counts.get(song.genre, 0) + 1
            mood_counts[song.mood] = mood_counts.get(song.mood, 0) + 1
            total_energy += song.energy_level

        fav_genre = max(genre_counts, key=genre_counts.get)
        common_mood = max(mood_counts, key=mood_counts.get)
        avg_energy = total_energy / len(self.songs)

        return {
            "total_songs": len(self.songs),
            "total_plays": sum(s.play_count for s in self.songs),
            "most_played": f"{most_played.title} ({most_played.play_count} plays)",
            "favorite_genre": fav_genre,
            "common_mood": common_mood,
            "average_energy": round(avg_energy, 2)
        }

    def save_data(self):
        """Saves the library to a JSON file."""
        data = [song.to_dict() for song in self.songs]
        save_data(data)

    def load_data(self):
        """Loads the library from a JSON file."""
        data = load_data()
        self.songs = [Song.from_dict(item) for item in data]

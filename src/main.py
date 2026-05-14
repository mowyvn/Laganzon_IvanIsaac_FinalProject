"""Main entry point for the MoodSync application."""
import sys
import time
from library import MusicLibrary
from song import Song
from utils import clear_screen, get_valid_energy, titles, eb, red, green, yellow, orange, rst

def display_menu():
    """Displays the main user menu."""
    titles("MOODSYNC MENU", 0)
    print("   1  │ Add Song")
    print("   2  │ View Songs")
    print("   3  │ Search Songs")
    print("   4  │ Recommend Songs")  
    print("   5  │ Sort Songs")        
    print("   6  │ Play Song")        
    print("   7  │ Favorites")
    print("   8  │ Statistics")   
    print("   9  │ Remove Song")
    print("   0  │ Save Data")
    print(" [ ↵ ]│ Close (Auto Saves)")

def main():
    """Main operational loop of the program."""
    library = MusicLibrary()

    while True:
        clear_screen()
        display_menu()
        choice = input("\nEnter your choice: ").strip()

        # Leave input empty and press enter to close and save the program.
        if not choice:
            print("Saving Data...")
            library.save_data()
            time.sleep(0.5)
            print(f"{green}Data saved.{rst}")
            time.sleep(0.25)
            print(f"{red}Closing...{rst}")
            time.sleep(0.5)
            sys.exit()

        # Choice 1: Add Songs
        elif choice == '1':
            while True:
                clear_screen()
                titles("ADD SONGS", 1)
                if not (title := input("Enter song title: ")): break
                if not (artist := input("Enter artist name: ")): continue
                if not (genre := input("Enter genre: ")): continue
                if not (mood := input("Enter mood (e.g., Energetic, Chill, Focused, Happy): ")): continue
                
                if not (energy := get_valid_energy("Enter energy level (1-10): ", title, artist, genre, mood)): continue
                
                new_song = Song(title, artist, genre, mood, energy)
                if library.add_song(new_song):
                    print(f'{green}"{title}" by {artist} successfully added.{rst}')
                    eb("add another song")
                    clear_screen()
                else:
                    print(f'{yellow}"{title}" by {artist} already exists.{rst}')
                    eb("add a different song")
                    clear_screen()

        # Choice 2: View Songs
        elif choice == '2':
            clear_screen()
            titles("SONGS", 0)
            library.display_songs()
            eb("go back to menu")

        # Choice 3: Search Songs
        elif choice == '3':
            while True:
                clear_screen()
                titles("SEARCH SONGS", 1)
                if not (keyword := input("Enter keyword to search (title, artist, genre, mood): ")): break
                results = library.search_song(keyword)
                if results:
                    print("\nSearch Results:")
                    library.display_songs(results)
                    eb("search again")
                else:
                    print(f"{yellow}No matching songs found.{rst}")
                    eb("search for a different song")

        # Choice 4: Recommend Songs
        elif choice == '4':
            while True:
                clear_screen()
                titles("RECOMMEND SONGS", 1)
                if not (mood := input("Enter the mood you are looking for: ")): break
                recommendation = library.recommend_songs(mood)
                if recommendation:
                    print("\nWe recommend you listen to:")
                    print(f"{green}♪ {recommendation.title} by {recommendation.artist} ♪{rst}")
                    eb("look for another recommendation")
                else:
                    print(f"{yellow}No matching songs found for that mood.{rst}")
                    eb("look for another recommendation")

        # Choice 5: Sort Songs
        elif choice == '5':
            while True:
                clear_screen()
                titles("SORT", 1)
                print("Sort options: title, artist, energy, plays, favorites")
                if not (inp := input("Enter sort criteria: ")): break
                criteria = inp.lower()
                if criteria in ['title', 'artist', 'energy', 'plays', 'favorites']:
                    library.sort_songs(criteria)
                    print(f"\nLibrary sorted by {criteria}:")
                    library.display_songs()
                    eb("change sorting type")
                else:
                    print(f"{red}Invalid sorting criteria.{rst}")
                    eb("change sorting type")

        # Choice 6: Play Songs
        elif choice == '6':
            while True:
                clear_screen()
                titles("PLAY SONGS", 1)
                if not (title := input("Enter the title of the song to play: ")): break
                song = next((s for s in library.songs if s.title.lower() == title.lower()), None)
                if song:
                    song.play_song()
                    print(f"{orange}Playing '{song.title}'... Play count is now {song.play_count}.{rst}")
                    eb("play another song")
                else:
                    print(f"{red}Song not found.{rst}")
                    eb("play a different song")

        # Choice 7: Favorites 
        elif choice == '7':
            while True:
                clear_screen()
                titles("FAVORITES", 1)
                # Using list comprehension to filter favorites
                favorites = [s for s in library.songs if s.favorite]
                if favorites:
                    print("Favorite Songs:")
                    library.display_songs(favorites)
                else:
                    print(f"{red}No favorites found.{rst}")

                if not (title := input("\nInput song title to toggle favorite status: ")): break
                song = next((s for s in library.songs if s.title.lower() == title.lower()), None)
                if song:
                    song.toggle_favorite()
                    status = "added to" if song.favorite else "removed from"
                    print(f'{green}"{song.title}" {status} favorites.{rst}')
                    eb("toggle another")
                else:
                    print(f"{red}Song not found.{rst}")
                    eb("enter a different song")

        # Choice 8: Statistics
        elif choice == '8':
            clear_screen()
            titles("STATISTICS", 0)
            stats = library.calculate_statistics() # Calls the logic in library.py
            
            if stats is None:
                print(f"{yellow}Your library is currently empty.{rst}")
                print(f"{yellow}Add some songs first to see your listening stats!{rst}")
                eb("go back to menu")
            else:
                print(f"{'Total Songs Stored':<20} │ {stats['total_songs']}")
                print(f"{'Total Play Count':<20} │ {stats['total_plays']}")
                print(f"{'Most Played Song':<20} │ {stats['most_played']}")
                print(f"{'Favorite Genre':<20} │ {stats['favorite_genre']}")
                print(f"{'Most Common Mood':<20} │ {stats['common_mood']}")
                print(f"{'Average Energy Level':<20} │ {stats['average_energy']}")
                eb("go back to menu")

        # Choice 9: Remove Songs
        elif choice == '9':
            while True:
                clear_screen()
                titles("REMOVE SONGS", 1)
                if not (title := input("Enter the title of the song to remove: ")): break
                song = next((s for s in library.songs if s.title.lower() == title.lower()), None)
                if song:
                    c = 0
                    while True:
                        clear_screen()
                        titles("REMOVE SONGS", 1)
                        print(f"Enter the title of the song to remove: {title}")
                        if c > 0: print(f"{yellow}Please enter a valid input!{rst}")
                        if not (inp := input(f"{yellow}Are you sure you want to remove '{title}'? (y/n): {rst}")): break
                        confirm = inp.strip().lower()
                        if confirm == 'y':
                            library.remove_song(title)
                            print(f'{green}"{title}" successfully removed.{rst}')
                            eb("remove another song")
                            break
                        elif confirm == 'n':
                            print(f"{red}Removal cancelled.{rst}")
                            eb("remove a different song")
                            break
                        else:
                            c += 1
                            continue
                else:
                    print(f"{red}Song not found.{rst}")
                    eb("enter a different song")

        # Choice 0: Save
        elif choice == '0':
            library.save_data()
            print(f"{green}Data saved successfully.{rst}")
            eb("continue")

        # Invalid input handler.
        else:
            print(f"{yellow}INVALID INPUT, please choose from menu!{rst}")
            eb("continue")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{yellow}Program interrupted. {red}Exiting MoodSync...{rst}")
        time.sleep(1)
        sys.exit()

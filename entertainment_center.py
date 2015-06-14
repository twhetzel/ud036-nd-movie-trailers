import fresh_tomatoes
import media

# Define movie objects
toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4",
                        media.Movie.VALID_RATINGS[0])

avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     media.Movie.VALID_RATINGS[2])

monsters = media.Movie("Monsters Inc.",
                       "Monsters generate their city's power by scaring children, but they are terribly afraid themselves of being contaminated by children, so when one enters Monstropolis, top scarer Sulley finds his world disrupted.",
                       "http://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG",
                       "https://www.youtube.com/watch?v=FLWO5uyFpNo",
                       media.Movie.VALID_RATINGS[0])

shrek = media.Movie("Shrek",
                    "After his swamp is filled with magical creatures, an ogre agrees to rescue a princess for a villainous lord in order to get his land back.",
                    "http://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg",
                    "https://www.youtube.com/watch?v=jYejzdBwvY4",
                    media.Movie.VALID_RATINGS[1])

shrek2 = media.Movie("Shrek 2",
                     "Princess Fiona's parents invite her and Shrek to dinner to celebrate her marriage. If only they knew the newlyweds were both ogres.",
                     "http://upload.wikimedia.org/wikipedia/en/b/b9/Shrek_2_poster.jpg",
                     "https://www.youtube.com/watch?v=dB7a9utApIQ",
                     media.Movie.VALID_RATINGS[1])

star_trek = media.Movie("Star Trek (2009)",
                        "The brash James T. Kirk tries to live up to his father's legacy with Mr. Spock keeping him in check as a vengeful, time-traveling Romulan creates black holes to destroy the Federation one planet at a time.",
                        "http://upload.wikimedia.org/wikipedia/en/2/29/Startrekposter.jpg",
                        "https://www.youtube.com/watch?v=SyJszxnJydA",
                        media.Movie.VALID_RATINGS[2])

# Generate list of movies to display on the web page 
movies = [toy_story, avatar, monsters, shrek, shrek2, star_trek]

# Create HTML file for movie trailer web site
fresh_tomatoes.open_movies_page(movies)



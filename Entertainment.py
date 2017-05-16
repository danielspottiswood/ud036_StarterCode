mport media
import fresh_tomatoes


# We must import both of the above modules.
# The code below creates a Movie object for each of the following six movies.
limitless = media.Movie("Limitless",
                        "An average 28-year-old man gains the ability to use"\
                        " the full extent of his brain's capabilities.",
                        "http://img.yescdn.ru/2016/07/26/cover/68456f1c4d52df66d607a81238eac373-limitless-1469592268.jpg", # noqa
                        "https://www.youtube.com/watch?v=jOLqNOfzus4")

avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a unique mission" \
                     "becomes torn between following his orders and"\
                     " protecting the world he feels is his home.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg", # noqa
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

happy_gilmore = media.Movie("Happy Gilmore",
                            "A rejected hockey player puts his skills to the "\
                            "golf course to save his grandmother's house.",
                            "https://upload.wikimedia.org/wikipedia/en/b/be/Happygilmoreposter.jpg", # noqa
                            "https://www.youtube.com/watch?v=-6sT7MSJ4GE")

ferris_bueller = media.Movie("Ferris Bueller's Day Off",
                             "A high school wise guy is determined to have "\
                             "a day off from school, despite what he is told.",
                             "http://www.movienewsletters.net/photos/006534H1.jpg",
                             "https://www.youtube.com/watch?v=R-P6p86px6U")

Dark_Knight = media.Movie("The Dark Knight",
                          "When the menace known as the Joker wreaks "\
                          "havoc and chaos on the people of Gotham, the Dark" \
                          "Knight must come to terms with one of the greatest"\
                          " psychological tests of his ability to fight injustice.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg", # noqa
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY")

Money_Ball = media.Movie("MoneyBall",
                         "Brad Pitt stars in this film about Oakland A's general manager "\
                         "Billy Beane and his attempt to put together a baseball club on a "\
                         "budget by employing a young statistician",
                         "https://upload.wikimedia.org/wikipedia/en/2/2e/Moneyball_Poster.jpg", # noqa
                         "https://www.youtube.com/watch?v=AiAHlZVgXjk")

# This creates an array of the movie object names and then uses the function in fresh_tomatoes to create a website with these movies.
movies = [limitless, avatar,
          happy_gilmore,ferris_bueller, Dark_Knight, Money_Ball]
fresh_tomatoes.open_movies_page(movies)

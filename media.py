import webbrowser


class Movie():
# This class defines a movie with the four traits described below.
# It has a function that shows the trailer of the movie from the web.

    def __init__(
        self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url):
        """
        Initializes the Movie object with the following traits,
        and sets them to be equal to that of the object.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        
    def show_trailer(self):
        """
        Opens the trailer of the specific movie.
        """
        webbrowser.open(self.trailer_youtube_url)

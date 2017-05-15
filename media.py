import webbrowser
class Movie():
    #The function below initializes the Movie object with the following traits, and sets them to be equal to that of the object.
    def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_id = trailer_youtube
    #This function opens the trailer of the specific movie.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

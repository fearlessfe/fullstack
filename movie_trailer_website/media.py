# coding=utf-8
"""
Module to display movie object, attributes and instances
"""
import webbrowser


# def class Movie
class Movie():
    """
    Class Movie stores movie related information
    """
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        """
        Initiallize instance of class Movie

        :para movie_title: string
        :para movie_storyline: string
        :para poster_image: string
        :para trailer_youtube: string
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Initializing instance for opening the youtube video
        :return: webbrowser to play thriller
        """
        webbrowser.open(self.trailer_youtube_url)

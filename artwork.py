class Artwork:
    """
    Represents an individual piece of art in the museum's collection.

    Attributes:
        title (str): The title of the artwork.
        artist (str): The artist who created the artwork.
        date_of_creation (str): The date of creation of the artwork.
        historical_significance (str): The historical significance of the artwork.
        exhibition_location (str): The location where the artwork is exhibited.
    """

    def __init__(self, title, artist, date_of_creation, historical_significance, exhibition_location):
        self._title = title
        self._artist = artist
        self._date_of_creation = date_of_creation
        self._historical_significance = historical_significance
        self._exhibition_location = exhibition_location
        self._exhibitions = []

    # Getter and setter methods for attributes

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_artist(self):
        return self._artist

    def set_artist(self, artist):
        self._artist = artist

    def get_date_of_creation(self):
        return self._date_of_creation

    def set_date_of_creation(self, date_of_creation):
        self._date_of_creation = date_of_creation

    def get_historical_significance(self):
        return self._historical_significance

    def set_historical_significance(self, historical_significance):
        self._historical_significance = historical_significance

    def get_exhibition_location(self):
        return self._exhibition_location

    def set_exhibition_location(self, exhibition_location):
        self._exhibition_location = exhibition_location

    def add_to_exhibition(self, exhibition):
        self._exhibitions.append(exhibition)

    def get_exhibitions(self):
        return self._exhibitions

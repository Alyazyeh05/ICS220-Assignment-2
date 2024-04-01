class Exhibition:
    """
    Represents an exhibition held at the museum.

    Attributes:
        name (str): The name of the exhibition.
        location (str): The location of the exhibition.
        duration (str): The duration of the exhibition.
        artworks (List[Artwork]): List of artworks featured in the exhibition.
    """

    def __init__(self, name, location, duration):
        self._name = name
        self._location = location
        self._duration = duration
        self._artworks = []

    # Getter and setter methods for attributes

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def get_duration(self):
        return self._duration

    def set_duration(self, duration):
        self._duration = duration

    def add_artwork(self, artwork):
        self._artworks.append(artwork)

    def get_artworks(self):
        return self._artworks

class Location:
    """
    Represents a location within the museum.

    Attributes:
        name (str): The name of the location.
        capacity (int): The capacity of the location.
        current_occupancy (int): The current occupancy of the location.
    """

    def __init__(self, name, capacity, current_occupancy):
        self._name = name
        self._capacity = capacity
        self._current_occupancy = current_occupancy

    # Getter and setter methods for attributes

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_capacity(self):
        return self._capacity

    def set_capacity(self, capacity):
        self._capacity = capacity

    def get_current_occupancy(self):
        return self._current_occupancy

    def set_current_occupancy(self, current_occupancy):
        self._current_occupancy = current_occupancy

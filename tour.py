class Tour:
    """
    Represents a guided tour arranged by the museum for visitors.

    Attributes:
        guide (str): The name of the tour guide.
        date (str): The date of the tour.
        time (str): The time of the tour.
        max_capacity (int): The maximum capacity of the tour.
    """

    def __init__(self, guide, date, time, max_capacity):
        self._guide = guide
        self._date = date
        self._time = time
        self._max_capacity = max_capacity

    # Getter and setter methods for attributes

    def get_guide(self):
        return self._guide

    def set_guide(self, guide):
        self._guide = guide

    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def get_time(self):
        return self._time

    def set_time(self, time):
        self._time = time

    def get_max_capacity(self):
        return self._max_capacity

    def set_max_capacity(self, max_capacity):
        self._max_capacity = max_capacity

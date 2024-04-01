class Event:
    """
    Represents a special event organized by the museum.

    Attributes:
        name (str): The name of the event.
        location (str): The location of the event.
        duration (str): The duration of the event.
        ticket_price (float): The price of tickets for the event.
        tickets_sold (int): The number of tickets sold for the event.
    """

    def __init__(self, name, location, duration, ticket_price):
        self._name = name
        self._location = location
        self._duration = duration
        self._ticket_price = ticket_price
        self._tickets_sold = 0

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

    def get_ticket_price(self):
        return self._ticket_price

    def set_ticket_price(self, ticket_price):
        self._ticket_price = ticket_price

    def get_tickets_sold(self):
        return self._tickets_sold

    def increment_tickets_sold(self):
        self._tickets_sold += 1

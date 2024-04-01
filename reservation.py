class Reservation:
    """
    Represents a reservation made by a visitor for an event or tour.

    Attributes:
        visitor (Visitor): The visitor who made the reservation.
        event_or_tour (str): The type of event or tour for which the reservation is made.
        date (str): The date of the reservation.
        status (str): The status of the reservation (e.g., confirmed, pending).
    """

    def __init__(self, visitor, event_or_tour, date, status):
        self._visitor = visitor
        self._event_or_tour = event_or_tour
        self._date = date
        self._status = status

    # Getter and setter methods for attributes

    def get_visitor(self):
        return self._visitor

    def set_visitor(self, visitor):
        self._visitor = visitor

    def get_event_or_tour(self):
        return self._event_or_tour

    def set_event_or_tour(self, event_or_tour):
        self._event_or_tour = event_or_tour

    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

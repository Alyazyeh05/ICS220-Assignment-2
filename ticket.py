class Ticket:
    """
    Represents a ticket purchased by a visitor for an event.

    Attributes:
        visitor (Visitor): The visitor who purchased the ticket.
        event (str): The type of event for which the ticket is purchased.
        price (float): The price of the ticket.
    """

    def __init__(self, visitor, event, price):
        self._visitor = visitor
        self._event = event
        self._price = price

    # Getter and setter methods for attributes

    def get_visitor(self):
        return self._visitor

    def set_visitor(self, visitor):
        self._visitor = visitor

    def get_event(self):
        return self._event

    def set_event(self, event):
        self._event = event

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

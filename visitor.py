class Visitor:
    """
    Represents an individual who visits the museum.

    Attributes:
        name (str): The name of the visitor.
        age (int): The age of the visitor.
        national_id (str): The national ID of the visitor.
        tickets (List[Ticket]): List of tickets purchased by the visitor.
    """

    def __init__(self, name, age, national_id):
        self._name = name
        self._age = age
        self._national_id = national_id
        self._tickets = []

    # Getter and setter methods for attributes

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_national_id(self):
        return self._national_id

    def set_national_id(self, national_id):
        self._national_id = national_id

    def add_ticket(self, ticket):
        self._tickets.append(ticket)

    def get_tickets(self):
        return self._tickets

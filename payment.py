class Payment:
    """
    Represents a payment made by a visitor for purchasing tickets.

    Attributes:
        amount (float): The amount of the payment.
        payment_method (str): The method used for payment (e.g., credit card, cash).
        transaction_id (str): The unique identifier for the transaction.
    """

    def __init__(self, amount, payment_method, transaction_id):
        self._amount = amount
        self._payment_method = payment_method
        self._transaction_id = transaction_id

    # Getter and setter methods for attributes

    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount

    def get_payment_method(self):
        return self._payment_method

    def set_payment_method(self, payment_method):
        self._payment_method = payment_method

    def get_transaction_id(self):
        return self._transaction_id

    def set_transaction_id(self, transaction_id):
        self._transaction_id = transaction_id

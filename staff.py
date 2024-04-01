class Staff:
    """
    Represents a staff member working at the museum.

    Attributes:
        name (str): The name of the staff member.
        role (str): The role or position of the staff member.
        contact_info (str): The contact information of the staff member.
    """

    def __init__(self, name, role, contact_info):
        self._name = name
        self._role = role
        self._contact_info = contact_info

    # Getter and setter methods for attributes

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_role(self):
        return self._role

    def set_role(self, role):
        self._role = role

    def get_contact_info(self):
        return self._contact_info

    def set_contact_info(self, contact_info):
        self._contact_info = contact_info

class Text_prod:
    def __init__(self, firstname, price, quantity, description, file):
        self.firstname = firstname
        self.price = price
        self.quantity = quantity
        self.description = description
        self.file = file


class Modify_prod:
    def __init__(self, firstname=None, price=None, quantity=None, description=None, file=None):
        self.firstname = firstname
        self.price = price
        self.quantity = quantity
        self.description = description
        self.file = file


class Text_serv:
    def __init__(self, emaillogin, password):
        self.emaillogin = emaillogin
        self.password = password



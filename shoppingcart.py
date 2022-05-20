class Item:
    def __init__(self, ID = -1, name = "null", price = 0.0, quantity = -1, description = "null"):
        self.ID = ID
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    @classmethod
    def importItem(cls, ID, name, price, quantity, description):
        return cls(ID, name, price, quantity, description)

    def __str__(self):
        result = ""
        result += "ID: " + str(self.ID) + "\n"
        result += "Name: " + self.name + "\n"
        result += "Price: $" + str(self.price) + "\n"
        result += "Quantity: " + str(self.quantity) + "\n"
        result += "Description: " + self.description
        return result

    def __eq__(self, item):
        return self.ID == item.ID
        pass

class User:
    def __init__(self, username = "null", firstName = "null", lastName = "null", email = "null", credit = 0.0):
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.credit = credit

    @classmethod
    def importUser(cls, username, firstName, lastName, email, credit):
        return cls(username, firstName, lastName, email, credit)

    def addCredit(self, amount):
        if not isinstance(amount, "float"):
            raise TypeError("Entered amount is not a number.")
        if amount <= 0.0:
            raise ValueError("Amount is non-positive.")
        self.credit += amount

    def removeCredit(self, amount):
        if not isinstance(amount, "float"):
            raise TypeError("Entered amount is not a number.")
        if amount <= 0.0:
            raise ValueError("Amount is non-positive.")
        self.credit -= amount

    def __str__(self):
        result = ""
        result += "Username: " + self.username + "\n"
        result += "First name: " + self.firstName + "\n"
        result += "Last name: " + self.lastName + "\n"
        result += "Email: " + self.email + "\n"
        result += "Store credit: " + str(self.credit)
        return result
    
class Cart(User):
    def __init__(self, username = "null", firstName = "null", lastName = "null", email = "null", credit = 0.0):
        super(Cart, self).__init__(username, firstName, lastName, email, credit)
        self._items = []

    @classmethod
    def importCart(cls, username, firstName, lastName, email, credit):
        return cls(username, firstName, lastName, email, credit)

    def addItem(self, item):
        if not isinstance(item, Item):
            raise TypeError("Parameter is not Item type.")
        self._items.append(item)

    def removeItem(self, item):
        if not isinstance(item, Item):
            raise TypeError("Parameter is not Item type.")
        self._items.remove(item)

    
    

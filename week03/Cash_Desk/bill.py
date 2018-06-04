class Bill:
    def __init__(self, amount):
        if isinstance(amount, int) is False:
            raise TypeError("Amount must be integer!")
        if amount < 0:
            raise ValueError("Amount must be positive!")
        self.amount = amount

    def __str__(self):
        return str(self.amount)

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __repr__(self):
        return str(self.amount)

    def __hash__(self):
        return hash(self.amount)

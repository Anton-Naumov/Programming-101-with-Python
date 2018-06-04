from copy import deepcopy
from bill import Bill


class BatchBill:
    def __init__(self, list_of_bills=[]):
        for bill in list_of_bills:
            if isinstance(bill, Bill) is False:
                raise TypeError("All elements in list_of_bills must be"
                                "isinstance of Bill")
        self.bills = deepcopy(list_of_bills)

    def __len__(self):
        return len(self.bills)

    def total(self):
        return sum([b.amount for b in self.bills])

    def __getitem__(self, index):
        return self.bills[index]

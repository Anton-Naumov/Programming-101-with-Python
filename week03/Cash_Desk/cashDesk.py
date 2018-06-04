from bill import Bill
from batchBill import BatchBill


class CashDesk:
    def __init__(self):
        self.money = []

    def take_money(self, new_money):
        if isinstance(new_money, Bill):
            self.money.append(new_money)
        elif isinstance(new_money, BatchBill):
            for bill in new_money:
                self.money.append(Bill(bill.amount))
        else:
            raise TypeError('take_money method takes Bill or'
                            'BatchBill instances!')

    def total(self):
        total_money = 0
        for bill in self.money:
            total_money += bill.amount
        return total_money

    def __str__(self):
        if len(self.money) == 0:
            return ''
        self.money.sort(key=lambda bill: bill.amount)
        final_string = ''
        dollars, count = self.money[0].amount, 1
        for bill in self.money[1:]:
            if bill.amount == dollars:
                count += 1
            else:
                final_string = f'{final_string}{dollars}$ bills - {count}\n'
                dollars, count = bill.amount, 1
        final_string = f'{final_string}{dollars}$ bills - {count}\n'
        return final_string

    def inspect(self):
        print(str(self))

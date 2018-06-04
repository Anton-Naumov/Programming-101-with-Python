import unittest

from bill import Bill
from batchBill import BatchBill
from cashDesk import CashDesk


class TestCashDesk(unittest.TestCase):
    def setUp(self):
        self.bill = Bill(10)
        self.cash_desk = CashDesk()
        self.cash_desk.money = [Bill(5), Bill(20)]

    def test_take_money_method_with_a_Bill(self):
        self.cash_desk.take_money(self.bill)
        self.assertEqual(self.cash_desk.money, [Bill(5), Bill(20), Bill(10)])

    def test_take_money_method_with_a_Batch_of_Bills(self):
        values = [10, 20, 50]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        self.cash_desk.take_money(batch)
        self.assertEqual(self.cash_desk.money,
                         [Bill(5), Bill(20), Bill(10), Bill(20), Bill(50)])

    def test_take_money_method_with_invalid_argument(self):
        with self.assertRaises(TypeError):
            self.cash_desk.take_money('not Bill or BatchBill')

    def test_total_method_without_any_money(self):
        desk = CashDesk()
        self.assertEqual(desk.total(), 0)

    def test_total_method_with_money(self):
        self.assertEqual(self.cash_desk.total(), 25)
        self.cash_desk.take_money(Bill(100))
        self.assertEqual(self.cash_desk.total(), 125)

    def test___str___method_with_not_any_money(self):
        self.assertEqual(str(CashDesk()), '')

    def test___str___method_with_one_Bill(self):
        desk = CashDesk()
        desk.take_money(Bill(100))
        self.assertEqual(str(desk), '100$ bills - 1\n')

    def test___str___method(self):
        self.cash_desk.take_money(BatchBill([Bill(10), Bill(10), Bill(5)]))
        self.assertEqual(str(self.cash_desk), '5$ bills - 2\n'
                                              '10$ bills - 2\n'
                                              '20$ bills - 1\n')
        self.cash_desk.take_money(Bill(20))
        self.cash_desk.take_money(Bill(10))
        self.assertEqual(str(self.cash_desk), '5$ bills - 2\n'
                                              '10$ bills - 3\n'
                                              '20$ bills - 2\n')


if __name__ == '__main__':
    unittest.main()

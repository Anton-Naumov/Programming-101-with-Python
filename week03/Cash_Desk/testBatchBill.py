import unittest

from bill import Bill
from batchBill import BatchBill


class TestBatchBill(unittest.TestCase):
    def setUp(self):
        values = [10, 20, 50, 100]
        self.bills = [Bill(value) for value in values]
        self.batch_bill = BatchBill(list_of_bills=self.bills)

    def test___init___method_with_non_Bill_instance_in_list_of_bills(self):
        with self.assertRaises(TypeError):
            BatchBill([Bill(10), Bill(15), 'abc'])

    def test___init___method(self):
        self.assertEqual(self.batch_bill.bills,
                         [Bill(10), Bill(20), Bill(50), Bill(100)])
        self.bills[0] = Bill(50)
        self.assertEqual(self.batch_bill.bills,
                         [Bill(10), Bill(20), Bill(50), Bill(100)])

    def test___len___method(self):
        self.assertEqual(len(self.batch_bill), 4)

    def test_total_method(self):
        self.assertEqual(self.batch_bill.total(), 180)

    def test___getitem___method(self):
        _sum = 0
        for bill in self.batch_bill:
            _sum += int(bill)
        self.assertEqual(self.batch_bill[1], Bill(20))
        self.assertEqual(_sum, 180)


if __name__ == '__main__':
    unittest.main()

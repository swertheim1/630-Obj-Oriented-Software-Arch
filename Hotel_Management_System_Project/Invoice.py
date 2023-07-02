from datetime import datetime
from datetime import timedelta
from _datetime import date


class Invoice:

    def __init__(self, invoice_number, num_nights, check_in_date, check_out_date, room_rate):
        self.invoice_number = invoice_number
        self.num_nights = num_nights
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.room_rate = room_rate
        self.invoice_total = room_rate
        # self.invoice_total = self.check_out_date - self.check_in_date) * 3

    def create_invoice(self):
        billing_date = date(2023, 2, 20)
        for night in range(self.num_nights):
            print(f'Date: {billing_date}  .................... ${self.room_rate}')
            billing_date = billing_date + timedelta(1)
        print(f'Date Paid: {self.check_out_date}  .................... ${self.room_rate * 3}')

    def pay_invoice(self, payment_amt):
        self.invoice_total = Invoice.calculate_number_of_nights(self) * self.room_rate
        if payment_amt == self.invoice_total:
            self.invoice_total = 0.00
        else:
            self.invoice_total = payment_amt - self.invoice_total
        print('AMOUNT PAID: ', payment_amt)
        print('INVOICE BALANCE: ', self.invoice_total)

    def calculate_number_of_nights(self):
        return (self.check_out_date - self.check_in_date).days


def test():
    invoice1 = Invoice(123456, 3, datetime(2023, 2, 20), datetime(2023, 2, 20) + timedelta(3), 161, )
    Invoice.create_invoice(invoice1)
    invoice1.pay_invoice(483)


if __name__ == '__main__':
    test()

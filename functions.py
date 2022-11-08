bill = 175.00

tax_rate = 15


def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100.00, 2)

print('Total Tax:', calculate_tax(bill, tax_rate))

print('Total Tax:', calculate_tax(164.33, 22)) #Tech%2016
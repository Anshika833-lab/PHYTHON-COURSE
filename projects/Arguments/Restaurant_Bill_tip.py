def total_amount(bill_amount, tip_perc):
    '''This function calculates the amount to be paid by the customer'''

    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")

total_amount(150, 20)
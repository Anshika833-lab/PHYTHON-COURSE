actual_cost = float(input("please enter the actual product price: "))
sale_amount = float(input("please enter the sale amount: "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("total_profit = {} in rupees for actual cost{}".format(amount, actual_cost))
else:
    print("no profit!!")

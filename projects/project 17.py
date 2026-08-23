def calculate_change(paid, price):
    change = paid - price
    return change

ticket_price = 30
print("======= Parking lot ticket helper =======")
print(f"this parking ticket costs {ticket_price}units.")

print("accepeted coins: (1, 5, 10, 25)\n")
total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Please enter a coin: (1, 5, 10 or 25)"))
    if coin != 1 and coin !=5 and coin!= 10 and coin != 25:
        print("invalid choice, try again\n")
        continue
    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total so far:{total_inserted}")

    if total_inserted >= ticket_price:
        print("Enough money is paid\n")
        break

change_due = calculate_change(total_inserted, ticket_price)

print("printing your parking ticket....")

if change_due == 0:
    pass
else:
    print(f"here is your change: {change_due} units")

    print("====== PAYMENT SUMMARY ======")
    print("Ticket price:", ticket_price)
    print("Coins inserted:", coins_inserted)
    print("Total paid:", total_inserted)
    print("Change Given:", change_due)
    print("=============================")

    print("parking lot ticket payment completed!")
    print("have a great day!")



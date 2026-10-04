items = ['pencil', 'eraser', "notebook", 'sharpener', "glue"]
stock_counts = [12, 0, 8, 5, 3]

inventory = {item: count for item, count in zip(items, stock_counts)}
print("full inventory:", inventory)

in_stock_items = [item for item in items if inventory[item]>0]
print("Item in stock:", in_stock_items)

choosen_item = input('what item do you want to buy?')

if choosen_item not in inventory or inventory[choosen_item] == 0:
    print(choosen_item, "is not in stock! stopping the checker....")
    exit()

prices = [10, 5, 40, 15, 20]
markup = int(input("enter the markup amount to add to every price"))

marked_up_prices = list(map(lambda p: p + markup, prices))
print("Marked up prices:", marked_up_prices)

item_index = items.index(choosen_item)
choosen_price = marked_up_prices[item_index]
print(item_index)
print("the price of", choosen_item, "after markup is:", choosen_price)


inventory[choosen_item] = inventory[choosen_item] - 1
print(choosen_item, "purchased! remaining stock:", inventory[choosen_item])
print("")
print("====== SCHOOL STORE INVENTORY CHECKER ======")
print('item bought:', choosen_item)
print('price paid:', choosen_price)
print("updated inventory:", inventory)
print("=============================================")



    


amount_due = 50

while amount_due > 0 :
    print(f"Amount Due: {amount_due}")
    coins = input("Insert Coin: ")
    if coins == "25" or coins == "10" or coins == "5" :
        amount_due -= int(coins)
print(f"Change Owed: " + str(abs(amount_due)))


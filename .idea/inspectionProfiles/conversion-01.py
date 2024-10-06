amount= int(input("Amount: "))
currency= input(("USD or BDT: "))
if currency.upper()== "USD":
    converted=amount * 120
    print(f"You have {converted} taka")
elif currency.upper()=="BDT":
    converted=amount/120
    print(f"You have {converted} USD")
else: print("Can't Convert")
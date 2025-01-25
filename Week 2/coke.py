#prompt = int(input("Insert coin: "))
PRICE = 50
total = 50
amount = 0
owed = 0
while amount != 50:
    prompt = int(input("Insert coin: "))
    if (prompt == 25) or (prompt == 10) or (prompt == 5):
        amount_owed = total - prompt
        if amount > 50:
            continue
        print(f"Amount due: {amount_owed}")
        total = amount_owed
        amount += prompt
    else:
        prompt = int(input('Insert coin: '))
    if amount >= 50:
            print(f'Change owed: {amount-50}')
    


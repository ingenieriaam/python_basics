####################################################
# It must be reported what money a seller gets in commissions
# of 13% of a sale. This information must be reported on the screen
name = input("enter you name: ")
value = float(input("enter sales amount: "))
commission = round(value * (13/100), 2)

print(f"the seller {name} takes a commission of {commission} dollars")
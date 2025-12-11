from datetime import date,datetime
print("Today : ",date.today())
money = 30
def showing_capital(money):
    print("Current Funds : $",money)



print()
available_products = {
    "Cofee" : 10,
    "Tea" : 8,
    "Choco" : 15,
    "Cookies" : 12,
    "Drinks" : 5
}

#this one is for the shop owner to list the price for his own
#i'll comment down this lines 

# print("\t \tOur shop Product buying list(base price)   ")
# print("\t \t  \titems \t ","prices", sep= "\t", end="\n")
# for items in available_products:
#     print("\t \t",items ," : ",available_products.get(items),sep="\t" )



#this was one of the stupid things maybe i write here  useless this big code block
def useless():

    print("\t \t  \titems \t ","prices", sep= "\t", end="\n")
    for items in available_products:
        #print("\t \t",items ," : ",int(available_products.get(items)*1.5),sep="\t" )
        if items == "cofee":
            print("\t \t \t Cofee "," : ",(available_products.get(items)*2))
            print("\t \t  The Cheapest Price in the Week!!!")
        elif items == "tea":
            print("\t \t \t Tea "," : ",(available_products.get(items)*2))
            print("\t \t  Highest sold product in the Week!!!")
        elif items == "Choco":
            print("\t \t \t Choco "," : ",(available_products.get(items)*2))
            print("\t \t  Brands Actually Matters!!!")
        elif items == "Cookies":
            print("\t \t \t Cookies "," : ",(available_products.get(items)*2))
            print("\t \t  What could be more good snacks than Cookies!!!")
        elif items == "Drinks":
            print("\t \t \t Drinks "," : ",(available_products.get(items)*2))
            print("\t \t  Bottle of Drinks --NOOOOOOO \n \t \t  Full of Energy!!!")



print("\t \tOur shop Product buying list(Selling price)   ")
def display_product():
    for (product,price) in available_products.items():
        print(f"\t \t{product}",end=" ")

display_product()
print("\n")
manager_level = 2.0

User_chioce = input("Enter your desire item : ").title()


#it's teacher's code I need to keep it safe for later uses 

def selling_price(item):
    base_price = available_products[item]
    sell_price = base_price * (1 + manager_level * 0.1)

    return sell_price

def total_price(item,quantity):
    single_price = selling_price(item=item)
    customer_bill = single_price*quantity
    print(f"Total bill : {customer_bill:.2f} ")
    return customer_bill

showing_capital(money)

cost = total_price(User_chioce,quantity=int(input("How many Pcs You want : ")))

def validate_funds(money,cost):
    if money<cost or money==cost:
        print("Your budget is not enough for this ")
        return False
    else:
        money = money-cost
        print(f"You have {money:.2f} left now !" )
        return True
    
if validate_funds(money,cost=cost)==True:
    print("It Works Successfully")
else:
    print("Gather some more money or reduce some products and Try again")








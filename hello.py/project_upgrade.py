base_capital = 100
def show_capital():
    global base_capital    
    print(base_capital)

inventory = {
    'Tea' : {"qty":5,"price":2.99},
    'Coffee' : {"qty":3,"price":2.99},
    'Milk' : {"qty":3,"price":2.99},
    'Bread' : {"qty":7,"price":4.5},
    'Egg' : {"qty":7,"price":2.3}
}
transection = {}
def display_transection():
    for (product,transection_amount) in transection.items():
        print(f"{product}  {transection_amount}")

def availability():
    print("\t Products ------------------ Availablility")
    for products in inventory.keys():
        print(f"\t {products}\t\t\t\t {inventory[products]['qty']}")


def manager_level():
    Manager_lvl = 1
    global base_capital
    if base_capital>300:
        return Manager_lvl+2
    elif base_capital>200:
        return Manager_lvl+1
    elif base_capital<200 and base_capital>0:
        return Manager_lvl


def display_Product():
    for i in inventory.keys():
        print("\t",i,end=" ")
    print("\n")

def user_ch():
    user_choice = input("Enter you choice ").title()
    sell_quantity = int(input("How many you want : "))
    sell(user_choice,quantity=sell_quantity)



def buy(product_name,pcs =5):
    cost = (inventory[product_name]['price']-1)*5
    inventory[product_name]['qty'] += pcs
    global base_capital
    base_capital-=cost
    transection[product_name] = cost



    

def sell(chioce,quantity):
    global base_capital
    if chioce in inventory.keys():
        None
    else:
        user_choice = input("Enter you choice ").title()
        sell_quantity = int(input("How many you want : "))
        sell(user_choice,sell_quantity)

    for products_name in inventory.keys():
        if products_name==chioce :
            if inventory[chioce]['qty']>quantity:
                price = (inventory[chioce]['price'])*(quantity+manager_level()*0.1)
                base_capital += price  
                inventory[chioce]['qty'] -= quantity 
                transection[chioce] = [price]
            elif inventory[chioce]['qty']==quantity:
                price = (inventory[chioce]['price'])*(quantity+manager_level()*0.1)
                print("This was the last stock")
                #i need to call the function for buying this product again 
                buy(chioce)
            else:
                print("Currently this item is not available in the stock")
                #we can call a func from here to show/take action when stock is out 
                buy(chioce)   
    
    #i was writing a else block if customer type wrong name then they can type again
    # else:
    #         chioce = input("Please type the name correctly : ")
    #         quantity = int(input("how many you want : "))
    #         sell(chioce=chioce,quantity=quantity)    
    if inventory[chioce]['qty']<2:
        buy(chioce,pcs=3)





Shopping = 1
while Shopping!='0':
    print("*****************Welcome To Our Shop Sir ******************")
    display_Product()
    user_ch()
    Shopping = (input("Want to buy more write anything or 0 for quit"))


print("Base_capital now : ",base_capital)
print(f"Today's Profit : {base_capital-100}")
print(f"shop available products now : {availability()}")
display_transection()



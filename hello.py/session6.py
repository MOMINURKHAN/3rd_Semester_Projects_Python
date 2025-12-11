#task 1 
def make_pizza():
    print(f"making your pizza - (task-1)")

make_pizza()
#task 2 + task3
def make_pizza_size(size,topping):
    print(f"Making a {size} inch pizza with {topping}")

#make_pizza_size(12,'honey')

#task 4
#make_pizza_size(int(input("Enter the pizza size")),input("Enter the topping you want "))
user_order = 1
all_order = []
while user_order<3:
    #task 5
    size = int(input("Enter size : "))
    topping = input("Enter your toppings ").split(',')
    make_pizza_size(size,topping=topping)

    def task_5(size,topping):
        x = []
        x = " ".join(topping)
        dictionary = {
            'size' : size,
            'topping' : topping,
        }
        return dictionary
        

    #task 8 

    order = (task_5(15,topping=topping))
    # print(order)

    #task 9
    order['crust'] = input("Enter crust : ")
    # print(order)

    #task 10
    user_choice = input("Delivery?(Yes/No)").lower()
    order['delivery'] = True if user_choice=='yes' else False
    user_order+=1
    all_order.append(order)
    


#task 11
#print(f"{order['size']} inch pizza with {order['topping']} 'crust' : {order['crust']} 'Delivery' : {order['delivery']}")

#Task 12
for i in all_order:
    print(f"{i['size']} inch pizza with {i['topping']} 'crust' : {i['crust']} 'Delivery' : {i['delivery']}")

#while doing this H.W I didn't notice i need to change the same function in every task so i made similar function several times, that's my mistake but i only apply the while loop 
#in the last func  and other components for two times and it's working properly




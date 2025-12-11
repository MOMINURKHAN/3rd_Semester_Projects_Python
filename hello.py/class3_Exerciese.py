# #7.7 writing a while loop that never ends
# while True:
#     print("Hello World")
#     break

# #5-3 -> Alien Color #1
# alien_color = 'green'
# user_color = input("Enter a color: ")

# if user_color.lower() == 'green':
#     print("Player earned 5 points")
# else:
#     print("you will not get points")

# #5.4 -> Alien Color #2
# user_color2 = input("Enter a color again : ")
# if user_color2 == 'green' :
#     print("Player got 5 points")
# else:
#     print("Player got 10 points")


# #5.5-> Alien color #3
# user_color3 = input("please Enter a color again: ")
# if user_color3 == 'green':
#     print("you got 5 points")
# elif user_color3 == 'yellow':
#     print("You got 10 points")
# elif user_color3 == 'red':
#     print("You got 15 points")
# else:
#     print("You will not get any points . ")
    

# #5.6 -> Stages of Life
# age = int(input("Enter your age : "))
# if age < 2:
#     print("A baby ")
# elif 2 <= age <= 4:
#     print("a toodler")
# elif 4 < age <= 13:
#     print("A Kid ")
# elif 13 < age <= 20:
#     print("A Teeneger")
# elif 20 < age < 65:
#     print("A Adult")
# elif age >= 65:
#     print("Elder")
# else:
#     print("Write your age correctly please!")

# #5.7 -> Favourite Fruits
# Available_Fruits = ['Banana','Pineapple','Mango']
# UserWant_Fruits = input("Enter a fruit Name : ")
# if UserWant_Fruits in Available_Fruits:
#     print("You really like ",UserWant_Fruits)
# elif UserWant_Fruits == 'Lichi' :
#     print("your choice is good",UserWant_Fruits)
# elif UserWant_Fruits == 'Dragon':
#     print("That's good but we don't have",UserWant_Fruits,"it now")
# elif UserWant_Fruits == 'Apple':
#     print("Your choice is good",UserWant_Fruits)
# elif UserWant_Fruits == 'Watermelon':
#     print("That's a juicy one",UserWant_Fruits)
# else:
#     print("you don't have any choices that we could have or Manage now \n Sorry Sir")

# 5.8 -> Hello Admin
# Usser_name = ['addmin','hashitha','Gilbert','Prattoy']
# for momin in Usser_name:
#     if momin == 'addmin':
#         print("Hello sir, How are you")#special greetings for admin
#     else:
#         print("Hey, Everything is ok right there")#normal greeting for general members


# #5.9 -> No Users

# userr = []

# if userr == []:
#     print("The list is empty")
# else:
#     print("The list is empty")

# print("Hello how are you?")

# #5.10 -> Checking Username
# #current username are taken from one of my favorite chinese drama 
# curr_username = ["chen xiaoxi","jiang chen","wu boosong","Lin Jiangxiao","Lu Yang"]
# #new username is taken from most of the cricketers
# new_username = ["alex ","bob","Max","David","Maxwell","Smith","Jiang CHEN"]

# for name in curr_username:#outer loop 
#     for name_temp in new_username:#inner/nested loop
        
#         if name.lower() == name_temp.lower(): #I use .lower func to make it case insensitive
#             print("Name(curr) : ", name, "Name(new): ",name_temp) #this one to show where exactly the match happen and with which name 
#             print("Not available")
#         else:
#             print("Available")
    
# #5.11 -> Ordinal Numbers
# Ordinal_Num = [1,2,3,4,5,6,7,8,9]
# for num in Ordinal_Num:
#     if num == 1:
#         print(Ordinal_Num[0],'st')#here i try it with list index but it's not perfectly fine i think. because here i know the index but if it's a big list 
# #it's almost impossible to know where the num will be equal to 1 so i think it's not convenient i just try    
#     elif num == 2:
#         print(num,"nd")
#     elif num == 3:
#         print(num,"rd")
#     else:
#         print(num,'th')
# #in this exercise i couldn't it's making a space while printing the statemtn like 1 st not 1st i don't know how to solve the issue

#5.12->styling the previous if-else statemtn---done



# #7.1-> Rental Car

# car_name = input("Sir, Which car you want : ")
# print("Let me see if i can find you a",car_name)

# #7.2 -> Restaurant Seating
# numberOfGuest = int(input("sir how many people are there in your group :"))
# if numberOfGuest > 8:
#     if (numberOfGuest % 8) == 0:
#         print("Sir can you seat on separate tables our regular table capacity is for 8 people")
#         Opinion = input("will you seat separately or together(Yes/No) : ")
#         if Opinion=="Yes":
#             print("Table is ready sir ")
#         else:
#             print("You must wait")
#     else:
#         print("You must wait")
                    
# else:
#     print("table ready")


# #7.3 -> checking multiple of 10

# number = int(input("Enter a Number"))

# if (number%5==0) and (number%2==0): #i just try to determine another method to find multiple of 10...just funny things(Coding is fun after feeling the logic) there's more way i believe
#     print("It's muliple of 10")
# else:
#     print("It's not a multiple of 10")

# #7.4-> pizza toppings

# dressing_Item_list = []
# while(True):
#     dressing_Item = input("Sir/Madam Your  dressing item please  : ")
#     print("Your item is added . Want to add more or wanna quit(for quitting type quit) ")
#     if dressing_Item == "quit":
#         break
#     dressing_Item_list.append(dressing_Item)#first i add it before if statement so it was also appending the quit as a topping so i drag it down

# print("Your topping list Sir/Madam : ",dressing_Item_list)

#7.5-> movie tickets

# while(True):
#     user_age = int(input("Enter your age :"))
#     if user_age < 3:
#         print("No need ticket it's free ")
#     elif user_age >= 3 and user_age <= 12:
#         print("Ticket fare 10$")
#     elif user_age >12:
#         print("Ticket fare 15$")

#     print("if you wanna quit the system type quit")
#     flow = input("quit/continue (type anything for continue): ")
#     if flow == "quit":
#         break

#7.6 ->..............
        
# #7.7->infinite loop 
# # one while loop
# num = 1
# while(True):
#     print(num)
#     num +=1

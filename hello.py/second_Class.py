# # #creating a list of 3 names and priting it using the index

# # names = ["Gilbert","Hashitha","Prattoy"]
# # print(names[0])
# # print(names[1])
# # print(names[2])
# # n = 0
# # string = "Hello guys How's your python learning going on? hope to enjoy it"
# # for name in names:
# #     print(f"{string}\t {names[0]}")

# # #let's explore some comment
# # #this is a single line comment starting with #
# # """this is a multiline comment quoted by 3 double quote """
# # #taking input from user
# # name = input("Name : ")
# # age = int(input("Age : "))
# # Height = float(input("Height : "))
# # print(f"he is {name}\nHe is {age} years old \nHis height is {Height} and he is {input("Marital Status : ")}")
# # print(f"he is a normal person {input("Name :")} ")
#example of conditional operator if-elif-else
#assume a traffic signal point 
# signal = input("color of current signal : ")
# if(signal == "red"):
#     print("You need to stop here \n you can't go further")
# elif(signal == "green"):
#     print("It's your turn you can go sir")
# else:
#     print("ok follow the system ")

# #now checking the ternary operator in python

# food = input("Enter food Name : ")
# eat  = "Yes" if food=="Cake" else "No"
# print(eat)

# game = input("Enter game name : ")
# print(game) if game=="Football" else print("is ",game ," better than Football! ")
# name = input("Name : ")
# age = int(input("Enter your age : "))
# print(name,"is a adult now ") if age>=18 else print(name, "is still a kids")
#there is another one called clever f it's also a ternary operator but works little differently let's see it

# salary = float(input("Salary : "))
# tax = salary *(0.1,0.2) [salary>50000] #if the salary is greater than 50k then tax will be 20%
# print("your total tax is : ",tax,"\nplease Pay the tax in time \n_The Government of Peoples Republic of Bangladesh")

# num_A = int(input("Enter a Number : "))
# num_B = int(input("Enter a Number : "))
# sum = num_A + num_B
# print("The calculated sum of provided two numbers are : ",sum)
# SideofSq = float(input("Enter the side of the square to get the area : "))
# print("Area : ", SideofSq*SideofSq)

#write a program to input two flaoting point and get there average 

# num_1 = float(input("Enter the 1st Number : "))
# num_2 = float(input("Enter the 2nd Number : "))
# average = (num_1+num_2)/2
# print(average)

# print(num_1>=num_2)
# print(True) if num_1>=num_2 else print(False)

#let's try to understand some string things in lecture 2 after 2.5 hours
#str = "Apna college"
#concatination is just adding two string together with + sign it's simple
#then there is slicing string let's see this 


# print(str[0:4]) #[0:4] it means from 0th index to 3rd index it always print till the last-1 digit
# print(str[:6]) #[0:6] this one will works like this 0 to 5 when we'll not mention the starting or ending the python machine will assume that as very beginning or ending 
# print(str[5:len(str)]) #len(str) means lenth of the string and it's also hold the value of reaching to the last digit

# str1 = input("Enter your first name : ")
# print(len(str1))
# print(str1.count("o"))

#let's check user's entered number is odd or even

# num_1 = int (input("Enter a number : "))
# if(num_1/2 == 0):
#     print("Even")
# else:
#     print("Odd")

# #another program to find  the greatest of 3 number entered by the user :
# num1 = int(input("Enter 1st Number : "))
# num2 = int(input("Enter 2nd Nubmer : "))
# num3 = int(input("Enter 3rd Number : "))

# if(num1>num2):
#     if(num1>num3):
#         print("Num1 : " ,num1, " is the greatest Number ")
#     elif(num3>num2):
#         print("Num3 : ",num3,"is the greatest Number ")
# elif(num2>num1):
#     if(num2>num3):
#         print("Num2 : " ,num2, " is the greatest Number ")

# #check user's entered number is dividable by 7 or not 
# number = int(input("Enter a number to check divisible or not by 7 : "))
# if(number%7 == 0):
#     print("helloDivisible")
# else:
#     print("e")
# #it's a number list where i apply append and pop operation
# numbers = ['23','34',53]
# numbers.append(44)
# print(numbers)
# numbers.pop(1)
# print(numbers)
# print(len(numbers))
#it's a question from the apna college tutorial they asked Write a program that ask for favourite movie to 3 user and store it in a list
# Movies = []
# for x in range(1,4):
#     x = input("Enter your favourite movie : ")
#     Movies.append(x)

# print(Movies)

# #It's another question to check if the list contains any palindrome or not 
# number = [1,2,3,2,1]

# x = int(len(number)/2)
# print(x)
# First_Half = number.copy()
# First_Half.reverse()
# print(First_Half)
# if((number[0:(x)])==First_Half[0:(x)]):
#     print("It's a palindrome")
# else:
#     print("It's not a palindrome")



# #now the same operation with a list with string and number
# letter = ['1','abc','abc',1,2,5]
# y = int(len(letter)/2)
# print("This is Y : ",y)
# Second_Half = letter.copy()
# Second_Half.reverse()
# if(letter[0:y]==Second_Half[0:y]):
#     print("it's a palindrome")
# else:
#     print("It's not a palindrome")

##little improvement of my answer 
#we can just reverse the list and check the both one equality if yes then palindrome otherwise not palindrome
# list = ["H","E","L","L","O"]
# list_copy = list.copy()
# list_copy.reverse()
# if(list==list_copy):
#     print("It's a palindrome")
# else:
#     print("It's not a palindrome")

#another problem
#write a program to find the occurance of a in the following tuple
#tuple and list is almost same but tuple is immutable and list is mutable means changable and not changable


# list =('C','D','A','A','B','B','A')
# x = list.count('A')
# print("X is : ",x)
# #another system is 
# print("Above list A appears :",list.count('A'),"times")

# #now need to sort a list 
# listt = ['C','D','A','A','B','B','A']
# listt.sort()
# print(listt) 


#now got another new one have to make a dictionary with the key : value pair

# student = {
#     "table": ["a piece of furniture","a beautiful room arrangment staffs"],
#     "cat": "A mouse",
# }
# print(student)
# print(student.get("chair"))
# print(type(student))


# print a multiplication table of number n with while loop

# n = 5
# i=1
# p=0
# while i<=10:
#     p = n*i
#     print(p,i)
#     i+=1



# #qs print the number of the given list using loop

# listt = [1,4,9,16,25,36,49,64,81,100]
# number = 1
# while number<=10:
#     print(number**2)
#     number+=1
# for number in listt:
#     print(number)



#print number from 1 to 100 using for loop

# for n in range(1,101):
#     print(n)
# for n in range(100,0,-1):
#     print(n)
# n = 5
# for n in range(10):
#     print(5*n)


# #sum of first n numbers using while loop
# n = int(input("Enter a number : "))
# p = 1
# x = 1

# while p<=n:
#     x = x*p
#     print("x :",x,"p : ",p, "i :",n,)
#     p+=1







#Func and Recursion Chap -> 6



#write a func to calculate the length of a list

# def Cal_LengList(lst):
#     print("Function length is : ",len(lst))
# listttt=["Hello","Kuddus",'monsur',"Boyati","Huzur","Saber","Ridwan-Vai","Al-Amin"]

# Cal_LengList(listttt)
# listttt.append("Aminul")
# print(len(listttt))
# Cal_LengList(listttt)


#write a func to print the element of a list in a single line->

# def print_ListElem(lst):
#     print(lst,sep="",end="")
# print_ListElem(listttt)


#write a func to calculate fact of n -> 

def calc_fact(n):
    fact=1
    for c in range(1,n+1):
        fact=fact*c
        
    print("Factorial of ",n,"is",fact)      
          

#calc_fact(int(input("Enter number :")))

#Write a Function to convert RMB/BDT TO BDT/RMB

def convertcurr(curr,num):
    if(curr=="RMB"):
        print(num*17.7)
    elif(curr=="BDT"):
        print(num/17.7)

#convertcurr("RMB",400) 
#convertcurr("BDT",8500)

def show(n):
    if n<-993:
        return
    
    print(n)
    show(n-5)
    print("Hello guys ",print(range))
    
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1) 
   
    
        

#show(5)
h = factorial(5)
print(h)

def firstNNumbersAddition(n):
    if n==0:
        return 0
    else:
        return n + firstNNumbersAddition(n-1)
    
SumofN = firstNNumbersAddition(int(input("Enter a number : ")))
print(SumofN)


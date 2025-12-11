numbers = [2,-34,6,0]

for n in numbers:
    if n>0:
        print(n,"is positive")
    else:
        print(n,"is negative")


 

def FirstFunc():
    birth_year = int(input("Enter your birth year : "))
    if birth_year > (2008):
        print("You are still a kid go back to home")
    elif birth_year<2000:
        print("You're also not eligible why you came here go to the elder's classroom")
    else:
        print("You can continue your study with us")

FirstFunc()

def second_func(name,age,Language = "English"):
    print("Hello How are you",name ,"What's your age ",age)
    print("He's learning",Language,"Language")

second_func("Mominur",23,Language="Chinese")


print("Hello Khan !", end=" sss ", sep= " sldfj ")

def returningFunc():
    c = int(input("Enter a number : "))
    d = c*107
    return d

print("wanna get 107 times of any number then proceed with the instructuction")

f = returningFunc()
print("this is the 107 times of your provided number is :",f)


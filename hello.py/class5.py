# name = "Ali"
# print("Hello",name, sep=" ", end="\n")
# a= 5
# b = 3
# print("Sum : ",a+b,"Difference : ",a-b,"Product : ",a*b, "Division : ",a/b)

# print("Hello")

# product = []
# product.append("Bags")
# product.append("Shoes")
# product.append("Light & Bulbs")
# for products in product:
#     print(products)

# number = int(input("Enter a Number : "))
# if number%3==0:
#     print("Divisble by 3")
# elif number%7==0:
#     print("Divisble by 7")
# else:
#     print("Not divisble by 3/7 ")


# for x in range(0,188,1):
#     print(x)


student = {"Name":"Muhammad Mansur Ali","Age":"25"}
#print(student["Name"])

student["Major"] = "Software Engineering"
student["ID Number "] = "235234132"
student["Country of Origin"] = "Bangladesh"

for x in student:
    if x=="Country of Origin":
        if student[x]=="Pakistan":
            del student["Country of Origin"]

    print(x,":",student[x])
    if x=="Major":
        print("Good Choice buddy go ahead")

Marital_Status = student.get("Marital-Status","No data assigned")
print(Marital_Status)
Name = student.get("Name","No data Assigned")
print(Name)

for key,value in student.items():
    print(key,value)

print("\n\n")
print("Printing the Key using .key() ")
for key in student.keys():
    print(key)

print("\n\n")
print("Printing the Values using .value() ")

for value in student.values():
    print(value)

print("\n\n")
print("Printing the unique value  using .set() ")
student["Title"] = "Muhammad Mansur Ali"
for students in set(student.values()):
    print(students.title())
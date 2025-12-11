#brain activation part

car = {"make":"Toyota" , "model":"Corolla", "year":2020}

print(car)

car["Motorcycle"] = "Harley Davidson"
for key,value in car.items():
    print(key,"Hello",value)

#lion 
# - 
#pen - it has ink and a good shaped body for convenient use
# writing mostly then drawing and sometimes fighting 
# normally release the ink according to the users use and also finish releasing when there's nothing left .
class Student:
    def __init__(self,Name,Major):
        self.Name = Name
        self.Major = Major
        self.Credit = 55
    def Introduce(self):
        print("Hi,I am",self.Name,"I'm studying in the major :",self.Major)
        print("Credit is :",self.Credit)
    def update_credits(self, new_value):
        if new_value>210 or new_value<0:
            print("It's not valid change it it should follow 0<credit<210")
        else:
            self.Credit = new_value;

s1 = Student("Jenniffer","Weapon Enginnering")

s2 = Student("Ricky","Communication Engineering")

s3 = Student("mike","Mining Technology")

Student_list = [s1,s2]
Student_list.append(s3)
for p in Student_list:
    if p==s1:
        s1.update_credits(34)
    p.Introduce()
    
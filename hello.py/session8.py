# # def greet(name):
# #     print(f"Hello,{name}")

# # greet("MOMINUR")

# # fruits = {"Apples","Banana","Pear"}

# # for fuit in fruits:
# #     print(f"Hey")



# def checkingthelarge(num1,num2):
#     if num1 > num2:
#         return num1
#     elif num1 == num2:
#         print("they are equal ")
#         return "you're a  fool"
#     else:
#         return num2


# print("Write two number to compare which one is big")
# a = int(input("Write a number : "))
# b = int(input("Write a number : "))
# # x = checkingthelarge(a,b)
# # print("The large number is ",x)

class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def describe(self):
        print(f"{self.year} {self.make} {self.model}")
     

class GasolineVehicle(Vehicle):
    def __init__(self, make, model, year,tank_size):
        super().__init__(make, model, year)
        self.tank_size = tank_size
    def describe(self):
        print(f"{self.year} {self.make} {self.model} {self.tank_size}")
        
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery = Battery(battery_capacity)
    def describe(self):
        print(f"{self.year} {self.make} {self.model} {self.battery.show_range()}")


class Battery():
    def __init__(self,battery):
        self.battery = battery
    
    def show_range(battery):
        print("The battery range : ")
        if battery == 20000:
            print("it can go approx 300km")
        else:
            print("Ask someone I don't know")

print("Gasoline vehicle : -> ")
vehicle1 = GasolineVehicle("Whatever","Suzuki",2500,"25Ltr")
vehicle1.describe()

print("Electronic vehicle : -> ")
vehicle2 = ElectricVehicle("Idk","bazzaj","2000","25000mah")
vehicle2.describe()

print("Vehicle : -> ")
vehicle3 = Vehicle("Idk","Yamaha",1999)
vehicle3.describe()

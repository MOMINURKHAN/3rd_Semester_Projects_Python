print("=============================================")
print("         Student Management System           ")
print("=============================================")
 #contains student information
list_of_dict = []#this contains list of student dictionaries 
grade_disctionary = {}


def choice():
    print("*********************Menu******************")
    print("1 : Add Student")
    print("2 : Delete Student")
    print("3 : Find Student")
    print("4 ; Modify Student")
    print("5 : calc average")
    print("6 : calc individual grade")
    print("7 : Display Information")
    print("8 : quit the program")
    temp_choice = int(input("choice : "))
    match temp_choice:
        case 1:
            add_student()
        case 2:
            delete_student()
        case 3:
            find_student()
        case 4:
            modify_student()
        case 5:
            calc_average()
        case 6:
            calc_individual_grade()
        case 7:
            display_info()
        case 8:
            return
        case _:
            print("Invalid Input check again and enter again")
            return





def add_student():
    student_dict = {}
    student_id = input("Student id : ")
    #to check wheather there's a second id
    if check_id(student_id=student_id):
        return
    student_dict['student_id'] = student_id.capitalize()
    name = input("Enter name : ")
    student_dict['name'] = name.capitalize()
    gender = input("Gender (M/F) : ")
    student_dict['gender'] = gender.capitalize()
    try:
        chinese_score = float(input("Enter chinese score : "))
        math_score = float(input("Enter math score : "))
    except ValueError:
        print("Wrong input data ")
        return
    student_dict["chinese_score"] = chinese_score
    student_dict["math_score"]=math_score
    list_of_dict.append(student_dict)
def delete_student():
    student_id = input("Enter id : ")
    for i in list_of_dict:
        if(student_id==i['student_id']):
            list_of_dict.remove(i)
            return
    else:
        print("no student foudn with that id")

def find_student():
    student_id = input("Enter id : ")
    for i in list_of_dict:
        if student_id==i["student_id"]:
            print(i)
            return
    else:
        print("no student found with that id")




def modify_student():
    student_id = input("Enter id : ")
    for i in list_of_dict:
        if student_id==i["student_id"]:
            print(f"The present data : \n{i}")
            print("you can enter new data now : ")
            chinese_score = float(input("Enter chinese score : "))
            i["chinese_score"] = chinese_score
            math_score = float(input("Enter math score : "))
            i["math_score"]=math_score
            return
    
            
    
def calc_average():
    chinese_score = 0.0
    math_score = 0.0
    count = 0
    for i in list_of_dict:
        chinese_score += i["chinese_score"]
        math_score += i["math_score"]
        count+=1
    chinese_score/=count
    math_score/=count
    print(f"Chinese Score {chinese_score} \nMath Score {math_score}")
    return

def calc_individual_grade():
    

    for i in list_of_dict:
        temp = (i["math_score"] + i["chinese_score"])/2
        int(temp)
        if 60<temp<=70:
            grade_disctionary[i["name"]] = "D"
        elif 70<temp<=80:
            grade_disctionary[i["name"]] = "C"
        elif 80<temp<=90:
            grade_disctionary[i["name"]] = "B"
        elif 90<temp<=100:
            grade_disctionary[i["name"]] = "A"
    print(grade_disctionary)
        

def display_info():
    for i in list_of_dict:
        print(f"Name : {i["name"]}")
        print(f"ID : {i['student_id']}")

def check_id(student_id):
    for i in list_of_dict:
        if student_id == i["student_id"]:
            print("This id already exist")
            return True



while(1):
    choice()
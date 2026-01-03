class Student:
    def __init__(self,name,nationality,contact,student_id,date_of_birth,Major,email):
        self.name = name
        self.nationality = nationality
        self.contact = contact
        self.student_id = student_id
        self.Major = Major
        self.email = email
        self.courses_included = [] #include the course code
        self.grades = {} #{"course_code" :[grade1,grade2,]}
        self.attendence = {}
    

        
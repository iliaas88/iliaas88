import json
class Course:
    id = 0
    name = ''
    units = 0
    score = 0.0
    courses = []

    def __init__(self, id, name, units,score) -> None:
        self.id = id
        self.name = name
        self.units = units
        self.score=score
    def __eq__(self, other) :
        return   type(self)==type(other) and self.id==other.id 
    def __str__(self) :
        return  'id: {}  name : {} unit:{} score:{} '.format(self.id,self.name,self.units,self.score) 
    @staticmethod
    def get_course(id):
        if Course(id,'',0,0) not in Course.courses: 
            print("not exist")
        else:
            s=Course.courses.index(Course(id,'',0,0))
            return Course.courses[s]    


    @staticmethod
    def add_course(course):
        if not isinstance(course,Course):
            print('argument is not a Course object')
        elif course in Course.courses:
            print('course already exists')
        
        else:
            Course.courses.append(course)

    @staticmethod
    def remove_course(id):
        if not isinstance(id,int):
            print('argument should be a int') 
        elif not Course(id,'',0,0)  in Course.courses :
            print('Course doest not exists')
        elif   Course(id,'',0,0) in Student.courses:
                print('student have this course')       
        else:
            Course.courses.remove(Course(id,'',0,0))    
           

    @staticmethod
    def print_course():
            print(*Course.courses,sep='\n')

    @staticmethod
    def indexof(id):
        if Course(id,'',1,1) in Course.courses:
            print(Course.courses.index(Course(id,'',1,1)))

    @staticmethod
    def edit_course(course):
        if not isinstance(course,Course):
            print("its not Course")
        elif not course in Course.courses:
            print("item not found")
        else:
            index=Course.courses.index(course)
            Course.courses[index].name=course.name
            Course.courses[index].units=course.units
            Course.courses[index].score=course.score
    


# ///////////////////////////////////////////////////////////////////////////// Student

class Student:
    id = 0
    name = ''
    family = ''
    courses = []
    students = []
    selected_student=None

    def __init__(self, id, name, family,courses) -> None:
        self.id = id
        self.name = name
        self.family = family
        self.courses=courses
    def __eq__(self, other) :
        return   type(self)==type(other) and self.id==other.id 
    def __str__(self) :
        return  'id: {}  name : {} family : {} courses : {}'.format(self.id,self.name,self.family, [i.name for i in  self.courses]) 
    def add_course(self,course):
        if course in self.courses:
            print('course already exists')
        
        else:

            select=Course.courses.index(course)
            # print(Course.courses[select])
            self.courses.append(Course.courses[select]) 
    @staticmethod
    def select_student(id):
        select=Student.students.index(Student(id,'','',[]))
        return Student.students[select]
    @staticmethod
    def print_student():
            print(*Student.students,sep='\n')
    @staticmethod        
    def add_student(student):
        if not isinstance(student,Student):
            print('argument is not a Student object')
        elif student in Student.students:
            print('student already exists')
        
        else:
            Student.students.append(student)
        

    @staticmethod
    def remove_student(id):
        if not isinstance(id,int):
                print('argument should be a int') 
        elif not Student(id,'',0,0)  in Student.students :
            print('Student doest not exists')
        else:
            Student.students.remove(Student(id,'',0,0))

    @staticmethod
    def indexof(id):
        if Student(id,'',0,0) in Student.students:
            print(Student.students.index(Student(id,'',0,0)))
    @staticmethod
    def print_course():
        for i in Course.courses:
            if i not in Student.courses:
                print(i)        

# //////////////////////////////////////////////////////////////////////////////// Teacher
class Teacher():
    id = 0
    name = ''
    family = ''
    courses = []
    teachers = []

    def __init__(self, id, name, family,courses) -> None:
        self.id = id
        self.name = name
        self.family = family
        self.courses=courses
    def __eq__(self, other) :
        return   type(self)==type(other) and self.id==other.id         
    def __str__(self) :
        return  'id: {}  name : {} family:{} courses:{} '.format(self.id,self.name,self.family,self.courses)  
    @staticmethod        
    def print_teacher():
            print(*Teacher.teachers,sep='\n')
    @staticmethod
    def add_teacher(teacher):
        if not isinstance(teacher,Teacher):
            print('argument is not a Teacher object')
        elif teacher in Teacher.teachers:
            print('teacher already exists')
        
        else:
            Teacher.teachers.append(teacher)

    @staticmethod
    def remove_teacher(id):
        if not isinstance(id,int):
                print('argument should be a int') 
        elif not Teacher(id,'',0,0)  in Teacher.teachers :
            print('Teacher doest not exists')
        else:
            Teacher.teachers.remove(Teacher(id,'',0,0))

    def indexof(id):
        if Teacher(id,'',1,1) in Teacher.teachers:
            print(Teacher.teachers.index(Teacher(id,'',0,0)))
# //////////////////////////////////////////////////////////////////// Classroom

class Classroom:
    id = 0
    name = ''
    teacher = None
    course = None
    student = []
    classrooms = []

    def __init__(self, id, name) -> None:
        self.name = name
        self.id = id

    @staticmethod
    def add_classroom(classroom):
        if not isinstance(classroom,Classroom):
                print('argument is not a Classroom object')
        elif classroom in Classroom.classrooms:
            print('classsroom already exists')
        
        else:
            Classroom.classrooms.append(classroom)  

    @staticmethod
    def remove_classroom(id):
        if not isinstance(id,int):
                print('argument should be a int') 
        elif not Classroom(id,'',0,0)  in Classroom.classrooms :
            print('Classroom doest not exists')
        else:
            Classroom.classrooms.remove(Classroom(id,'',0,0)) 

    @staticmethod
    def indexof(id):
        if Classroom(id,'',1,1) in Classroom.classrooms:
            print(Classroom.classrooms.index(Classroom(id,'',0,0)))


j1=open("data.json","rt")
j=j1.read()
s=json.loads(j) 
for i in s["courses"]:
    Course.add_course(Course(i["id"],i["name"],i["units"],0))
    # Course.add_course(Course(i.id,i.name,i.units)) 
   
for student in s["students"]:
    s1=Student(student["id"],student["name"],student["family"],[]) 
    for course  in student["courses"]:
        
        cr=Course.get_course(course["id"])

        cr.score=course["score"]

        s1.add_course(cr)
    Student.add_student(s1)                  
for m in s["teachers"]:
    Teacher.add_teacher(Teacher(m["id"],m["name"],m["family"],m["courses"]))              
level="root"

while True:
    if level=="root":
        print("1-students")
        print("2-teachers")
        print("3-courses")
        print("4-classrooms")
        print("0-exit")
        cmd=int(input())
        if cmd==1:
            level="students"
        elif cmd==2:
            level="teachers"
        elif cmd==3:
            level="courses"
        elif cmd==4:
            level="classrooms"
        elif cmd==0:
            break
    elif level=="students":
        print("1-show students")
        print("2-add student")
        print("3-edit student")
        print("4-delete student")
        print("5-select student")
        print("0-back")
        cmd=int(input())
        if cmd==1:
            Student.print_student()
        elif cmd==2:
            id=int(input("id: "))
            name=input("name: ")
            family=input("family: ")
            Student.add_student(Student(id,name,family,[]))
        elif cmd==3:
            pass
        elif cmd==4:
            id=int(input("id: "))
            Student.remove_student(id)
        elif cmd==5:
            Student.print_student()
            id=int(input("id:"))
            print("1-show info")
            print("2-add course")
            print("3-delete course")
            print("4-set course")
            print("0-back") 
            cmd=int(input()) 
            Student.selected_student=Student.select_student(id)
            if cmd==1:
                print("id: ",Student.selected_student.id)
                print("name: ",Student.selected_student.name)
                print("family: ",Student.selected_student.family)
                print("course: ",Student.selected_student.courses)

            elif cmd==2:
                Student.print_course()
                id=int(input("id:"))
                cr=Course.get_course(id)
                Student.selected_student.add_course(cr)
            elif cmd==3:
                pass
            elif cmd==4:
                pass
            elif cmd==0:
                pass


        elif cmd==0:
            level="root"
    elif level=="teachers":
        print("1-show teachers")
        print("2-add teacher")
        print("3-edit teacher")
        print("4-delete teacher")
        print("5-select teacher")
        print("0-back")
        cmd=int(input())
        if cmd==1:
            Teacher.print_teacher()
        elif cmd==2:
            id=int(input("id: "))
            name=input("name: ")
            family=input("family: ")
            Teacher.add_teacher(Teacher(id,name,family,0))
        elif cmd==3:
            pass
        elif cmd==4:
            id=int(input("id: "))
            Teacher.remove_teacher(id)
        elif cmd==5:
            pass
        elif cmd==0:
            level="root"
    elif level=="courses":
        print("1-show courses")
        print("2-add course")
        print("3-edit course")
        print("4-delete course")
        print("0-back")
        cmd=int(input())
        if cmd==1:
            Course.print_course()
        elif cmd==2:
            id=int(input("id: "))
            name=input("name: ")
            units=int(input("units: "))
            Course.add_course(Course(id,name,units,0))
        elif cmd==3:
            id=int(input("id: "))
            name=input("name: ")
            units=input("units: ")
            Course.edit_course(Course(id,name,units,0))
        elif cmd==4:
            id=int(input("id: "))
            Course.remove_course(id)
        elif cmd==0:
            level="root"
    elif level=="classrooms":
        print("1-show classrooms")
        print("2-add classroom")
        print("3-edit classroom")
        print("4-delete classroom")
        print("5-select classroom")
        print("0-back")
        cmd=int(input())
        if cmd==1:
            pass
        elif cmd==2:
            pass
        elif cmd==3:
            pass
        elif cmd==4:
            pass
        elif cmd==5:
            pass
        elif cmd==0:
            level="root"       
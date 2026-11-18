from grade import get_grade

student_file = "student.txt"

#data student
def load() :
    students = {}
    
    try :
         with open(student_file , "r") as file :
            for line in file :
                if line.strip() == "" :
                    continue
                student_names , score = line.strip().split(",")
                students[student_names] = int(score)
    except FileNotFoundError :
        pass
    
    return students

 
def save(students) :
    #file 
    with open(student_file, "w") as file :
        for student_names, score in students.items() :
            file.write(f"{student_names}, {score}\n")
                 
      
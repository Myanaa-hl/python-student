from time import sleep

#Grade
def get_grade(score) :
    if score >= 90 :
        return "A"
    elif score >= 80 :
        return "B"
    elif score >= 70 :
        return "C"
    elif score >= 60 :
        return "D"
    elif score < 60 : 
        return "E"
    
def ending() :
    sleep(1)
    print("...")
    sleep(1)
    print("Goodbye")
    sleep(1)
    print("...")
def calculate_avg(average):
    if average >=90:
        return "A"  
    elif average >=80:
        return "B"
    elif average >=70:
        return "C"  
    elif average >=60:
        return "D"
    else: 
        return "F"
    
def main():
    name=input("Enter your name: ")
    class_name=input("Enter your class name: ")
    subject=int(input("Enter the number of subjects: "))
    total = 0
    subjects = {}

    for i in range(subject):
        subject_name=input(f"Enter the name of subject {i+1}: ")
        marks=float(input(f"Enter the marks obtained in {subject_name}: "))
        subjects[subject_name] = marks
        total += marks

    average = total / subject
    grade = calculate_avg(average)

    print (f"Student Name: {name}")
    print (f"Class Name: {class_name}") 
    print (f"Average Score: {average}")
    print (f"Grade: {grade}") 

if __name__ == "__main__":
    main()
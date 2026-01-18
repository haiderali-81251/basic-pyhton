def percent(obt,total):
    percentage=(obt/total)*100
    print(f"Percentage : {percentage:.2f}%")
    return round(percentage, 2)

def grade(percentage):
    if (percentage>=80 and percentage<=100):
        print("Grade : A+")
    elif (percentage>=70 and percentage<80):
        print("Grade : A")
    elif (percentage>=60 and percentage<70):
        print("Grade : B")
    elif (percentage>=50 and percentage<60):
        print("Grade : C")
    elif (percentage>=40 and percentage<50):
        print("Grade : D")
    else:
        print("You failed!")

student = []
n=int(input("Enter no of students: "))

print("----------------------------------------------")

for i in range(n):
    
    print(f"\nEnter details for student {i+1}:")
    name=str(input("Enter student's name :"))
    
    marks_maths=int(input("Enter marks of maths: "))
    marks_physics=int(input("Enter marks of Physics: "))
    marks_cs=int(input("Enter marks of CS: "))
    marks_chemistry=int(input("Enter marks of Chemistry: "))

    obtained_marks= (marks_cs + marks_chemistry + marks_maths + marks_physics)
    total_marks=400

    Percentage=percent(obtained_marks,total_marks)

    grade(Percentage)

    student.append((name,Percentage))
    print("-----------------------------------------------------")

student.sort(key=lambda x : x[1])

print(f"1st position goes to {student[-1][0]} at {student[-1][1]}%")
print(f"2nd position goes to {student[-2][0]} at {student[-2][1]}%")
print(f"3rd position goes to {student[-3][0]} at {student[-3][1]}%")

print("--------------------------------------------------------")






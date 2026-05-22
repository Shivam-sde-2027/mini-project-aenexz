def analyze_result(name,roll,marks):
    total=sum(marks)
    average=total/len(marks)

    if average>=90:
        grade="A"
    elif average>=75:
        grade="B"
    elif average>=60:
        grade="C"
    elif average>=40:
        grade="D"
    else:
        grade="Fail" 

    print(f"\nStudent: {name} (Roll: {roll})")
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Grade: {grade}")

    failed_subjects=[]
    for i in range(len(marks)):
        if marks[i]<40:
            failed_subjects.append(f"subject {i+1}")

    if failed_subjects:
        print("Subject below 40:",", ".join(failed_subjects))
    else:
        print("No subjects below 40!")

name=input("Enter student name: ")
roll=int(input("Enter student roll number: "))

marks=[]
for i in range(5):
    mark=float(input(f"Enter marks of subject {i+1}: "))
    marks.append(mark)

analyze_result(name,roll,marks)
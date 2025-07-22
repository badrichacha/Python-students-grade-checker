marks = int(input("Enter the marks of student:"))
if(marks > 90):
    Grade = "A+"
elif(marks >=80 and  marks <90 ):
    Grade = "A"
elif(marks >=70 and marks < 80):
    Grade = "B"
elif(marks >=60 and marks < 70):
    Grade = "C"
else:
    Grade = "Failed"
print("The grade of the student is ",Grade)

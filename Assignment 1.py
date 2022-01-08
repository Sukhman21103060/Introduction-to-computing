#Assignment1
#Name:Sukhmanpreet Singh
#S.ID:21103060
# Question 1
A=int(input("Enter first number:"))
B=int(input("Enter second number:"))
C=int(input("Enter third number:"))
Average=(A+B+C)/3
print("The average of three numbers is :",Average)



# Question 2
#All values are in $s
Standard_deduction=10000
Dependent_deduction=3000
#There is a $3000 deduction for each dependents
Gross_income=int(input("enter your gross income to the nearest penny:"))
Number_of_dependents=int(input("Enter your number of dependents:"))
Taxable_income=(Gross_income-Standard_deduction-(Dependent_deduction*Number_of_dependents))
print("Taxable income:",Taxable_income)
#tax rate=20% so, Taxable_income will be multiply by 0.2
Tax=Taxable_income*0.2
print("Your Income Tax is :",Tax)





# Question 3
SID=int(input("Enter your SID:"))
Name=input("Enter your name:")
Gender=input("Enter your Gender: ")
Course_name=input("Enter your course name:")
CGPA=float(input("Enter your CGPA:"))
data=['Name','SID','Gender','Course name','Cgpa']
print(data)
#we name our list as STUDENT_INFORMATION
STUDENT_INFORMATION=[SID,Name,Gender,Course_name,CGPA]
print(STUDENT_INFORMATION)



#question 4
student_1marks=int(input("Enter student 1 marks: "))
student_2marks=int(input("Enter student 2 marks: "))
student_3marks=int(input("Enter student 3 marks: "))
student_4marks=int(input("Enter student 4 marks: "))
student_5marks=int(input("Enter student 5 marks: "))

my_list=[student_1marks,student_2marks,student_3marks,student_4marks,student_5marks]
print("List: ",my_list)
my_list.sort()
print("sorted list",my_list)


  
# Question 5
colour=['Red','Green','White','Black','Pink','Yellow']
print("List:",colour)
colour.remove(colour[3])
# remove 4th term that is black
print("Part A of question 5: ",colour)
colour=['Red','Green','White','Black','Pink','Yellow']
print("List:",colour)
#replace black and pink with purple
# to replace nth term we write {my_list[n-1]='new value'}
colour[3:5]=['Purple']
print("Part B of question 5:",colour)


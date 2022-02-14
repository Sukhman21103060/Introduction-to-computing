#SOLUTION 1
print("SOLUTION 1")
a=str(input("ENTER STRING: "))
list=a.split() #To split all the elements of string in a list
dict={} #initializing an empty dictionary
if list.__len__()==1:   #if statement will be implemented when a single word is entered
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
else:                   #else statement will be implemented when more than one word is entered in a string
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")




#SOLUTION 2
print("SOLUTION 2")
def Next_Date():
    list1=[1,3,5,7,8]
    list2=[4,6,9,11]
    list3=[2]
    list4=[12]
    while(True):                 #while loop is used so that if any wrong value is entered  then values will be entered again
        day=int(input("ENTER THE DAY: "))
        if(1<=day<=31):
            break
        else:
            print("Please Enter a valid day")
    while(True):                  #while loop is used so that if any wrong value is entered  then values will be entered again
        month=int(input("ENTER THE MONTH OF THE YEAR: "))
        if(1<=month<=12):
            break
        else:
            print("Please Enter a valid month")
    while(True):                #while loop is used so that if any wrong value is entered  then values will be entered again
        year=int(input("ENTER THE YEAR: "))
        if(1800<=year<=2025):
            break
        else:
            print("Please Enter year from 1800 to 2025 only")
    if month in list1 :    
        if(day==31):
            day=1
            month=month+1
            print("NEXT DATE IS: ",day,"/",month,"/",year)
        elif(day<31):
            day+=1
            print("NEXT DATE IS: ",day,"/",month,"/",year)
        else:
            print("INVALID DATE TRY AGAIN")
            Next_Date()
    
    elif month in list2 :
        if(day==30):
            day=1
            month=month+1  
            print("NEXT DATE IS: ",day,"/",month,"/",year)   
        elif(day<30):
            day+=1
            print("NEXT DATE IS: ",day,"/",month,"/",year)
        else:
            print("INVALID DATE TRY AGAIN") 
            Next_Date()      
    elif month in list3:
        if(year % 4 == 0):  
            if(day==29):
                day=1
                month=month+1
                print("NEXT DATE IS: ",day,"/",month,"/",year)
            elif(day<29):
                day+=1
                print("NEXT DATE IS: ",day,"/",month,"/",year)
            else:
                print("INVALID DATE TRY AGAIN")
                Next_Date()
        else:
            if(day==28):
                day=1
                month+=1
                print("NEXT DATE IS: ",day,"/",month,"/",year)
            elif(day<28):
                day+=1
                print("NEXT DATE IS: ",day,"/",month,"/",year)
            else:
                print("INVALID DATE TRY AGAIN")
                Next_Date()
    elif month in list4:
        if(day==31):
            day=1
            month=1
            year+=1  
            print("NEXT DATE IS: ",day,"/",month,"/",year)
        elif(day<31):
            day+=1;
            print("NEXT DATE IS: ",day,"/",month,"/",year)
        else:
            print("INVALID DATE TRY AGAIN")
            Next_Date()
        
    else:
        print("INVALID DATE TRY AGAIN")
        Next_Date()
Next_Date()
print("\n")



#SOLUTION 3
print("SOLUTION 3")
input_list = input('Enter list separate its  elements by space ')
user_list = input_list.split()
# print list
print('List: ', input_list)

for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])
squarelist =[(user_list[i], user_list[i]**2)for i in range(len(user_list))]

print("Square List:",squarelist)

print("\n")



#SOLUTION 4
print("SOLUTION 4")

def input_gradePoint():
    gradePoint = int(input("Enter Your Grade Point: "))
    # check if the grade point meets the conditions
    if gradePoint>10 or gradePoint<4:
        print("Invalid grade point! Try Again")
        gradePoint = input_gradePoint()
    return gradePoint
grade=input_gradePoint()
if(grade==4):
    print("Your Grade is 'D' and poor performance")
elif(grade==5):
    print("Your Grade is 'C' and Below Average performance")
elif(grade==6):
    print("Your Grade is 'C+' and Average performance")
elif(grade==7):
    print("Your Grade is 'B' and Good performance")
elif(grade==8):
    print("Your Grade is 'B+' and Very Good performance")
elif(grade==9):
    print("Your Grade is 'A' and Excellent performance")
else:
    print("Your Grade is 'A+' and outstanding performance")
print("\n")


#SOLUTION 5
print("SOLUTION 5")
x = 6
for i in range(x):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2*(x-i)-1):
        print(chr(65 + j), end='')  #ASCII VALUE OF A=65,B=66,C=67,D=68,E=69,F=70,G=71,H=72,I=73,J=74,K=75
    print()
print("\n")


#SOLUTION 6
print("SOLUTION 6")
sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {sid:name}

while True:
    option = input("Do you want to add another student entry(Y or N):").upper()
    if option == 'Y':
        sid = int(input("Enter different SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif option == 'N':
        break
    else:
        print('Invalid input!')

#part a. print the dictionary
print("<a> Student Details",students)

#part b. sort acc to the names
print("<b> Sorted Dictionary According To Student Name :",{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

#part c. sort acc to the SIDs
print("<c> Sorted Dictionary According To Student SID :",{k:v for k,v in sorted(students.items())})

#part d. search for a student by their SID
while True:
    sid = int(input("Search Name with help of SID: "))
    if sid in students:
        print("<d> Name Of The Student Is :",students[sid])
        break
    else:
        print(" Wrong Sid Please Check Again")
        
    


#SOLUTION 7
print("SOLUTION 7")
#  Function to display the Fibonacci sequence
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
no_of_terms=int(input("ENTER THE NUMBER OF TERMS IN THE SERIES: "))
if no_of_terms <= 0:     # Check if the number of terms is valid
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   sum=0
   for i in range(no_of_terms):
       print(recur_fibo(i))
       sum=sum+recur_fibo(i)
avg=float(sum/no_of_terms)
print("AVERAGE OF RESULTANT FIBONACCI SERIES IS",avg)


#SOLUTION 8
print("\n\nSOLUTION 8.")

set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}

# part a.
print("a.",(set1|set2)-(set1&set2))
# part b(Subtracting intersection of sets taken two at a time from the Union of all three sets)
print("b.",(set1|set2|set3)-((set1&set2)|(set1&set3)|(set3&set2)))
# part c(Subtracting the intersection of all three sets from the Intersection of sets taken two at a time)
print("c.",((set1&set2)|(set1&set3)|(set3&set2))-(set1&set2&set3))
# part d(Excluding the numbers from 1 to 10 that are occuring in Set1)
set10 = {1,2,3,4,5,6,7,8,9,10}
print("d.",set10-set1)
# part e(Excluding the numbers from 1 to 10 that are occuring in Set1, Set2 and Set3)
print("e.",set10-(set1|set2|set3))


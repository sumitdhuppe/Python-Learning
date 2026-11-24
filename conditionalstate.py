#if statement
age =21
if(age>=18):
    print("can vote")

#if elif conditional statement
colour="yellow"
if(colour=="red"):
    print("stop")
elif(colour=="green"):
    print("go")
elif(colour=="yellow"):
    print("look")
print("end the code")

#if elif else conditional statement
light="blue"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
else:
    print("light is broken")
print("end the code")


marks=67

if(marks>=90 ):
    grade = "A"
elif(marks>=80 and marks<90):
    grade = "B"
elif(marks>=70 and marks<80):
    grade = "C"
else:
    grade = "D"
print("grade of student =",grade)
print("end the code")

#practice questions
num=int(input("enter the number:-"))

if(num%2==0):
    print("number is even")
else:
    print("number is odd")

#wap to find the largest no.
num1=int(input("enter the first num:-"))
num2=int(input("enter the second num:-"))
num3=int(input("enter the third num:-"))
if(num1>=num2 and num1>=num3):
    print("num1 is largest number",num1)
elif(num2>=num1 and num2>=num3):
    print("num2 is largest number",num2)
else:
    print("num3 is largest number",num3)

#wap to check if a number is multiple of 7
num=int(input("enter the num:-"))
if(num%7==0):
    print("the number is multipe of 7")
else:
    print("the num is not multiple of 7")
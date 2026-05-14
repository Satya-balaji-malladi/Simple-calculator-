#simple calculator
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print("1---addition\n2---subtraction\n3---division\n4---multiplication")
choice=int(input("enter your choice:"))
if(choice==1):
    sum=num1+num2
    print(sum)
elif(choice==2):
    difference=num1-num2
    print(difference)
elif(choice==3):
    if(num2==0):
        print("Cannot be Divisble By 0")
    else:
        division=num1/num2
        print(division)
elif(choice==4):
    multiply=num1*num2
    print(multiply)
else:
    print("invalid input")

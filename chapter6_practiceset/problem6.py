marks=int(input("enter the number : "))

if(marks==100 and marks>90):
    print("exceptional")
elif(marks>80 and marks==90):
    print("a grade")
elif(marks==80 and marks>70):
    print("b grade")
elif(marks==70 and marks>60):
    print("c grade")
elif(marks==60 and marks>50):
    print("d grade")
elif(marks<50):
    print("f grade")


import cmath

#problem 1

a=10
if (a%2==0):
    print("a is even number")
else:
    print("a is odd number")

#problem 2 

b='W'

if(b=="a" or "e" or "i" or "o" or "u"):
    print("b is vowel")

else:
    print("b is a consonant")


#problem 3 

num1 = int(input())
num2 = int(input())
num3 = int(input())

if(num1>num2):
    if(num1>num3):
        print("num1 is greater")
    else:
        print("num3 is greater")
else:
    if(num2>num3):
        print("num2 is greater")
    else:
        print("num3 is greater")

#problem 4 

a=int(input())
b=int(input())
c=int(input())

discriminent=b**2-4*a*c

if(discriminent>0):
    print("two different roots : ")
    x1=-b+cmath.sqrt(discriminent)/2*a
    x2=-b-cmath.sqrt(discriminent)/2*a
    print(x1)
    print(x2)
elif(discriminent==0):
    print("same roots : ")
    x1=-b/2*a
    print(x1)
elif(discriminent<0):
    print("one imaginary and one real roots : ")
    x1=-b/2*a
    x2=cmath.sqrt(-discriminent)/2*a
    print("the real part is : ",x1)
    print("the imaginary part is : ",x2)

#problem 5 

year=int(input())

if(year%4==0 and year%100!=0 or year%400==0):
    print("the year is leap year")
else:
    print("year is not leap year")

    


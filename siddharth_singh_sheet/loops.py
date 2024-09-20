#problem 1 

n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i

print(sum)

#problem 2 

fact=1
n1=int(input())

for i in range(2,n+1):
    fact=fact*i

print(fact)

#problem 3
n2=int(input())
for i in range(1,n2):
    print(f"{n2} * {i} = {n2*i}")

#problem 4 

a = 0
b = 1

value = int(input("Enter the position of the Fibonacci number to find: "))

if value <= 0:
    print("Please enter a positive integer.")
elif value==1:
    print(a)
    
elif value==2:
    print(b)
else:
    for i in range(3, value+1):  # Start from 2 because we already have the first two numbers
        c = a + b
        a = b
        b = c
    print(b)  # This will print the Fibonacci number at the given position


#problem 5

number= int(input())

if(number<=0):
    print("enter the valid input")
else:
    a=0
    b=1
    while a<=number:
        print(a,end=",")
        a,b=b,a+b

#problem 6 
#finding the gcd 
#logic : a,b=b,a%b   this will make the value b to zero and then left with the values a and then printing a

a=int(input())
b=int(input())

while (b!=0):
    a,b=b,a%b

print(a)

#u can use the above or below logic for gcd
a=int(input())
b=int(input())

while(a!=b):
    if(a>b):
        a-=b
    else:
        b-=a

#problem 7
#finding the lcm 
#logic  (a*b)/gcd

def gcd(a,b):
    while(b!=0):
        a,b=b,a%b
    return a

def lcm(a,b):
    return (a*b)//gcd(a,b)

num1=int(input())
num2=int(input())

lcm(num1,num2)

#problem 8 
number = int(input())

reversed_num=0

while(number!=0):
    remainder = number %10
    reversed_num= reversed_num*10 + remainder
    number = number//10

print(reversed_num)


#problem 9 

sumnumber=0
number=int(input())
while(number!=0):
    remainder=number%10
    sumnumber=sumnumber+remainder
    number=number//10

print(sumnumber)


#problem 10 

base=int(input())
power=int(input())

power_number=pow(base,power)
print(power_number)

#problem 11

base=int(input())
power=int(input())

# power_number=base**power
# print(power_number)

# or

result=1
while(power!=0):
    result=result*base
    power-=1

print(result)

#problem 12

number =int(input())

num_str=str(number)

if(num_str==num_str[::-1]):
    print("yes it is palindrome number")
else:
    print("it is not palindrome number")


#problem 13 

number = int(input())

for i in range(2,number):
    if(number%i==0):
        print("it is not prime number")
        break
else:
    print("it is prime number")

#problem 14 

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Get two numbers from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Prime numbers between {start} and {end} are:")

# Loop through the range and check for prime numbers
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")

#problem 15
##armstrong number is cube of sum of numbers

number= int(input())

value=0
while(number!=0):
    
    remainder=number%10
    
    value=value+remainder**3
    
    number=number//10

print(value)


#problem 16
number = int(input())

for i in range(1,number+1):
    if (number%i==0):
        print(f"{i} is the factor of the number {number}")
        


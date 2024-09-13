#checking the prime number or not 
num=int(input())

for i in range(2,num):
    if(num%i==0):
        print("this is not prime number")
        break
else:
    print("this is prime number")


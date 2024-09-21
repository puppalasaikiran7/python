#pattern 1 
number=int(input("enter the number : "))
number1=int(input("enter the number1 : "))
for i in range(number):
    for j in range(number1):
        print("*",end=" ")
    print()

#pattern 2
a=int(input("enter the value a : "))
b=int(input("enter the value b : "))

for i in range(a):
    for j in range(b):
        if(i==0 or i==a-1 or j==0 or j==b-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()


#problem 3
number=int(input("enter the number : "))

for i in range(number+1):
    for j in range(i):
        print("*",end=" ")
    print()

#problem 4
number=int(input("enter the number : "))

for i in range(number,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()


#problem 5 
def print_pyramid(n):
    
    for i in range(1, n + 1):
        
        print(' ' * (n - i), end='')
        
        print('* ' * i)


rows = int(input("Enter the number of rows: "))
print_pyramid(rows)

#problem 6
def print_pyramid(n):
    
    for i in range(n ,0,-1):
        print('* ' * i)
        print(' ' * (n - i), end=' ')


rows = int(input("Enter the number of rows: "))
print_pyramid(rows)

#problem 7
n=int(input())

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,2*i):
        if (i==n or k==1 or k==(2*i)-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()

#problem 8 
n=int(input())

for i in range(n):
    for j in range(1,i+1):
        print(j,end="")
    print()

#problem 9 
def print_pascals_triangle(rows):
    # Loop to handle the number of rows
    for i in range(rows):
        coef = 1  # Starting coefficient
        # Print leading spaces
        for space in range(1, rows - i):
            print(" ", end="")

        # Loop to print the values in each row
        for j in range(i + 1):
            if j == 0 or i == 0:
                coef = 1  # First element is always 1
            else:
                # Compute value based on the previous row's values
                coef = coef * (i - j + 1) // j
            print(coef, end=" ")

        print("\n")  # Move to the next line after each row

# Input for number of rows
rows = int(input("Enter the number of rows: "))
print_pascals_triangle(rows)

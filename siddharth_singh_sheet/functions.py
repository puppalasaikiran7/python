#question 1 
def prime(n):
    for i  in range(2,n):
        if(n%i==0):
            print("this is not prime number")
            break
    else:
        print("it is prime number")


n=int(input())
prime(n)

#question 2 
# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to find and print all prime pairs
def find_prime_pairs(n):
    
    # Check every number from 2 to n//2
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            print(f"{n} = {i} + {n - i}")
            
    

# Main program
n = int(input("Enter a positive integer: "))
find_prime_pairs(n)

#problem 3
def binary_decimal(binary):
    i=0
    decimal=0
    while(binary!=0):
        value=binary%10
        decimal=decimal+value*(2**i)
        binary=binary//10
        i=i+1
    return decimal




binary=int(input())
decimal= binary_decimal(binary)
print(decimal)

#problem 4 
# Function to convert decimal to binary
def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        remainder = decimal % 2  # Get the remainder (0 or 1)
        binary = str(remainder) + binary  # Prepend the remainder to the binary string
        decimal //= 2  # Divide the decimal by 2
    return binary if binary else '0'  # If the decimal was 0, return '0'

# Main code
decimal = int(input("Enter a decimal number: "))

binary = decimal_to_binary(decimal)
print(f"The binary equivalent is: {binary}")

#Problem 1
def sum_n_natural_numbers(number):
    if number==0:
        return 0
    else:
        value=number+sum_n_natural_numbers(number-1)
        return value
    

number=int(input())
print(sum_n_natural_numbers(number))


#problem 2 
def fact(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        value= num * fact(num-1)
        return value
    
    
    
    
num=int(input())
print(fact(num))

#problem 3 
def gcd(a,b):
    if b==0:
        return a 
    else:
        return gcd(b,a%b)
    
a=int(input())
b=int(input())
print(gcd(a,b))

#problem 4 
def power(base,expo):
    
    if expo==0:
        return 1
        
    else:
        return base * power(base,expo-1)
    
    
    
base=int(input())
expo=int(input())
print(power(base,expo))
    
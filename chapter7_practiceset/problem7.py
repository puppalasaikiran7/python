n=int(input())

for i in range(n+1):
    for k in range(n-i):
        print(end=" ")
    for j in range(i):
        if(i%2!=0):
            print("*",end=" ")
    print()
    
    

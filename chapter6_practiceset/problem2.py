sub1=int(input("enter the marks of sub1 : "))
sub2=int(input("enter the marks of sub2 : "))
sub3=int(input("enter the marks of sub3 : "))


percentage=((sub1+sub2+sub3)/300)*100

if(percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print(f"you have passed the exam now chill out , your percentage is {percentage}")

else:
    print(f"you have failed the exam ,{percentage}")

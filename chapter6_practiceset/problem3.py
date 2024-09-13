string=input()
list=["make a lot of money" , "buy now" , "subscribe" , "click this"]


# one way of doing this is 
if (phrase in string for phrase in list):
    print("the text is a spam ")

else:
    print("this is a genune text")

#another way of doing this is 
p1="make a lot of money "
p2="buy now"
p3="subscribe"
p4="click now"

string1=input()

if(p1 in string1 or p2 in string1 or p3 in string1 or p4 in string1):
    print("this is a spam text")

else:
    print("this is a genuene text")
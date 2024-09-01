# sorting the list 
g=["ganesh","shiva","eristotle","ananadhi","bosh"]

g.sort()

print("sort : ",g)

#reverse the list 
h=["ganesh","shiva","eristotle","ananadhi","bosh"]

h.reverse()

print("reverse : ",h)


# index 
e=["apple",3,456.57,False]

print("index : ",e.index(3))


#count 
c=["apple",3,456.57,False,3]

print("count : ",c.count(3))


# inserting the elements in the list  ( append , insert , extend )

#append  ( adding element from the last )
a=["apple",3,456.57,False]

a.append("banana")

print("append : ",a)


# insert ( adding element in the specific position)
k=["apple",3,456.57,False]

k.insert(1,9)  # the first one is the position of the element and second one is the element that is inserted

print("insert : ",k)

#extend ( adding bunch of elements in the form of list , tuple , etc from the last)
l=["apple",3,456.57,False]

l.extend([True,34.23])

print("extend : ",l)


# deleting the elemets from the list  ( remove, pop , del)

#remove
t=["apple",3,456.57,False]

t.remove("apple")   # removing the element of the respective value

print("remove : ",t)

# pop 
u=["apple",3,456.57,False]

u.pop(1)  # removing the element of the respective index

print("pop : ",u)


# clear 
o=["apple",3,456.57,False]

o.clear()

print("clear : ",o)
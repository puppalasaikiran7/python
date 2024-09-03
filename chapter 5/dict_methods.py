# dictionaty methods 

marks={
    "harry":100,
    "shubam":90,
}

# items ( means all the data in dictionary)
print(marks.items())


# value ( means all that is assigned )
print(marks.values())


# key ( means variable type )
print(marks.keys())


#update
marks.update({"hemanth":90 ,"vishnu":50})
print(marks)


#get ( return the value of the specific key ) ( prints none is the key is not present in the dictionary )
print(marks.get("hemanth"))

#copy ( does a shallow copy )
new_dict=marks.copy()
print(new_dict)


#pop ( removes specific item from the dictionary based on the key given )
marks.pop("hemanth")
print(marks)


#clear ( clears all the values and keys )
marks.clear()
print(marks)
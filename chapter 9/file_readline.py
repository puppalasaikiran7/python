f=open("D:\learning\python\chapter 9\poem.txt")

# data1=f.readline()   ### reads theone single line at a time
# data2=f.readline()
# data3=f.readline()
# data4=f.readline()

# print(data1)
# print(data2)
# print(data3)
# print(data4)
# print(type(data1))

data=f.readlines()  ### reads the lines and returns them as list 

print(data)


f.close()
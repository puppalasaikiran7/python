word="donkey"

with open("D:\learning\python\chapter9_practiceset/file.txt") as f:
    content=f.read()

contentnew = content.replace(word,"######")

with open("D:\learning\python\chapter9_practiceset/file.txt",'w') as f:
    f.write(contentnew)
with open("D:\learning\python\chapter9_practiceset/this.txt") as f:
    content=f.read()

with open("D:\learning\python\chapter9_practiceset/this_copy.txt",'w') as f:
    f.write(content)
with open("D:\learning\python\chapter9_practiceset/log.txt") as f:
    lines=f.readlines()


lineno=1
for line in lines:
    if "python" in line:
        print(f"python is present in the lines{lineno}")
    lineno+=1



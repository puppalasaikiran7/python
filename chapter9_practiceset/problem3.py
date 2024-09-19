def generatetable(i):
    with open(f"D:\learning\python\chapter9_practiceset/tables/table{i}.txt","w") as f:

        for j in range(1,11):
            f.write(f"{i} * {j} = {i*j}\n")

for i in range(2,21):
    generatetable(i)
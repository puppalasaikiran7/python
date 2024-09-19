with open("D:\learning\python\chapter9_practiceset/log.txt") as f:
    content=f.read()

if "python" in content:
    print("yes python present in file")
else:
    print("no python is not present in content")    
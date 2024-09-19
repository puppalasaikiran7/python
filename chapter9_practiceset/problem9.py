with open("D:\learning\python\chapter9_practiceset/this.txt") as f:
    content1=f.read()

with open("D:\learning\python\chapter9_practiceset/this_copy.txt") as f:
    content2=f.read()

if (content1==content2):
    print("both the contents are same they are identical")
else:
    print("no the files are not identical ")
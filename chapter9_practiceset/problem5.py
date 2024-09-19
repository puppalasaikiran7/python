word=["donkey","bad","gandha"]

with open("D:\learning\python\chapter9_practiceset/file.txt") as f:
    content=f.read()

for words in word:
    content = content.replace(words,"#" * len(words))

with open("D:\learning\python\chapter9_practiceset/file.txt",'w') as f:
    f.write(content)
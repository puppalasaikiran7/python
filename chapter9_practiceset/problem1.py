with open("D:\learning\python\chapter9_practiceset/poem.txt") as f:
    content=f.read()
    print(content)

    print()
    
    word="Twinkle"
    if word in content:
        print("yes it is present")
    else:
        print("the word is not present in the content")
    



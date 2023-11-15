with open("test1.txt", "r+") as file1:
    file1.truncate(10)
    word = file1.read()
    print("WORD:", word)

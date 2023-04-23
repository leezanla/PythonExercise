with open("a.txt", "r", encoding="utf-8") as file1:
    with open("b.txt", "r", encoding="utf-8") as file2:
        with open("d.txt", "w", encoding="utf-8") as file3:
            file3.write(file1.readline().strip("\n") + file2.readline().strip("\n") + "\n")































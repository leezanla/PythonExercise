file1 = open("a.txt", "r", encoding="utf-8")
file2 = open("b.txt", "r", encoding="utf-8")
file3 = open("c.txt", "a+", encoding="utf-8")

for a in file1.readlines():
    for b in file2.readlines():
        file3.write(a.strip("\n") + b)
    file3.write("\n")
    file2.seek(0)

file1.close()
file2.close()
file3.close()































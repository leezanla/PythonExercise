while True:
    score = float(input("请输入该学生的成绩\n"))
    if score > 90:
        print("该学生的成绩为A")
    elif score >= 80:
        print("该学生的成绩为B")
    elif score >= 70:
        print("该学生的成绩为C")
    else:
        print("该学生的成绩为D")


"""def Check_grade():
    if (score >= 0) and (score <= 100):
        if (score >= 80) and (score < 100):
            grade = "A"
        elif (score >= 75) and (score < 80):
            grade = "B+"
        elif (score >= 70) and (score < 75):
            grade = "B"
        elif (score >= 65) and (score < 70):
            grade = "C+"
        elif (score >= 60) and (score < 65):
            grade = "C"
        elif (score >= 55) and (score < 60):
            grade = "D+"
        elif (score >= 50) and (score < 55):
            grade = "D"
        else:
            grade = "F"
    else:
        grade = "I"
"""
from statistics import mean
x = []
total = []
grade = str
while True:
    score = float(input("Input your score : "))
    total.append(score)
    if (score >= 0) and (score <= 100):
        if (score >= 80) and (score < 100):
            grade = "A"
        elif (score >= 75) and (score < 80):
            grade = "B+"
        elif (score >= 70) and (score < 75):
            grade = "B"
        elif (score >= 65) and (score < 70):
            grade = "C+"
        elif (score >= 60) and (score < 65):
            grade = "C"
        elif (score >= 55) and (score < 60):
            grade = "D+"
        elif (score >= 50) and (score < 55):
            grade = "D"
        else:
            grade = "F"
    else:
        grade = "I"
    x.append(grade)
    x.pop
    total.pop
    if (score == -1):
        break
total = mean(total)

print("Your class grade is : {}".format(x))
print("Your class average is : {:.2f}".format(total))
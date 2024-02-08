l = []
sum_grade = 0
lec_grade = 0
grade = 0
answer = 0

dict = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0,
}

for _ in range(20) :
    l.append(input().split(" "))

for i in l :
    if i[2] == 'P':
        continue
    else :
        lec_grade = dict[i[2]]
    grade = float(i[1])
    sum_grade += grade
    answer += grade * lec_grade

print("%.6f" % (answer / sum_grade))

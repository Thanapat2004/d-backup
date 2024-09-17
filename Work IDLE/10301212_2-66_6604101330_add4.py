
student = int (input())
student_score = { }
for i in range(student):
    student_data = input().split()
    student_name = student_data[0]
    score = list(map(float, student_data[1: ]))
    student_score [student_name] = score
name_avg = input()
max = max(student_score[name_avg]) 
min = min(student_score[name_avg]) 
print("%d"%(max),("%d"%(min)))

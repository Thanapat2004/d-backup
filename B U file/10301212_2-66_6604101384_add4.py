"""
   problemname : add3
   filename :  10301212_2-66_6604101384_add3
"""
student = int (input())
student_score = { }
for i in range(student):
    student_data = input().split()
    student_name = student_data[0]
    score = list(map(float, student_data[1: ]))
    student_score [student_name] = score
name_avg = input()
avg = sum(student_score[name_avg]) / len(student_score[name_avg])
print("%.2f"%(avg))

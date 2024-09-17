"""
   problemname : add7
   filename :  10301212_2-66_6604101330_Lucky_man
"""
n, lucky_number = input().split()
n = int(n)

lottery_numbers = [input() for _ in range(n)]

lucky_students = [index + 1 for index, number in enumerate(lottery_numbers)
                  if number == lucky_number]

if lucky_students:
    for student in lucky_students:
        print(student)
else:
    print("No")

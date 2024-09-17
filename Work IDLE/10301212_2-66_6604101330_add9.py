"""
   problemname : add9
   filename :  10301212_2-66_6604101330_Histogram(histogram)
"""
#code ของอาจาร์ย
n = int(input())
input_lst = [ ]
for i in range(n):
    input_lst.append(int(input()))
for i in range(0, 21):
    print("%s:%s" %(i, "*" *input_lst.count (i) ))

##n = int(input())
##numbers = [int(input()) for count_number in range(n)]
##
##for i in range(21):
##    count = numbers.count(i)
##    print(f"{i}:{'*'*count}")

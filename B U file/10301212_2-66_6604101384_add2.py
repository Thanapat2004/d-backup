"""
   problemname : add2
   filename :  10301212_2-66_6604101384_add2   
"""
n = int(input())
number_list = [ ]

for i in range (n):
    num = float(input())
    number_list.append(num)
    
lenght = len(number_list)    
result  = sum(number_list)
avg = result/lenght
print(lenght, ("%.1f" %(result)), ("%.1f" %(avg) ) )


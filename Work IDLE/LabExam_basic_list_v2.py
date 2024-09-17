import numpy as np
n = int(input())
number_list = [ ]

for i in range (n):
    num = float(input())
    number_list.append(num)
    
lenght = len(number_list)    
result  = sum(number_list)
avg = result/lenght
v = np.std(number_list)
print( ("%.1f" %(avg) ), ("%.1f"%(v)) )
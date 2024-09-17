"""
   problemname : add10
   filename :  10301212_2-66_6604101330_(funnyclock)
"""
def time_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

time1 = input().split()  
time2 = input().split()  

time1_seconds = time_to_seconds(int(time1[0]), int(time1[1]), int(time1[2]))
time2_seconds = time_to_seconds(int(time2[0]), int(time2[1]), int(time2[2]))

time_difference = abs(time1_seconds - time2_seconds)
print(time_difference)



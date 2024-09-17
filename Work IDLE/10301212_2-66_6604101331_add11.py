"""
   problemname : add11
   filename :  10301212_2-66_6604101331_(DateTimeOfPost)
"""
import datetime
T = int(input())
for i in range(T):
    t1 = datetime.datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
    delta = abs(t1 - t2)
    seconds = delta.total_seconds()
    print(int(seconds))

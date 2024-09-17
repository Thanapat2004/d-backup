"""
   problemname : add8
   filename :  10301212_2-66_6604101330_Count_Unique_Word
"""
n = int(input())  
word_count = {}   
for _ in range(n):
    word = input().strip()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(len(word_count))  
for count in word_count.values():
    print(count, end=' ')

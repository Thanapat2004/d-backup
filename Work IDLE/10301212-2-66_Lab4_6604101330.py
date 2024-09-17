""" docstring documentation string 3 duble  quote
block of comment
##type("Hello Sack")
##<class 'str'>
##type(500)
##<class 'int'>
##type(550.50)
##<class 'float'>
###funtion ที่เกี่ยวข้องกับการเเปลงชนิดข้อมูล
##str(5)
##'5'
"""
##กด save และตั้งชื่อไฟล์ .py ดังนี้
##10301212-2-66_Lab4_รหัสนักศึกษา.py
##การเขียน function ต้องมีการประกาศ function
##define function
'''
def square() : #Funcion Header หัวฟังก์ชัน
    new_value = 4**2 #Function Body ตัวฟังก์ชัน
    print(new_value)

square()  #call function การเรียกใช้ฟังก์ชัน
#เรียกไปที่ ฟังก์ชันเรียกชื่อว่า square ซึ่งภายในตัวฟังก์ชัน
##มีการประกาศตัวแปรชื่อ new_value โดยมีการคำนวณเลข 4 ยกกำลัง 2
##หลังจากนั้นก็พิมค่าในตัวเเปร new_value ด้วยฟังก์ชัน print
##ค่า 16 จึงแสดงออกมาทางหน้าจอ
'''
"""
##define function argument
def square(value) : ##define argument value
    new_value = value **2  ##use value to compute
    print(new_value) 

square(4)##call square function and assign 4 agu
square(5)##call square function and assign 5 agu
"""

def square (value):
    """Return the square of value !!! """
    new_value = value  **2
    return  new_value ##return ค่าตัวแปร new_value กลับ 

num = square(4) ## กลับมา ณ ที่จุดเรียกใช้ function
print(num)
##เราประกาศ function และสร้างขั้นตอนการทำงานใน body
##สุดท้ายจบ function เรามีการคืนค่าตัวแปร ย้อนกลับไป ณ จุดที่เรียกใช้
##เรียกใช้ square function พร้อมส่งค่า 4 ไปให้
##ขั้นตอนการทำงานใน function ก็จะเกิดขึ้นแล้วตอนสุดท้ายคืนค่าจริง
## กลับมาที่ตุดเรียก แล้สค่านั้นถูกนำไปกำหนดให้ ตัวแปร num
## สุดท้ายตัวแปร num ถูกพิมพ์ ออกทางหน้าจอด้วย print()

num = square(5)
print(num)
print(square(6))

base = 10
print(square(base))
##เรียก func print ส่งค่า funct square ที่ส่งค่าตัวแปร base

## ใบงานที่ 1 shout function and call one time
def shout(value):
    print(value)

shout_word = "Congratulation" + "!!!"
shout(shout_word)

def shout ():
    shout_word = "congratulation"+"!!!"
    print(shout_word)

shout()

def shout_word():
    new_word =  "congratulation!!"
    print(new_word)

shout_word()

#ใบงานข้อที่ 3 assign argument and re turn value
def shout(word): # word = "congratulation"
    """Return a string with three exclamation marks"""

    ##Cocatenate string : shout_word
    shout_word = word +"!!!" + "Sack"
    ##"congratulation Sack !!!"
    
    ##return print with return
    return shout_word

##Pass "Congratulation" to shout and return to yell var
yell = shout("congratulation")

#print yell
print(yell)
## ถ้าอยากได้คำว่า congratulation ชื่อเรา !!! ทำไง


##mutiple function parameter(argument)
def raise_to_power(base, power):
    """ Raise base to the value of power """
    new_value = base ** power
    return new_value
#call function
result = raise_to_power(5, 2)
print(result)
##ประกาศ function ชื่อ raise_to_power พร้อมกำหนดให้มี 2 argument
##ตัวแรกชื่อ base และ power ตามลำดับ
##ในตัว function มีการคำนวณ base ยกกำลังด้วย power
##มาเก็บในตัวแปร new_value แล้ว return ค่าตัวแปร ื new_value กลับ
##
##เรียก raise_to_power พร้อมส่งค่า (pass) 4 and 2 ไปให้
##raise_to_power จrนำค่า 4 and 2 ไปคำนวณตามขั้นตอนใน body
##ค่า 16 ก็จะถูก return มาเก็บในตัวแปร result and print output


##พอเป็นแบบนี้ข้างใน body ของ function จะไม่มีการกำหนดค่าไว้ก่อน
result = raise_to_power(5, 3)
print(result)
print("5 power by 3 = %s"%(result))
#get every value assign to variable
valueB = 5
valueP = 3
result = raise_to_power(valueB, valueP)
print("%s power by %s =%s" %(valueB, valueP, result))
##>> 5 power by 3 = 125


even_nums = (2, 4, 5)
type(even_nums)
print(type(even_nums))
## Tuple ต่างจาก list ตรงที่สร้างแล้วแก้ไขไม่ได้
## ตัวแปรที่สร้างแล้วสร้างเลยแก้ไขภายในไม่ได้ immutable
## แต่ก็เป็น zero based indexing
print(even_nums)
a, b, c = even_nums
print(a)

##Tuple คือ ตัวแปรที่มีโครงสร้างเป็นสมาชืกหลายตัวคล้าย list
##สามารถอ้างอิงบาง element ได้แบบ zero-based indexing
##แต่ที่ต่างกันคือ เป็น immutable คือการสร้างและกำหนดค่าแล้วแก้ไขไม่ได้

## เราเอาตัวแปร tuple มาเก็บผลลัพธ์การ return function ที่ต้องการส่งกลับหลายตัวแปร

##ตัวอย่าง immutiple argument and Return tuple

def raise_both(value1, value2):

    new_value1 = value1 ** value2 # 2 **3
    new_value2 = value2 ** value1 # 3**2
    new_tuple = (new_value1, new_value2)
                               # 8      ,         9
    return new_tuple
result = raise_both(2,3)
print(result)#(8. 9)
# การแยก Tuple
res_val1, res_val2 = raise_both(5, 3)
print(res_val1)
print(res_val2)

#ใบงานที่  4 function ที่รับข้อความ congratulation และชื่อ
#ตัวอย่างผลลัพธ์ congratulation ชื่อ !!
def word(value):
    new_value =  value + " SACK !!!!"
    return new_value

name  = word("congratulation")
print(name)


#ใบงานที่ 5  multiple arguments + return tuple
#อยากให้เขียน function ที่รับข้อความ congratulation และ ชื่อ
#พิมพ์ 2 ข้อความ
#  congratualtion ***
#  ชื่อ Cool!!!


def message(con, name):
    message1 = ("Congratulation")
    message2= ("Cool Sackl!!!")
    return message1, message2
message1, message2 = message("Congratulation", "Sack")
print(message1)
print(message2)

##เฉลยใบงานที่ 5\
def shout2(value1, value2):
    "Function for creat tuple 2 element"
    sht1 = value1 + "!!!"
    sht2 = value2 + "Cool" + "!!!"

    res = (sht1, sht2) #get 2 var in tiple
    return res
#tuple extraction การแยกสามชิกใน tuple ด้วยการเอาตัาเเปรมารับรอง
res_sht1, res_sht2 = shout2("congratulation","Sack")
#เรียกฟังชันโยน argument ให้ไปแล้วได้ผลลัพธ์กลับมาและต้องแยกผลลัพธ์ออกมาเป็น 2 ตัวแปร
print(res_sht1)
print(res_sht2)

##เราประกาซตัวแปรที่ new_val ที่ root intent
new_val = 10 #global variable (scope)

def square (value):
    """Return the square  of a number"""
    new_val = value **2 ## local variable (scope)
    return new_val #การ return เป็นการีืนค่ากลับไม่ใช่ตัวแปร
print(square(876))
print(new_val) # ยังคงมีค่า 10 ไม่ใช่ 16
#new val ใน function เป็นคนละตัวกับ ข้างนอกฟังชั่น

print("Global Scope")
new_val= 10
def square2(value):
    new_val2 = new_val **2
    return new_val2
print(square2(3))
###เราโยน 3 เข้าไปแต่ใน body fucyion เราใช้ new_val มายกกำลัง 2
##ซึงมีค่า 10 ผลลัพธ์จึงได้ 100
##จะเห็นได้ว่าตอนนี้ใน function body มองเห็น new_val แล้วและสามารถดึงค่าตัวแปรไปประมวลผลได้
print("Changing value in Globa Var")
new_val = 50 #Global scope

def square3(value):
    global new_val
    new_val = new_val ** 2
    return new_val
print(square3 (3) )
print(new_val) #ต้องทีการใช้ keyword global บอกใน function body
##จึงจะสามารถอัพเดต global var ใน function body ได้

#ใบงานข้อที่ 6 keyword global
team = "teen titans"
print("Old team name : %s" %team)
def change_team():
    """change the value of the global var team"""
    global team
    team = "Justric league"
change_team()
print("New team name : %s"%team)

##เนื้อหาเสรืม changing list dict in function
team_lst = ["Doraemon"]

def insertLst(value):
    global team_lst # List ก็เป็น global var
    #method ที่เอาข้อมูล value มาต่อท้าย List
    team_lst.append(value)

insertLst("Nobita")
print(team_lst)


##global val with dictionary
bp_dict = { }
print(len(bp_dict))

def insertDct(key, value) :
    global bp_dict

    #insert new element in dict array ใช้
    bp_dict [key]  = value

#key = name Actor
#value = bp status
insertDct("gus", 99)
print(bp_dict)

### LAB 4-3 Start There
def power (number, pow=1):
    """ Raise number to the power of pow  (default  1) """
    new_value = number**pow

    return new_value
print("Result of power Function = %s"%(power(9, 2) ) )
print("Result of power Function = %s"%(power(9) ) )
print("Result of power Function = %s"%(power(9, 1) ) )

##ในบางครั้งเราก็ไม่รู้ว่า function ควรจะต้องมี Argrument เท่าไหร่ เราจึงเขียน Function ที่มี Flexible Argrument
## เราต้องการสร้าง Fuction ที่รับตัวเลขไม่จำกัด เพื่อหาผลรวม

def add_all(*args): #args = (1,2,3)
    """ Sum all values in *args together """
    """ *arg เรียกว่า flexible argument """

    #Initialize sum variable
    sum_all = 0

    #Accumulate the sum
    for num in args: # รอบที่ 3 sum = 3 num = 3
        print("Sum_all = % s, num = %s"%(sum_all, num))
        #sum_all = sum_all + num
        sum_all += num
        print("After add %s"%sum_all)

    return sum_all

print("call func by pass flex args = %s"%add_all(5,6,7,8,9,10,11))
#แนะนำให้เริ่ม ในตัว function ที่ define ขึ้น มีทั้ง docstring ใส่ comment
##และ มี code print ค่าตัวแปรต่างๆ เพื่อเช็คความถูกต้องในแต่ละลำดับขั้นตอนเสมอ

#ในบางครั้ง flex args ก็อาจจะไม่สะดวกในการเรียกใช้ เพราะ ไม่มีชื่อ args กำกับ
##สังเกต Function  round(number, ndigits = 1)
##จึงมี keyword argument **kwargs

def print_all(**kwargs):
    """Print all key-value pairs in **kwagrs """
    print("Key of argument")
    print(kwargs.keys())
    print(kwargs.values())

    #Print out the key-value pairs
    for key, value in kwargs.items():
        print(key + " : " + str (value))
print("Call fuction print_all by pass and job")
print_all(name = "Sack",  job ="Student")
print_all(team_home = "Arsenal" ,score1= 3,
               team_away = "Great Team ",  score2=1)

#อยากเขียน fuction scoreBoard
##รับ argument ประกอบด้วย
##home ชื่อทีมเจ้าบ้าน
##score1 ผลประตูเจ้าบ้าน
##away ชื่อทีมเยือน
##scpore2 ผลทีมเยือน
##
##ิอยากให้ print ผลลัพธ์ในรูปแบบ  "Arsenal3:1 Great Team"
def score(**score):
    """print all key-value pairs in **score """
    print("Key of argument")
    print(score.keys())
    print("Value of argument")
    print(score.values())

    #print out the key-value pairs
    for key,value in score.items():
        print(key + ":" + str(value))
score(home_team = "Arsenal", home_score = 3,
          away_Team = "Liverpool", away_score = 4)


def scoreBoard(home, score1, away, score2):
    print(f"{home} {score1} : {score2} {away}")

scoreBoard("Arsenal", 3, "Great Team", 1)

##นอกเหนือจากที่เราเช็ค โปรแกรมที่เราเขียน ทำงานให้ผลลัพธ์ได้ตามที่ออกแบบไว้หรือไม่
##สามารถแก้ไชโจทย์ปัญหาที่ได้รับมาแล้วหรือไม่อย่างไม่มี error ในขั้นถัดมา เราก็จะต้องวิเคราะห์การใช้ทรัพยากรในการ
##ประมวลผลโปรแกรมทรัพยากรในการประมวลผล 1 เวลา 2 หน่วยความจำ
##
##ในบทนี้เราพูดถึงเชิงเวลาเพียงอย่างเดียว ใน python ก็จะมี packege เกี่ยวกับเวลา time

print("Check time Execution")
import time
 ## recode time brfore execution
start_time = time.time()

#excute operation
result = 5*2

#recode time after eccution
end_time = time.time()

print("Result calculation in {} sec ".format(
    end_time - start_time))

print("Result calculation in %5f sec"% (end_time - start_time) )


#for loops
for_loop_start_time = time.time()
result = [ ]
for i in range(0, 1000000):
    result.append(i*i)

for_loop_end_time = time.time()

print("Time using the for loop : %s" %(for_loop_end_time - for_loop_start_time) )

#List comprehension
print("Example of list comprehension")
list_comp_start_time = time.time()
result = [i*i for i in range (0, 1000000) ]
list_comp_end_time = time.time()

print("Time using the list comprehesion : %s"
      %(list_comp_end_time - list_comp_start_time) )

#เราจะเห็นว่า งานก็เป็นงานเดิมแก้ไชปัญหาเดียวกัน วนรอบทำซ้ำ 1 ล้านครั้ง
##เพื่อเติมข้อมูลเลขผลคูณในตัวแปร list
##แต่การเขียนแบบ list comprehension กลับใช้เวลา ประมวลผลน้อยกว่า
##ประมาณ 1 เท่า (เครื่องอาจารย์)
##เราเรียกว่าการเขียนโปรแกรมทีนอกจากจะแก้ไขปัญหาได้แล้ว ยังใช้ ทรัพยากร ได้น้อยกว่า
##ว่า Efficient coding การโค้ดอย่างมีประสิทธิภาพ

def sum_brute_force(N):
    res = 0
    for i in range (1, N+1):
        res = res + i
        #res += i
    return res

bf_start_time = time.time()
print("Sum N number by brute force alg : %s"
      %(sum_brute_force(1000000) ) )
bf_eng_time = time.time()
print("Sum N number by brute force alg : %s"
      %(sum_brute_force(1000000) ) )
print("Sum N number brute force alg : %s"
      % (sum_brute_force(1000000)) )

def sum_formula(N):
    return N*(N+1)/2
formu_start_time = time.time()
print("Sum N number by formula: %.0f"
      %(sum_formula(1000000)) )
formu_end_time = time.time()
print("Time using formula : %s"
      %(formu_end_time - formu_start_time))

##จะเห็นได้ว่า brute force alogorithm ก็สามารถให้ค่า
##ผลรวมเมื่อป้อนเลขเมื่อป้อน N เข้าไปได้ถูกต้อง (gเขียน Code มีประสิทธิผล)
##Effective coding
##แต่ก็ใช้เวลาในการประมวลผลจำนวนหนึ่ง
##แต่เมื่อเราเปลี่ยนไปใช้ formula การหาผลรวม ซค่งเป็นส่วนหนึ่งของวิชา Math for cs และ
##alogorithm design เวลาในการประมวลผลจะน้อยลงด้วย เรียกว่า เขียน code อย่างมีประสิทธิภาพ
##Efficiency coding 
def square() : #Funcion Header หัวฟังก์ชัน
    new_value = 4**2 #Function Body ตัวฟังก์ชัน
    print(new_value)
square()
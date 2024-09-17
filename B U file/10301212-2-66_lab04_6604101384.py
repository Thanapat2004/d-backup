"""
## กด save และตั้งชื่อไฟล์ .py ดังนี้
##10301212-2-66_lab04_6604101384.py


##การเขียน function ต้องมีการประกาศ function
##define function

def square():        #function header หัวฟังก์ขัน
    new_vale = 4 ** 2       #function body ตัวฟังก์ชัน
    print(new_value)

square()     #call function การเรียกใช้ฟังก์ชัน
#เรียกไปที่ ฟังก์ชันชื่อว่า square ซึ่งภายในตัวฟังก์ชัน
##มีการประกาศตัวแปรชื่่อ new_value โดยมีการคำนาณ เลข 4 ยกกำลัง 2
##หลังจากนั้นก็พิมพ์ค่า ในตัวแปร new_value ด้วยฟังก์ชัน print
##ค่า 16 จึงแสดงออกมาทางหน้าจอ
"""
"""
def square(value):
    new_value = value **2
    print(new_value)

square(4)   #call square function and assign 4 agu
square(5)   #call square function and assign 5 agu
"""

def square(value):
    """ Return the square of value  !!! """
    new_value = value ** 2
    return new_value

num = square(4)     #กลับมา ณ จุดเรียกใช้ function
print(num)

##เราประกาศ function และ สร้างขั้นตอนการทำงานใน body
##สุดท้ายจบ function เรามีการคืนค่าตัวแปร ย้อนกลับไป ณ จุดที่เรียกใช้
##เรียกใช้ square function พร้อมส่งค่า 4 ไปให้
##ขั้นตอนการทำงาน function ก็จะเกิดขึ้นแล้วตอนสุดท้ายคืนค่าจริง
##กลับมาที่จุดเรียก แล้วค่านั้นถูกนำไปกำหนดให้ ตัวแปร num
##สุดท้ายตัวแปร num ถูกพิมพืออกทางหน้าจอด้วย print()

num = square (5)
print(num)

print(square(6))

base = 10
print(square(base))
##เรียกใช้ func print  ส่งค่า funct sqare ที่ส่งตัวแปร base เข้าไป



#ใบงาน function shout word
def shout(value):
    print(value)

shout_word = "congratulation" + "!!!"
shout(shout_word)

#version basic
def shout(): 
    shout_word = "congratulation" + "!!!"
    print(shout_word)

shout()

#ใบงานข้อที่ 3 assign argumemt and return value
def shout(word):   # word = "congratulation"
    """ Return a string with three exclamtion marks """

    #Concatenate string: shout_word
    shout_word = word + ' supawit ' + "!!!"
    #"conngratulation supawit !!!"

    #return print with return
    return shout_word

##Pass "congratulation" to shout and return to yell var
yell = shout('congratulation')

#print yell
print(yell)
### ถ้าอยากได้เป็นคำว่า congratulation ชื่อเรา !!!  ทำยังไง ไม่เพิ่ม agu

#multiple function parameters (arguments)
def raise_to_power(base, power):
    """Reaise base to the valur of power """
    new_value = base ** power
    return new_value
#call function
result = raise_to_power(4,  2)
print(result)
#ประกาศ function ชื่อ raise_to_power พร้อมกำหนดให้มี 2 argument
##ตัวแรกชื่อ base และ power ตามลำดับ
##ในตัว function มีการคำนวณ base ยกกำลังด้วย power
##มาเก็บในตัวแปร new_value แล้ว return ค่าตัวแปร new_value กลับ
##
##เรียก raise_to_power พร้อมส่งค่า (pass)  4 และ 2 ไปให้
##raise_to_power จะนำค่า 4 และ 2 ไปคำนวณตามข้นตอนใน body
##ค่า 16 ก็จะถูก return มาเก็ยในตัวแปร result และ print ออกจอ

#พอเป็นแบบนี้ ข้างใน body ของ function จะไม่มีการกำหนดค่าไว้ก่อน
result = raise_to_power(5, 3)
print(result)
print("5 power by 3 = %s" %(result))
#get every value assign to variables
valueB =5
valueP = 3
result = raise_to_power(valueB, valueP)  #ค่าเรียงตามลำดับการส่ง
print("%s power by %s = %s" %(valueB, valueP, result))
## >>>   5 power by 3 = 125


#tuple คือ ตัวแปร ทีมีโครงสร้างสมาชิกหลายตัว คล้าย list
##สามารถอ้างอิงบาง element ได้แบบ zero-based indexing
##แต่ที่ต่างกันคือ เป็น immutable คือสร้างและกำหนดค่าแล้วแก้ไขไม่ได้

#เราเอา ตัวแปร tuple มาเก็บผลลัพธ์การ return function ที่้องการ
#ส่งกลับหลายตัวแปร

#ตัวอย่างการ multiple arguments and return tople

def raise_both(value1, value2): #2  3

    new_value1 = value1 ** value2       #2**3
    new_value2 = value2 ** value1       #   3**2

    new_tuple = (new_value1, new_value2)
                            #       8       ,       9
    return new_tuple

result = raise_both(2, 3)
print(result)  # (8, 9)
#การแยก tuple
res_val1, res_val2 = raise_both(5, 3)
print(res_val1)
print(res_val2)

#ใบงานที่ 4
# อยากให้เขียน function ที่รับข้อความ congratulation และ ชื่อ
#ตัวอย่างผลลัพธ์  congratulation ชื่อ !!!
def word(value):
    new_value = value + "BOSS !!!"
    return new_value

name = word("congratulation")
print(name)

#ใบงานที่ 5
#อยากให้เขียน function ที่รับข้อความ congratulation และ ชื่อ
#พิมพ์ 2 ข้อความ
#   congratulation ***
#   ชื่อ Coll!!!
def text(con,name):
    text1 = ("Congratulation")
    text2 = ("Cool Boss!!!")
    return text1, text2
text1, text2 = text("Congratulation", "Boss")
print(text1)
print(text2)
























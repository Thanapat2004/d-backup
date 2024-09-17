import datetime
now = datetime.datetime.today()
print("TO DAY IS :", now)
def calculate(brithday):
    today = datetime.date.today()
    age = today.year - brithday.year
    if (today.month, today.day) < (brithday.month, brithday.day):
        age -= 1  
    return age
your_years = int(input("กรุณาใส่ปีเกิดของคุณ (ค.ศ.): "))
your_brithday = datetime.date(your_years, 1, 1) 
print(f"Your AGE : {calculate(your_brithday)} years")

"""                             การถามว่าต้องการเพิ่มข้อมูลส่วนตัวหรือไม่                             """
want = str(input(" หากต้อกงารป้อนข้อมูลส่วนตัว กด : y, หากไม่ กด : n "))
yes = "y" 
no = "n"
if want == yes :
    YOUR_ID = int(input( "ID CARD 13 : " ))
    while YOUR_ID < 13:
        print("กรุณากรอกเลขบัตรให้ครบด้วย !!!")
        YOUR_ID = int(input( "ID CARD 13 : " ))
        continue
    NAME = input(" MR OR MISS :")
    NICE_NAME = input("  MR OR MISS :")
    YOUR_BRITHDAY = int(input("YOUR_BRITHDAY : "))
    HEIGHT = int(input(" CM :  "))
    WEIGHT = float(input( " KG :  " ))
    bmi = WEIGHT / (HEIGHT/100)**2
    print("YOUR_BMI : %.14f"%bmi)
else:
    print("no")



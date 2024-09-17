""" 10301212-2-66_Lab05_6604101330_datetime 
"""
from datetime import datetime
print("Now datetime subodule import in mem")

parking_violations_date = '06/11/2016'
print(type(parking_violations_date))
##dd/mm/yy dd/mm/yyyy yyy-mm-dd
##mm/dd/yyy mm-dd-yy
#04-03-24

date_dt = datetime.strptime(parking_violations_date,'%m/%d/%Y')
print(date_dt)
print(type(date_dt))
#2016-06-11 00:00:00 ปี /จๅก เดือน 06 (มิถุนายน) วันที่ 11 
#note  ว่า มาตรฐานของการเขียนวันที่ เวลา - ปี - เดือน - วัน

parking_violations_date = '06/11/2016 20:15:30'
date_dt = datetime.strptime(parking_violations_date,'%m/%d/%Y %H:%M:%S')
print(date_dt)

#str2datetime -> .strptime()
#datetime -> .strptime()

#ข้อวังเกต ตอนแปลงกลับไปเป็น string เราเรียก medthod จาก obj date_dt
#ไม่ได้เรียก datetime submodole
#format ที่เป็ฯ agument ใน strftime ช่วยให้เราจัดรูปแบบ str ที่นำเสนอ วันที่ และเวลาได้ตามต้องการ
pkvd_str = date_dt.strftime('%Y/%m/%d ,%H hrs.:%M mins.')
print(pkvd_str)
print(type(pkvd_str))
print("Now pkvd_str data type: %s"%type(pkvd_str))

print(date_dt.isoformat())
#2016-06-11T20:15:30
#International Standard Organzition

#แสดงค่าเวลาปัจจุบัน medthod.now()
#เป็นเวลาท้องถินที่เครื่องนั้นประมวลผล
local_dt =  datetime.now()
print("Local time now : %s"%local_dt)

#ในกรณีที่เราต้องการเก็บค้าเวลาสากล UTC universal time
utc_dt = datetime.utcnow()
print("Universal time Now : %s" %utc_dt)

#ทำไมต้องเก็บข้อมูลเป็น obj datetime นึกภาพ เก็บข้อมูลวันที่เวลาเป็น str
print("Day in Local datetime : %s" %local_dt.day)
#ข้องสังเกต . day ไม่มี() เพราะมันไม่ใช่ method แต่เป็น attribute

print("month in local datetime : %s " %local_dt.month)
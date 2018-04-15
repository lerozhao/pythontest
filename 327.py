import json
# json.dumps()  转换成json
# json.loads()  json解码
import time
import calendar

# list1=[1,2,3,6,7,'haha','heihei']
# dict1={'a':1,'b':2,'c':'ls'}
# tuplel=(1,2,3,'kk')
# int1=1

# a=json.dumps(int1)
# print(type(a),a)
# b=json.loads(a)
# print(type(b),b)

time_now=time.time()
print(time_now)
time_now_localation=time.localtime(time.time())
print(time_now_localation)   
time_now_localation_format=time.asctime(time_now_localation)
print(time_now_localation_format)
calendar1=calendar.month(2018,3)
print(calendar1)
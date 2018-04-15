# class Employee:
#     pay_raise_amount=1.2
#     __weight=40   # 类外面不能修改，也不能直接调用
#     def __init__(self,first,last,pay,weight):
#         self.first=first
#         self.last=last
#         self.pay=pay
#         self.email=first+last+"@email.com"
#         self.__weight=weight
    
#     def fullname(self):
#         return self.first+self.last
#     def new_pay0(self):
#         return self.pay * Employee.pay_raise_amount
#     def new_pay1(self):
#         return self.pay * self.pay_raise_amount
#     def __say(self):
#         print("{}".format(self.__weight))
#     def Isay(self):
#         self.__say()
# class Sample(Employee):
#     super().__init__(first,last,pay,weight)

# # emp1=Employee("xiaoming","wang",1000,50) 
# # emp2=Employee("xiaohong","zhang",2000)
# # print(emp1.fullname())
# # print(emp1.email)
# # emp1.say()
# # emp1.Isay()

# sam=Sample("xiaoming","wang",1000,50) 
# sam.say()

# import re

# html =  """<span class="top_score">7315</span>
#         <span class="top_score">7316</span>
#         <span class="top_score">73</span>
#         <span class="top_score">715</span>
#         <span class="top_score">15</span>"""

# res = re.findall('<span class="top_score">(.+?)</span>',html)
# print(res)

import urllib.request
import re
r=urllib.request.urlopen("http://118.31.19.120:3000/")
# print(r.read().decode("utf-8"))
html=r.read().decode("utf-8")
res = re.findall(r'(?<=<span class="top_score">).+?(?=</span>)',html)
print(res)
class Person:
    def __init__(self,name,sfznum):
        self.name=name
        self.sfznum=sfznum
    def sikao(self):
        print(self.name,"思考")
    def aiqing(self):
        print(self.name,"爱情")
class Student(Person):
    def __init__(self,name,stunum,sfznum):
        self.name=name
        self.stunum=stunum
        self.sfznum=sfznum
    def xuexi(self):
        print(self.name,"学习")
    def kaoshi(self):
        print(self.name,"考试")
a=Student(name="name",stunum=2,sfznum=333333)
print(a.sfznum)
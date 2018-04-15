# class Student:
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id
#         #赋值给类的参数=传进来的参数
#         #调用参数，用self.
#         # 没有这个方法，说明没有类的参数（类里面所有的方法都可以用到的参数叫类的参数）
#         print("一般在对象被创建的时候执行，是在所有方法之前执行")
#     def study(self):
#         print(self.name,"is studying")
# zhao=Student("zhao",23,5)
# #只要有实例化，都会执行init；类的入口，每个类封装都会有一个init函数，python内置
# # namelist=["zhao","dong","zhai"]
# # name="zhao"
# # zhao.study(name)
# # zhao.study(namelist[1])
# zhao.study()

# class Animal:
#     def eat(self):
#         print(self.name,'eat goods')
# class Cat(Animal):
#     def __init__(self,name):
#         self.name=name
#     def cry(self):
#         print("miaomiaomiao")
# xiaohua=Cat("小花猫")
# xiaohua.eat()
# xiaohua.cry()

# 定义一个动物类，动物可以做的事情有：吃、喝、拉、撒；定义个人类，可以除了吃喝拉撒还能：思考，爱情
#定义一个大象类，它能喷水；再定义一个学生类，还能：学习、考试；定义一个教师类，能：教学
# 打印所有实例的所有方法
# 一号蟑螂（zhanglang1）；大象实例，大象2号（ele2）；人实例（mayun）；学生实例（weichengqun）；老师（john）
class Animal:
    def __init__(self,name):
        self.name=name
    def chi(self):
        print(self.name,"吃")
    def he(self):
        print(self.name,"喝")
    def la(self):
        print(self.name,"拉")
    def sa(self):
        print(self.name,"撒")
class Person(Animal):
    def __init__(self,name,sfznum):
        self.name=name
        self.sfznum=sfznum
    def sikao(self):
        print(self.name,"思考")
    def aiqing(self):
        print(self.name,"爱情")
class Ele(Animal):
    def penshui(self):
        print(self.name,"喷水")
class Student(Person):
    def __init__(self,name,stunum):
        self.name=name
        self.stunum=stunum
    def xuexi(self):
        print(self.name,"学习")
    def kaoshi(self):
        print(self.name,"考试")
class Teacher(Person):
    def __init__(self,name,teachernum):
        self.name=name
        self.teachernum=teachernum
    def jiaoxue(self):
        print(self.name,"教学")
zhanglang1=Animal("zhanglang1")
zhanglang1.chi() 
zhanglang1.he()
zhanglang1.la()
zhanglang1.sa()
ele2=Ele("ele2")
# ele2.chi()
# ele2.he()
# ele2.la()
# ele2.sa()
ele2.penshui()
mayun=Person("mayun",1234567)
mayun.sikao()
mayun.aiqing()
weichengqun=Student("weichengqun",11111)
weichengqun.xuexi()
weichengqun.kaoshi()
print("stunum",weichengqun.stunum)
john=Teacher("john",3)
john.jiaoxue()

    

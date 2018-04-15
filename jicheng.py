class People:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

class Student(People):

    def __init__(self,n,a,w,grade):
        # People.__init__(self,n,a,w)
        People.__init__(self,n,a,w)
        self.grade = grade

    # 方法重写
    def speak(self):
        print("%s 说: 我 %d 岁, %d 年级" %(self.name,self.age,self.grade))

class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    @property
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
 
#多重继承
class sample(speaker,Student):
    a =''
    def __init__(self,n,a,w,g,t):
        Student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
 
test = sample("Tim",25,80,4,"Python")

n,t="1 222".split(" ")
test.n=n
test.t=t
test.speak#方法名同，默认调用的是在括号中排前地父类的方法

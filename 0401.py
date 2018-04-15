# list1=[1,2,3,4,5,6,7,8,9]
# print(list1[1])
# print(list1[0:-1])
# print(list1[1::2])
# list2=["tab","tas"]
# list1.extend(list2)
# for i in list1:
#     list2.append(i)
# list1.count()
# list1.sort()
# list1.remove()
# i=0
# j=1
# while j<21:
#     print(j)
#     i,j=j,i+j

# list1=[1,2,4,7]
# for i in list1:
#     for j in list1:
#         for k in list1:
#             for l in list1:
#                 if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l:
#                     print(1000*i+100*j+10*k+l)


# list3=[]
# for i in range(1,10,2):
#     list3.append(i)
# print (list3)


# def john(a,b):
#     # return a*b;
#        if a*b>10:
#          print('da')
#        elif a*b<10:
#          print('xiao')
#        else:
#          print('wrong')

# john(3,5)



# b=[1:'1',2:'2']
# def plus(b):
#     return b*10;
# print(plus(b))
# print(b)

# def sum(q,w):
#     t=q+w
#     print('nei',t)
#     return t;
# t=sum(10,20)
# print('wai',t)


# def printinfo(arg1,*v):
#     print('shuchu')
#     print(arg1)
#     for var in v:
#         print(var)
#     return;

# printinfo(10);
# printinfo(70,60,50);

# import sys


# def f(a):
#     if a==1:
#         return a;
#     if a>1:
#       return a+f(a-1)
# print(f(999))


# a=lambda x,y:x*x+y
# print(a(3,2))

# for i in range(10):
#     age=i
# print(age)

# name ='1'
# def f1(name):
#     print(name)
# def f2():
#     name='2'
#     f1(name)

# f2()

# num=input(2*6)
# print(num)


def make_counter():
    count = 0
    def counter():
        nonlocal count
        count +=1
        return count
    return counter
def make_counter_test():
    mc=make_counter()
    print(mc())
    print(mc())
make_counter_test()

# mcc=make_counter()
print(make_counter)
# print(mcc())
# print(mcc())
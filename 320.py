# list3=['A','a','B','b','C','c']
# #取出所有大写字母
# print('取出所有大写字母')
# # i=0
# # list33=[]
# # while i<6:
# #     print(list3[i],end='\t')
# #     list33.insert(list3[i])
# #     i=i+2
# # print(list33)
# print(list3[0::2])
# #将所有小写字母顺序倒过来
# print('将所有小写字母顺序倒过来')
# list4=list3[1::2]
# list4.reverse()
# print(list4)
# #想办法生成两个列表，将大小写分开
# print('想办法生成两个列表，将大小写分开')
# list5=list3[0::2]
# list6=list3[1::2]
# print(list5)
# print(list6)



# 利用26哥字母创建一个字典A:a
# 1.找出所有的值value
# 2.字典转换成字符串
# 3.取出所有的值转换成字典











# x={'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'}
# print('1.找出所有的值value')
# print(x.values())
# print('字典转换成字符串')
# print(str(x))
# print('取出所有的值转换成字符串')
# print(str(x.values()))

print('九九乘法表')
for i in range(1,10):
    for j in range(1,10):
        if j>i:
           print()
           break;
        else:
           print(i,'*',j,end='\t')

# print()
# print('有一对兔子，从出生起每个月生一对兔子，小兔子每个月又生一对兔子，假如兔子不死，第19个月有多少个兔子？？？')
# x=1   # 初始兔子数 
# for y in range(2,20):
#     x=x*2
# print('到第十九个月的兔子总数为：',(x*2))

# print('第三题：第一次超过两千只是在什么时候')



# sum=0
# for a in range(1,9,2):
#     for s in range(1,9,2):
#           for d in range(1,9,2):
#                  for f in range(1,9,2):
#                       if a!=s and a!=d and a!=f and s!=d and s!=f and d!=f:
#                         print(a*1000+s*100+d*10+f);
#                         sum+=1
# print(sum)



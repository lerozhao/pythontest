# 正则表达式区分大小写

import re
# key=r"<html><body><h1>hello word<h1></body></html>"# 这段是你要匹配的文本
# p1=r"(?<=<h1>).+?(?=<h1>)"# 这是我们写的正则表达式规则
# pattern1=re.compile(p1)# 编译这段正则表达式
# matcher1=re.search(pattern1,key)# 在源文本中搜索符合正则表达式部分
# print(matcher1.group())


# str="pythonjavac++phpRC#Python"
# rules='python'# 最原始的正则表达式
# r=re.compile(rules,re.S)# re.S遍历取出所有符合要求的数据
# match=re.findall(r,str)
# print(match)
# print(r.findall(str))

# search 和findall有什么区别或差异
# .字符在正则表达式代表着可以代表任何一个字符包括它本身，+表示多次匹配
# findall返回所有符合要求的元素列表，只有一个元素时，也是返回列表
# *表示匹配0次或者多次
# []代表匹配里面字符中的任意一个；[^]表示除了内部包含的字符以外都能匹配
# [0-9][a-z][A-Z]   \d等于[0-9]表示0到9中的任意一个数字；\D表示除0-9之外的任意非数字
# \w 等于[a-z0-9A-Z]匹配大小写字母、数字和下划线；             \W除了数字、大小写字母和下划线都匹配

# ?贪婪模式变为懒惰模式，一旦找到，就停止寻找
# {a,b}(代表a<=匹配次数<=b)    比如s="xy{1,2}"  y匹配一到两次，即寻找xy 或xyy
key=r"chuxiuhong@hit.edu.cn"
p1=r"[^@]*\."
# p1=r"@.+?\."
pattern1=re.compile(p1)
print(pattern1.findall(key))
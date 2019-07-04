# -*- coding: utf-8 -*-

# 输出
print("hello world!!!")  # 自动换行输出
print("hello python!!!", end="这里面想写啥写啥 空格什么的 怎么喜欢怎么来      ")  # 不换行输出
# 输入
demo = input("请输入您的姓名,按enter键结束: ")
print(demo, ",欢迎来到Python的世界!")

# 数字类型  不可变
# 1. 整数 1
# 2. 浮点数 1.1  1.6e9(1.6 * 10的9次方)
# 3. 布尔型  True(1) False(0)
# 4. 复数   eg: 1 + 1j
# 加减乘除算法时,除法和java是不一样的  还有一个乘方  eg: 2 ** 3   结果就为8 是不是很爽
demo = 10 / 3  # 精确除法,得到的是一个浮点数
print(demo)  # 3.3333333333333335
demo = 10 // 3  # 取整
print(demo)  # 3

# 字符串  不可变
# 1. 拼接时可以用','(自带一个空格) 或者用'+'(还是习惯这个) 再或者格式化(下面专门说 有点儿意思)
#    注意: 用+拼接时,如果是数字类型的需要用str()函数,eg: str(2) + "22"
demo = 'demo'
print(ord('p'), ord('y'), ord('t'), ord('h'), ord('o'), ord('n'))  # 112 121 116 104 111 110  字符->编码
print(chr(112), chr(121), chr(116), chr(104), chr(111), chr(110))  # p y t h o n   编码->字符
print(len(demo))  # 4  字符串长度
print(str(True) + "555")  # True555 字符串拼接
print(1, "de")  # 1 de
print(demo * 2)  # demodemo
print(demo[0:2])  # de  截取字符串
print(demo[1])  # e 获取指定下标的字符
print(demo[1:])  # emo
print(r'demo\nceshi')  # demo\nceshi  r''的作用是转义字符不发生转义
# 2. 字符串格式化(我是不常用这个,感觉很是麻烦,哪有+来得爽,只是感觉java上没有这个,拿来说说,只当了解)
# %s(字符串)  %d(整数)  %f(浮点数)  %x(十六进制整数)  其实一个%s就成  貌似all->字符串
print('我今天(%s)心情还好,但是这个天气(%s)却不怎么滴!' % ('2019-7-4', '阴天'))
print('%03d' % 1)  # 001  这个不错 那个3代表字符长度转为>=3,不够的补0(只能写0)
print('%.1f' % 6.84888888)  # 6.8  f前的数代表几位小数(四舍五入)
print('我今天({0})心情还好,但是这个天气({1})却不怎么滴!'.format('2019-7-4', '阴天'))  # 这个字符串的格式化方法贼麻烦

# 列表 list  这个在java开发时我是经常用 高频
#   1. 截取的方式和字符串都一样 能拼接 能用 * 复制 都一样
#   2. 有序 元素能改变
#   3. [] 表示空列表
demoList = [6, 6.6, True, 'demo', [6, 6.6, True]]
print(demoList[1:3])  # [6.6, True]
demoList.append('ceshi')
print(demoList)  # 在末尾追加元素  [6, 6.6, True, 'demo', [6, 6.6, True], 'ceshi']
demoList.insert(1, "demo")
print(demoList)  # 插入元素  [6, 'demo', 6.6, True, 'demo', [6, 6.6, True], 'ceshi']
demo = demoList.pop(2)  # 删除指定元素并返回该元素  为空时 默认删除末尾元素
print(demo)  # 6.6
demoList[0] = 8
print(demoList)  # 修改指定元素

# 元组 tuple 基本和list一样   不可变
#   1. 截取的方式和字符串都一样 能拼接 能用 * 复制 都一样
#   2. 有序 元素不能改变
#   3. () 表示空元组  比较特殊的是 只有一个元素的元组应该这样表示 eg: (1,)
demoTuple = (6, 6.6, True, 'demo', [6, 6.6, True])

# 集合 set
#   1.创建方式比较特殊 可以用 demoSet = {6, 6.6, True, 'demo', [6, 6.6, True]},也可以用 demoSet = set(list)
#   2.空集合必须用set()
#   3.无序不重复
#   4.很像字典中的key
#   5.综上原因 set集合可以进行并集和交集操作
demoSet = {6, 6.66, True, 'demo'}
print(demoSet)  # {'demo', True, 6, 6.66}
demoSet = set([6, 6.666, True, 'demo'])
print(demoSet)  # {'demo', True, 6, 6.666}
# demoSet = set('222')  # 一般不这么用 没什么意义
demoSet.add("ceshi")  # 添加元素
print(demoSet)  # {'demo', True, 6, 6.666, 'ceshi'}
demoSet.remove(6)
print(demoSet)  # {'demo', True, 6.666, 'ceshi'}
demoSet1 = {6, 6.66, True, 'demo'}
print(demoSet & demoSet1)  # 交集  {True, 'demo'}
print(demoSet | demoSet1)  # 并集  {True, 'demo', 6.666, 6, 6.66, 'ceshi'}

# 字典 Dictionary  真心和java中的map很像
#   1. 空字典 {}
#   2. 判断是否有某个key值  用 (key in demoDictionary) 根据返回的True和False判断
demoDictionary = {"name":"muyou", "age":26, 'gender':'男'}
print(demoDictionary["name"])  # 根据key值获取value
print(demoDictionary.keys())  # 获取所有的key值  dict_keys(['name', 'age', 'gender'])
print(demoDictionary.values())  # 获取所有的value值  dict_values(['muyou', 26, '男'])
print(demoDictionary.pop("gender"))  # 删除元素


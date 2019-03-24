# -*- coding: utf-8 -*-
'''
1.lambda定义了一个匿名函数；
2.lambda并不会带来程序运行效率的提高，只会使代码更简洁；
3.如果可以使用for..in..if 来完成，坚决不用lamba；
4.尽量用函数，提高代码的可复用性喝可读性；
'''
from functools import reduce

'''
python内置函数
filter 返回满足函数的数组
map  对里面的参数依次输出
reduce：不能直接使用，需要导包
zip：对两个数组进行合并
'''
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
filter_foo = filter(lambda x: x % 3 == 0, foo)
print(list(filter_foo))
print([x for x in foo if x % 3 == 0])
map_foo = map(lambda x: x * 2 + 10, foo)
print(list(map_foo))
print([x * 2 + 10 for x in foo])
list_a = [1, 2, 3]
reduce_foo = reduce(lambda x, y: x + y, list_a)
reduce_foo = reduce(lambda x, y: x + y, list_a, 5)
print("reduce")
print(reduce_foo)
print("-----------")
for i in zip([1, 2, 3], [4, 4, 8]):
    print(i)


# 闭包函数的使用
def a_line(a, b):
    return lambda x: a * x + b


line1 = a_line(2, 3)
print(line1)
print(line1(10))

# 用zip对字典进行 key values 互换操作
dicta = {'a': 'aa', 'b': 'bb'}
zip_b = zip(dicta.values(), dicta.keys())
dictb = dict(zip_b)
print(dictb)

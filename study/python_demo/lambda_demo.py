# -*- coding: utf-8 -*-
'''
1.lambda定义了一个匿名函数；
2.lambda并不会带来程序运行效率的提高，只会使代码更简洁；
3.如果可以使用for..in..if 来完成，坚决不用lamba；
4.尽量用函数，提高代码的可复用性喝可读性；
'''
from functools import reduce

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
filter_foo = filter(lambda x: x % 3 == 0, foo)
print(list(filter_foo))
print([x for x in foo if x % 3 == 0])
map_foo = map(lambda x: x * 2 + 10, foo)
print(list(map_foo))
print([x * 2 + 10 for x in foo])
reduce_foo = reduce(lambda x, y: x + y, foo)
print(reduce_foo)

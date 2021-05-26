def f1(x):
    return x * 2


def new_f1(f):
    """装饰器函数"""
    def fn(x):
        print('call ' + f.__name__ + '()')
        return f(x)
    return fn


# g1 为装饰后新函数
g1 = new_f1(f1)
print(g1(5))


# f1为装饰后新函数，彻底隐藏f1的原始定义
f1 = new_f1(f1)
print(f1(4))

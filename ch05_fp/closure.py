def f(x):
    print('f() ...')

    def g():
        # 防止其他代码调用 g
        print('g() ...')
    return g


# 闭包
# 内层函数引用了外层函数的变量（参数也算变量）
# 然后返回内层函数的情况
# 闭包的特点
# 引用了外层函数的局部变量
# 正确使用闭包
# 确保引用的局部变量在函数返回后不能变
def calc_sum2(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum


def count():
    fs = []
    for i in range(1, 4):
        def h():
            return i * i
        fs.append(h)
    return fs


# 使用闭包请注意：返回函数不要引用任何循环变量或者后续会发生变化的变量
f1, f2, f3 = count()
print(f1())  # 期望是1 实际为9
print(f2())  # 期望是4 实际为9
print(f3())

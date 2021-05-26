def calc_sum(lst):
    return sum(lst)


arr = [1, 2, 3, 4]
print(calc_sum(arr))


def calc_sum2(lst):
    """返回内部的函数"""
    def lazy_sum():
        return sum(lst)
    return lazy_sum


arr = [1, 2, 3, 4]
f = calc_sum2(arr)
print(f)
print(type(f))
print('可以实现延迟计算，现在开始执行计算：')
res = f()
print(res)

import time
from functools import wraps
def timer(func):
    @wraps(func)
    def inner():
        print(time.time())
        ret = func()  # 原来的函数
        return ret
    return inner


@timer  # func1 = timer(func1)
def func1():
    """
    func1 xxxx
    :return:
    """
    print('func1')
    return 'func1的返回值'

@timer  # func1 = timer(func1)
def func2():
    """
    func2 xxxx
    :return:
    """
    print('func2')
    return 'func2的返回值'

print(func1.__name__)
print(func2.__name__)
print(func2.__doc__)

def wrapper1(func):
    def inner(*args, **kwargs):
        print('wrapper1 前')  # 2
        ret = func(*args, **kwargs)
        print('wrapper1 后')  # 4
        return ret

    return inner


def wrapper2(func):
    def inner(*args, **kwargs):
        print('wrapper2 前')  # 1
        ret = func(*args, **kwargs)
        print('wrapper2 后')  # 5
        return ret
    return inner

@wrapper2  # func1 = wrapper2(func1)  wrapper2.inner   func=wrapper1.inner
@wrapper1  # func1 = wrapper1(func1)  wrapper1.inner   func=func1
def func1():
    print('func1')  # 3
    return 'func1的返回值'


print(func1())  # 6

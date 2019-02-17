import time


def timer(func):
    def inner():
        print(time.time())
        ret = func()  # 原来的函数
        return ret

    return inner


@timer  # func1 = timer(func1)
def func1():
    print('func1')
    return 'func1的返回值'


def func2():
    print('func2')


def download(func):
    def inner(*args, **kwargs):
        print('下载软件')
        ret = func(*args, **kwargs)
        return ret

    return inner


@download
def yue(tools):
    print('使用{}约一约'.format(tools))
    return '约成功了'


# yue = download(yue)  # 装饰的步骤

print(yue('momo'))  # inner
yue('tantan')
yue('漂流瓶')


def wrapper(func):
    def inner(*args, **kwargs):
        # 执行被装饰函数之前进行的操作
        ret = func(*args, **kwargs)
        # 执行被装饰函数之后进行的操作
        return ret

    return inner

import time

flag = False


def outer(flag):
    def timer(func):
        def inner(*args, **kwargs):
            if flag:
                print(time.time())
                ret = func(*args, **kwargs)  # 原来的函数
            else:
                ret = func(*args, **kwargs)  # 原来的函数
            return ret

        return inner

    return timer


# @timer          # func1 = timer(func1)    inner
@outer(True)  # func1 = timer(func1)  inner
def func1():
    print('func1')


@outer(False)  # func1 = timer(func1)  inner
def func2():
    print('func2')


func1()
func2()

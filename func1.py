
def func():
    print('func')
    print('func内部的__name__:',__name__)
    pass  # 占位符

if __name__ == '__main__':
    print('func1')
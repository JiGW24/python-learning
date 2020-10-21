# a=2
# def get():
#     a = 1
#     print(a)
# get()
# print(a)

# 函数数没定义局部变量 而去打印，不会回退到全局变量
# def m():
#     print(a)
#     a = 'apple'
# a='123'
# m()

try:
    print(1/0)
except(ZeroDivisionError):
    print('出现异常')

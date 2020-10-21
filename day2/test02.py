# 编写一个名为collatz()的函数，它有一个名为number 的参数。如果参数是偶数，
# 那么collatz()就打印出number // 2，并返回该值。如果number 是奇数，collatz()就打
# 印并返回3 * number + 1。

def collatz(number):
    if number%2 == 0:
        print(number)
        return number
    elif number%2 != 0:
        print(3 * number + 1)
        return 3 * number +1

collatz(3)
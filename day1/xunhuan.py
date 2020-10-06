name=input()

while name != 'tom':
    print('请重新输入姓名：')
    name=input()
    # break语句
    if name == 'mary':
        break
    # continue语句
    elif name == 'jack':
        continue
print('输入正确')
print('请输入')
s = 'hello python'
print(len(s))

# name=input()
# while name != 'tom':
#     print('请重新输入姓名：')
#     name=input()
#     # break语句
#     if name == 'mary':
#         break
#     # continue语句
#     elif name == 'jack':
#         continue

# for循环
name = ''
if not name:
    print('name为空，true')
print('----------')
age = 1
if age:
    print('age为1,不为0,true')
print('----------')
for i in range(5):
    print('i='+str(i))
print('----------')
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')
print('------')
gaoSi = 0
for i in range(101):
    gaoSi = gaoSi + i
print('gaoSi='+str(gaoSi))


print('输入正确')
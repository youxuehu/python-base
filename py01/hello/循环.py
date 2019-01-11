# 循环
print('循环')
for i in '100':
    print(i)
# 循环0到100
print('循环0到100')
for i in range(1, 100):
    if i % 2 == 0:
        break
    print(i)
print('while循环')
sum = 0
num = 0
while num < 100:
    sum += num
    num += 1
    print(sum)

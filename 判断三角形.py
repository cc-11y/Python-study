a=int(input('请输入数据：'))
b=int(input('请输入数据：'))
c=int(input('请输入数据：'))
if a+b > c and b+c > a and a+c > b:
    print('可以组成三角形')
elif a <= 0 or b <= 0 or c <= 0:
    print('数据不合理')
lst = []
for i in range(5):
    goods = input('请输入商品的编号和商品的名称，每次只能输入一个商品：')
    lst.append(goods)
for item in lst:
    print(item)
car = []
while True:
    flag = False
    m = input('请输入要购买的商品编号：')
    for item in lst:
        if m == item[:4]:
            car.append(item)
            print('商品已添加进入购物车！')
            flag = True
            break
    if not flag and m != 'q':
        print('不存在该商品，请重新输入：')
    if m == 'q':
        break
print('*'*40)
car.reverse()
print('购物车中的商品为：')
for item in car:
    print(item)

goods = [
    ['编号', '名称', '    品牌', '单价'],
    ['01', '电风扇', '美的', 500],
    ['02', '洗衣机', 'TCL', 1000],
    ['03', '微波炉', '老板', 400]
]
for row in goods:
    for item in row:
        print(item, end='\t\t')
    print()
price = 0
for i in range(1,4):
    goods[i][0] = '0000'+goods[i][0]
    price = '￥{0:.2f}'.format(goods[i][3])
    goods[i][3] = price
for row in goods:
    for item in row:
        print(item, end='\t\t')
    print()
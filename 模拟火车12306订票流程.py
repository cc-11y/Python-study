train = [
    ['车次', '    出发站-到达站', '出发时间', '到达时间', '历时时长'],
    ['G1569', '北京南-天津南', '18:06', '18:39', '00:33'],
    ['G1567', '北京南-天津南', '18:15', '18:49', '00:34'],
    ['G8917', '北京南-天津西', '18:20', '19:19', '00:59'],
    ['G203', '北京南-天津南', '18:35', '19:09', '00:34']
]
for row in train:
    for item in row:
        print(item, end='\t\t')
    print()
ticket = []
flag = True
while flag:
    flag = False
    turn = input('请输入要购买的车次：')
    for i in range(len(train)):
        if train[i][0] == turn:
            ticket.append(train[i])
            flag = False
            break
        elif train[i][0] != turn:
            flag = True
            continue
    else:
        print('不存在该车次，请重新输入！')
human = input('请输入乘车人，如果是多为乘车人请使用逗号隔开：')
print(ticket)

#用字典-列表综合创建会更好
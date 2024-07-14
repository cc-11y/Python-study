ku = []
place = []
for i in range(3):
    car_number = input('请输入车牌号：')
    ku.append(car_number)
    place.append(car_number[0])
dic = {key: value for key, value in zip(ku,place)}
for key in dic:
    print('{0} 归属地是：{1}'.format(key,  dic[key]))
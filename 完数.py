
for i in range(1,1000):
    s=0
    for j in range(1,i):
        if i%j == 0 :
            s += j
    if i == s:
        print(i,'是完数')


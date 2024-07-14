lst=[88, 89, 99, 90, 00, 98]
s=0
print(lst)
for i in range(6) :
    s=lst[i]
    if s//10 == 8 or s//10 == 9:
        s+=19*100
        lst[i]=s
    else:
        s+=20*100
        lst[i] = s
print(lst)

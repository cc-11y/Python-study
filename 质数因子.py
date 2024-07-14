m=int(input('请输入一个正整数：'))
n=2
lst=[]
while m!=n:
    if m%n==0:
        lst.append(n)
        m/=n
    else:
        n+=1
lst.append(int(m))
print(lst)


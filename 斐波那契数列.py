lst=[1,1]
n=len(lst)
m=int(input('请输入斐波那契数列的项数：'))
while n!=m :
   lst.append((int(lst[n-2]+int(lst[n-1]))))
   print(lst)
   n+=1
   print(lst[n-1])
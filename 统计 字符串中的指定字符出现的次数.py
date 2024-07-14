s = 'HelloPython,HelloJava,hellophp'
n = input('请输入要统计的字符：')
s = s.lower()
num = s.count(n)
print('{0}在{1}出现{2}次'.format(n, s, num))

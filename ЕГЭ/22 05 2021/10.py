with open(r'ЕГЭ\22 05 2021\10-1 (1).txt', mode='r', encoding='1251') as f:
    text = f.read()
lst = ['я ','Я ','ты ','Ты ','он ','Он ','она ','Она ','Оно ','оно ']
sums = []
for i in lst:
    sums.append(text.count(i))
print(sums, sum(sums))
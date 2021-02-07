abc = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"

word = 'мамасобираетсынуобедвшколу'#input()
shifter = 16
shifter = shifter % 32

ans = ""
for i in word:
    ans += abc[abc.index(i) + shifter]

f = open(r'C:\Users\Dmitry\Documents\Projects\Python\Алгоритмы\Школьное Шифрование\Цезарь\new.txt',mode='w',encoding='utf-8')
f.write(ans)
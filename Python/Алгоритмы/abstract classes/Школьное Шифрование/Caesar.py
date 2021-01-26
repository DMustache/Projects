Salphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"
Balphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
word = input()
shifter = int(input())
shifter %= 32
ans = ""
for i in word:
    if i.islower:
        ans += Salphabet[Salphabet.index(i) + shifter]
    elif i.isalpha:
        ans += Balphabet[Balphabet.index(i) + shifter]
    else:
        ans += " "
print(ans)
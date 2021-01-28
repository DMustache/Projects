from typing import Counter

alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"
word = input()
key = input()

def checker(ans, key):
    if ans.count(key) > 0:
        return True

for i in range(32):
    ans = ""
    for symbol in word:
        ans += alphabet[alphabet.index(symbol, len(alphabet) // 2 ,len(alphabet)) + i]
    if checker(ans, key) == True:
        print(word)
    break
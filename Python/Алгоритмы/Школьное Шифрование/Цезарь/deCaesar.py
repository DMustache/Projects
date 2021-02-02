alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"
word = input()
key = input()

answer = ''
counter = 0
for i in range(32):
    ans = ""
    for symbol in word:
        ans += alphabet[alphabet.index(symbol) + i]
    if key in ans:
        counter += 1
        if counter == 0:
            answer = ans
            move = i
if counter > 1 or counter == 0:
    print('ERROR')
elif counter == 1:
    print(counter)
    print(answer)
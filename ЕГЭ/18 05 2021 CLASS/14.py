num = '79766443076871347601979'
ans = ''
for i in range(len(num), 0, -1):
    ans += f' + {num[len(num) - i]} * 9 ** {i - 1}'
    print(f'+ {num[len(num) - i]} * 9 ** {i - 1}')
print(ans, len(num))
print('7972351312044692422809'.count('0'))
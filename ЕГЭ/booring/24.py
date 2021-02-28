answer = 0
for i in range(32):
    for j in range(32):
        if i != j and i < j:
            answer += 1
print(answer)
out_arr = []
count = 0
for i in range(32):
    for j in range(32):
        if i % 2 != j % 2 and i < j:
            count += 1
            out_arr.append(f"{i} и {j}")
print(count)
for elem in out_arr:
    print(elem)
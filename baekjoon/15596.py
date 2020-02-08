def s():
    list_a = set()
    for i in range(1, 10001):
        res = 0
        list = str(i // 10)
        for v in list:
            res += int(v)
        res = res + i + (i % 10)
        list_a.add(res)
    return list_a

list_a = s()

for i in range(1, 10001):
    if i not in list_a:
        print(i)
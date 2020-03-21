case = int(input())

for i in range(case):
    input_string = input()
    n, string = input_string.split()
    res = ""
    for s in string:
        res += s * int(n)
    print(res)


import sys
first = int(sys.stdin.readline())
block = []

for i in range(first):
    block.append(int(sys.stdin.readline()))

def see(n):
    n.reverse()
    count = 0
    tmp = n[0]

    for i in range(len(n) - 1):
        if tmp < n[i + 1]:
            count += 1
            tmp = n[i + 1]
    return count + 1

print(see(block))
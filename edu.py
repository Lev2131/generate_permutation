
def check(a, value):
    for x in a:
        if x == value:
            return False
    return True

# c из n по k
def generate_permutation(n, m, data = None):
    if not(data):
        data = []
    if m == 0:
        print(*data)
        return
    for i in range(1, n + 1):
        if check(data, i):
            data.append(i)
            generate_permutation(n, m - 1, data)
            data.pop()



n, m = map(int, input().split())
generate_permutation(n, m)
res = []
nums = [num for num in range(245182, 790572 + 1)]
def ff(x):
    sx = str(x)
    l = len(sx)
    for i in range(1, l:
        if sx[i] < sx[i-1]:
            return False
    for i in range(1, l):
        if sx[i] == sx[i-1]:
            return True
    return False
res = list(filter(ff, nums))
print(len(res))
print(res)
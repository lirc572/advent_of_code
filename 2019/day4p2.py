res = []
nums = [num for num in range(245182, 790572 + 1)]
def f1(x):
    sx = str(x)
    l = len(sx)
    for i in range(1, l):
        if sx[i] < sx[i-1]:
            return False
    for i in range(1, l):
        if sx[i] == sx[i-1]:
            return True
    return False
def f2(x):
    sx = str(x)
    if sx[0] == sx[1]:
        if sx[2] != sx[1]:
            return True
    if sx[-1] == sx[-2]:
        if sx[-3] != sx[-2]:
            return True
    for i in range(3):
        if sx[i+1] == sx[i+2]:
            if sx[i] != sx[i+1] and sx[i+1] != sx[i+3]:
                return True
    return False
res1 = list(filter(f1, nums))
res = list(filter(f2, res1))
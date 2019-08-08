def cumsum(t):
    for i in range(1, len(t)):
        t[i] = t[i] + t[i-1]
    return t

t = [1, 2, 3, 4, 5, 6]
print cumsum(t)

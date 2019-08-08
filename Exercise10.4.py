def middle(t):
    t.pop(0)
    t.pop(len(t)-1)
    return t

t = [1, 2, 3, 4]
print middle(t)


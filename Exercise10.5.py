def is_sorted(t):
    t2 = sorted(t)
    if t == t2:
        return True
    else:
        return False

print is_sorted([1, 2, 2])
print is_sorted(['b', 'a'])

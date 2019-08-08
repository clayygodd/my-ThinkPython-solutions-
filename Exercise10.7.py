def has_duplicates(t):
    i = 0
    ts = t[:]
    while i < len(t):
        a = ts.pop(0)
        if a in ts:
            return True
        else:
            i += 1
    return False

t = [1, 3, 7, 2, 6, 2]
print has_duplicates(t)
    

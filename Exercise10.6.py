def is_anagram(a, b):
    ta = sorted(list(a))
    tb = sorted(list(b))
    if ta == tb:
        return True
    else:
        return False

print is_anagram('abnfg', 'bafnd')

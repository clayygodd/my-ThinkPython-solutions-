def open_file(f):
    fin = open(f)
    t = []
    for word in fin:
        t.append(word.strip())
    return t
    
def in_bisect(t, word):
    ts = sorted(t)
    while len(ts) > 1:
        if word in ts[0:len(ts)//2]:
            return True
        else:
            del ts[0:len(ts)//2]
            in_bisect(ts, word)
    if word in ts:
        return True
    else:
        return False


print in_bisect(open_file('words.txt'), 'egg')
        

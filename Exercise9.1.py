fin = open('words.txt')


def has_no_e(w):
    if 'e' not in w:
        return True
    else:
        return False

total = 0.0
total2 = 0.0
for word in fin:
    if has_no_e(word):
        
        total2 += 1
        total += 1
    else:
        total += 1


print (total2/total)

        



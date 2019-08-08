fin = open('words.txt')
dic = dict()
for word in fin:
    dic[word] = 1

print dic

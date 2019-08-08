def nested_sum(t):
    result = []
    for i in range(0, len(t)):
        result += t[i]
    return sum(result)

t = [[1, 2], [3], [4, 5, 6]]
print nested_sum(t)

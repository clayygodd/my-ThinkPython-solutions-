def cal_birth(n):
    k = (1.0/365)**n
    pa = 1.0
    for i in range(0, n):
        pa = (365-i)*pa
        i += 1
    return 1-k*pa

print cal_birth(75)

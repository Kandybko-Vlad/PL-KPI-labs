l = [0, 1]
ll = len(l)
while(ll < 12):
    for i in range(100):
        a = l[i] + l[i+1]
        l.append(a)
def getMax(l):
    if not l:
        return None
    else:

        res = l[0]                  # assume l[0] is the max
        for i in range(1, len(l)):  # iterate through index 1 to last
            if l[i] > res:           # check whether current element is greater than res
                res = l[i]          # if current element is greater than res ,update res to current
        return res
    
    
    

def getSecMax(l):
    if len(l) <= 1:
        return None
    lar = getMax(l)
    slar = None

    for x in l:

        if x != lar:
            if slar == None:
                slar = x
            else:
                slar = max(x, slar)
    return slar

l = [int(x) for x in input().split()]
print(getSecMax(l))


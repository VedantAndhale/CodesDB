def getMax(l):
    for x in l:         # iterate for each element
        for y in l:     # iterrate to compare with each element
            if y > x:
                break
        else:           # if loop is exited naturally, no larger element found
            return x
    return None

# O(n2)




l = [int(x) for x in input().split()]
print(getMax(l))
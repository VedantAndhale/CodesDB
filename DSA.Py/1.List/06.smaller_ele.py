def getSmaller(l,x):
    
    res = []
    
    for e in l:
        if e<x:
            res.append(e)
    
    return res
    
l = [8,100,20,40,3,7]
x = 10
print(getSmaller(l,x))
            
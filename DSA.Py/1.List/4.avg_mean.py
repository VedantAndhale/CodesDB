def average(l):
    
    sum = 0
    for x in l:
        sum = sum+x
        
    n = len(l)
    return sum/n

l = [10,20,30,40]

print(average(l))


def fun_average(l):
    return sum(l)/len(l)

print(fun_average(l))
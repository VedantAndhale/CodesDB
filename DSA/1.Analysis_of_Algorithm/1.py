def function1(n):
    return n*(n+1)/2

def function2(n):
    sum1=0;
    for i in range(1,n+1):
        sum1=sum1+i
    return sum1
    
def function3(n):
    sum1=0;
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum1=sum1+1
    return sum1
    
n=5
print(function1(n))
print(function2(n))
print(function3(n))
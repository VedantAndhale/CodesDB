l = {10,20,3,4,10,20,7,3}

s1 = {x for x in l if x%2==0 }
s2 = {x for x in l if x%2!=0 }  # set comprehension

print(s1)
print(s2)


l1 = [1,3,4,2,5]

d1 = {x:x**3 for x in l1}

d2 = {x:f"ID{x}" for x in range(5)} # dictionary comprehension
print(d2)


l2 = [101,103,102]
l3 = ['gfg','ide','corse']

d3 = {l2[i]:l3[i] for i in range(len(l2)) }   # dictionary comprehension

print(d3)


d4 = dict(zip(l2,l3))

print(d4)






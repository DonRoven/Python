import random
n = 10
list1 = [random.randint(1, n) for i in range(n)]
list2 = [random.randint(1, n) for i in range(n)]

cities = {}
for k, v in zip(list1,list2):
    if k in cities:
        cities[k].append(v) 
    else:
        cities[k] = [v]
    
print (cities)
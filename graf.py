import random

def create_citis(city1,city2, n):
    list1 = [random.randint(1, n) for i in range(n*2)]
    list2 = [random.randint(1, n) for i in range(n*2)]
    return (list1, list2)

def cities_path(list1, list2):
    cities = {}
    for k, v in zip(list1,list2):
        if k in cities:
            cities[k].append(v) 
        else:
            cities[k] = [v]
    for k, v in zip(list1,list2):
        if k not in cities:
            if v in cities:
                cities[v].append(k) 
            else:
                cities[v] = [k]
    return (cities)

def check_direct_path(city1, city2, list1, list2):
    if x == list1[i] and y == list2[i] or x == list2[i] and y == list1[i]:
        return True
        print (city1, city2)
    else:
        return False

def check_path(city1, city2, cities):
    path = []
    path += [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_pach(graf, start, end)
            if newpath:
                return newpath
    return None



print (create_citis(6, 12, 20))

import random

def create_citis(n):
    list1 = [random.randint(1, n) for i in range(n*3)]
    list2 = [random.randint(1, n) for i in range(n*3)]
    return (list1, list2)

def cities_network(list1, list2):
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
    if city1 == list1[i] and city2 == list2[i] or city1 == list2[i] and city2 == list1[i]:
        return True
        print (city1, city2)
    else:
        return False

def check_path(city1, city2, cities):
    path = []
    path += [city1]
    if city1 == city2:
        return path
    if not cities.has_key(city1):
        return None
    for node in cities[city1]:
        if node not in path:
            newpath = check_path(city1, city2, cities)
            if newpath:
                return newpath
    return None

print check_path(8, 15, cities_network(*create_citis(20)))


def euclidean_dist(x, y):
    if (len(x)==0 or len(y)==0):
        raise ValueError("lengths must not be zero")
    if len(x)!=len(y):
        raise ValueError("lengths must be equal")
    index = 0
    sum_res = 0
    for feature in x:
        each_dist = abs(x[index] - y[index])**2
        sum_res += each_dist
        index += 1
    res = sum_res**(1/2)
    return res

def manhattan_dist(x, y):
    if (len(x)==0 or len(y)==0):
        raise ValueError("lengths must not be zero")
    if len(x)!=len(y):
        raise ValueError("lengths must be equal")
    index = 0
    sum_res = 0
    for feature in x:
        each_dist = abs(x[index] - y[index])
        sum_res += each_dist
        index += 1
    return sum_res

def jaccard_dist(x, y):
    if (len(x)==0 or len(y)==0):
        raise ValueError("lengths must not be zero")
    # list_of_lists = [x, y]
    # shorter_list = min(list_of_lists, key=len)
    # longer_list = max(list_of_lists, key=len)
    # intersection = [x for x in shorter_list if x in longer_list]
    intersection = set(x).intersection(set(y))
    union = set(x).union(set(y))
    return 1 - (len(intersection)/len(union))

def cosine_sim(x, y):
    if (len(x)==0 or len(y)==0):
        raise ValueError("lengths must not be zero")
    if len(x)!=len(y):
        raise ValueError("lengths must be equal")
    index = 0
    numerator = 0
    x_sum_euclidean_norm = 0
    y_sum_euclidean_norm = 0
    for feature in x:
        each_product = x[index]*y[index]
        numerator += each_product
        x_sum_euclidean_norm += x[index]**2
        y_sum_euclidean_norm += y[index]**2
        index += 1
    x_euclidean_norm = x_sum_euclidean_norm**(1/2)
    y_euclidean_norm = y_sum_euclidean_norm**(1/2)
    return numerator/(x_euclidean_norm*y_euclidean_norm)

# Feel free to add more

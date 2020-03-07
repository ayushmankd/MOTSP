import math
def fun1(x):
    val = x ** 2
    return val
def fun2(x):
    val = (x-2) ** 2
    return val
def index_of(a,list):
    for i in range(0,len(list)):
        if list[i] == a:
            return i
    return -1
def sort_by_values(list1, values):
    sorted_list = []
    while(len(sorted_list)!=len(list1)):
        if index_of(min(values),values) in list1:
            sorted_list.append(index_of(min(values),values))
        values[index_of(min(values),values)] = math.inf
    return sorted_list
# I use Max - Min of only the Current Front
def CrowdingDistance(front, population):
    distance = [0.0 for i in front]
    fun1_values = [] 
    fun2_values = []
    for i in front:
        fun1_values.append(fun1(population[i]))
        fun2_values.append(fun2(population[i]))
    cost_indices = sorted(
        range(len(fun1_values)), 
        key=lambda k: fun1_values[k],
        reverse=True
    )
    dist_indices = sorted(
        range(len(fun2_values)), 
        key=lambda k: fun2_values[k],
        reverse=True
    )
    diff_cost_max = max(fun1_values) - min(fun1_values)
    diff_dist_max = max(fun2_values) - min(fun2_values)
    distance[cost_indices[0]] = math.inf
    distance[cost_indices[-1]] = math.inf
    i = 1
    while i < (len(front)-1):
        distance[cost_indices[i]] += (fun1_values[cost_indices[i-1]] - fun1_values[cost_indices[i+1]]) / diff_cost_max 
        i += 1
    distance[dist_indices[0]] = math.inf
    distance[dist_indices[-1]] = math.inf
    i = 1
    while i < (len(front)-1):
        distance[dist_indices[i]] += (fun2_values[dist_indices[i-1]] - fun2_values[dist_indices[i+1]]) / diff_dist_max 
        i += 1
    return distance
# He Takes Max of all fitness values - Min of all fitness values
# def crowding_distance(values1, values2, front):
#     distance = [0 for i in range(0,len(front))]
#     sorted1 = sort_by_values(front, values1[:])
#     sorted2 = sort_by_values(front, values2[:])
#     distance[0] = 4444444444444444
#     distance[len(front) - 1] = 4444444444444444
#     for k in range(1,len(front)-1):
#         distance[k] = distance[k]+ (values1[sorted1[k+1]] - values1[sorted1[k-1]])/(max(values1)-min(values1))
#     for k in range(1,len(front)-1):
#         distance[k] = distance[k]+ (values2[sorted2[k+1]] - values2[sorted2[k-1]])/(max(values2)-min(values2))
#     return distance

# fronts = [[3, 4], [0, 1, 2]]
# fun1_values = []
# fun2_values = []
# population = [2, 1, 0, 4, -1]
# for i in population:
#     fun1_values.append(fun1(i))
#     fun2_values.append(fun2(i))
# myCD = []
# hisCD = []
# for front in fronts:
#     myCD.append(CrowdingDistance(front, population))
#     hisCD.append(crowding_distance(fun1_values, fun2_values, front))
# for newE in myCD:
#     print (newE)
# print ("---")
# for newH in hisCD:
#     print (newH)
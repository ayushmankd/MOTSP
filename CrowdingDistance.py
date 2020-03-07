import math
distance_matrix = [
    [0, 81, 72, 55, 81, 3],
    [81, 0, 3, 44, 9, 40],
    [72, 3, 0, 87, 72, 21],
    [55, 44, 87, 0, 67, 25],
    [81, 9, 77, 67, 0, 93],
    [3, 40, 21, 25, 93, 0]
]
cost_matrix = [
    [0, 82, 14, 14, 43, 47],
    [82, 0, 61, 76, 29, 47],
    [14, 61, 0, 29, 31, 51],
    [14, 76, 29, 0, 78, 67],
    [43, 29, 31, 78, 0, 28],
    [47, 47, 51, 67, 28, 0]
]


def Evaluate(tour, matrix):
    value = 0
    i = 0
    while i < (len(tour)-1):
        value += matrix[tour[i]][tour[i+1]]
        i += 1
        pass
    value += matrix[tour[-1]][tour[0]]
    return value

def CrowdingDistance(front, population):
    distance = [0.0 for i in front]
    fitness_cost_values = [] 
    fitness_dist_values = []
    for i in front:
        fitness_cost_values.append(Evaluate(population[i], cost_matrix))
        fitness_dist_values.append(Evaluate(population[i], distance_matrix))
    cost_indices = sorted(
        range(len(fitness_cost_values)), 
        key=lambda k: fitness_cost_values[k],
        reverse=True
    )
    dist_indices = sorted(
        range(len(fitness_dist_values)), 
        key=lambda k: fitness_dist_values[k],
        reverse=True
    )
    # Should we take maximum and minimum fitness value possible of the current front
    # or the whole population?
    diff_cost_max = max(fitness_cost_values) - min(fitness_cost_values)
    diff_dist_max = max(fitness_dist_values) - min(fitness_dist_values)
    distance[cost_indices[0]] = math.inf
    distance[cost_indices[-1]] = math.inf
    i = 1
    while i < (len(front)-1):
        distance[cost_indices[i]] += (fitness_cost_values[cost_indices[i-1]] - fitness_cost_values[cost_indices[i+1]]) / diff_cost_max 
        i += 1
    distance[dist_indices[0]] = math.inf
    distance[dist_indices[-1]] = math.inf
    i = 1
    while i < (len(front)-1):
        distance[dist_indices[i]] += (fitness_dist_values[dist_indices[i-1]] - fitness_dist_values[dist_indices[i+1]]) / diff_dist_max 
        i += 1
    return distance
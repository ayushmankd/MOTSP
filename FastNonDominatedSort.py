# Fast Non Dominated Sort of Population
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

def CheckDomination(solution_1, solution_2):
    solution_1_cost = Evaluate(solution_1, cost_matrix)
    solution_1_dist = Evaluate(solution_1, distance_matrix)
    solution_2_cost = Evaluate(solution_2, cost_matrix)
    solution_2_dist = Evaluate(solution_2, distance_matrix)

    dist_comp_eql_p = solution_1_dist <= solution_2_dist
    cost_comp_eql_p = solution_1_cost <= solution_2_cost
    dist_comp_p = solution_1_dist < solution_2_dist
    cost_comp_p = solution_1_cost < solution_2_cost

    dist_comp_eql_q = solution_1_dist >= solution_2_dist
    cost_comp_eql_q = solution_1_cost >= solution_2_cost
    dist_comp_q = solution_1_dist > solution_2_dist
    cost_comp_q = solution_1_cost > solution_2_cost

    if ((dist_comp_eql_p and cost_comp_eql_p) and (dist_comp_p or cost_comp_p)):
        return 1
    elif ((dist_comp_eql_q and cost_comp_eql_q) and (dist_comp_q or cost_comp_q)):
        return -1
    else:
        return 0
    

def FastNonDominatedSort(population):
    population_data = {}
    fronts = []
    solution_p = 0
    while solution_p < len(population):
        sols_dom_by_p = []
        dom_count_p = 0
        solution_q = 0
        while solution_q < len(population):
            dom_p_q = CheckDomination(population[solution_p], population[solution_q])
            # if p dominates q
            if dom_p_q == 1:
                sols_dom_by_p.append(solution_q)
            # if q dominates p
            elif dom_p_q == -1:
                dom_count_p += 1
            solution_q += 1
        population_data[solution_p] = {
            "dominates": sols_dom_by_p,
            "dominationCount": dom_count_p,
        }
        solution_p += 1
    while len(population_data):
        new_front = []
        for i in population_data:
            if population_data[i]["dominationCount"] == 0:
                new_front.append(i)
        for j in new_front:
            for submissive in population_data[j]["dominates"]:
                population_data[submissive]["dominationCount"] -= 1
            del population_data[j]
        fronts.append(new_front)
    return fronts

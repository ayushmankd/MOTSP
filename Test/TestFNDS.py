# Fast Non Dominated Sort of Population
def fun1(x):
    val = x ** 2
    return val
def fun2(x):
    val = (x-2) ** 2
    return val
def CheckDomination(solution_1, solution_2):
    solution_1_fun1 = fun1(solution_1)
    solution_1_fun2 = fun2(solution_1)
    solution_2_fun1 = fun1(solution_2)
    solution_2_fun2 = fun2(solution_2)

    dist_comp_eql_p = solution_1_fun1 <= solution_2_fun1
    cost_comp_eql_p = solution_1_fun2 <= solution_2_fun2
    dist_comp_p = solution_1_fun1 < solution_2_fun1
    cost_comp_p = solution_1_fun2 < solution_2_fun2

    dist_comp_eql_q = solution_1_fun1 >= solution_2_fun1
    cost_comp_eql_q = solution_1_fun2 >= solution_2_fun2
    dist_comp_q = solution_1_fun1 > solution_2_fun1
    cost_comp_q = solution_1_fun2 > solution_2_fun2

    if ((dist_comp_eql_p and cost_comp_eql_p) and (dist_comp_p or cost_comp_p)):
        return 1
    elif ((dist_comp_eql_q and cost_comp_eql_q) and (dist_comp_q or cost_comp_q)):
        return -1
    else:
        return 0
    
# Returns Array of Arrays
# Inside Array contains Indices of solutions in the population having
# same Rank
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

# # Correct one by Someone Else
# def fast_non_dominated_sort(values1, values2):
#     S=[[] for i in range(0,len(values1))]
#     front = [[]]
#     n=[0 for i in range(0,len(values1))]
#     rank = [0 for i in range(0, len(values1))]

#     for p in range(0,len(values1)):
#         S[p]=[]
#         n[p]=0
#         for q in range(0, len(values1)):
#             if (values1[p] > values1[q] and values2[p] > values2[q]) or (values1[p] >= values1[q] and values2[p] > values2[q]) or (values1[p] > values1[q] and values2[p] >= values2[q]):
#                 if q not in S[p]:
#                     S[p].append(q)
#             elif (values1[q] > values1[p] and values2[q] > values2[p]) or (values1[q] >= values1[p] and values2[q] > values2[p]) or (values1[q] > values1[p] and values2[q] >= values2[p]):
#                 n[p] = n[p] + 1
#         if n[p]==0:
#             rank[p] = 0
#             if p not in front[0]:
#                 front[0].append(p)

#     i = 0
#     while(front[i] != []):
#         Q=[]
#         for p in front[i]:
#             for q in S[p]:
#                 n[q] =n[q] - 1
#                 if( n[q]==0):
#                     rank[q]=i+1
#                     if q not in Q:
#                         Q.append(q)
#         i = i+1
#         front.append(Q)

#     del front[len(front)-1]
#     return front

# test_fronts = FastNonDominatedSort([2, 1, 0, 4, -1])
# for i in test_fronts:
#     print (i)
# print ("------")
# fun1_values = []
# fun2_values = []
# population = [2, 1, 0, 4, -1]
# for i in population:
#     fun1_values.append(fun1(i))
#     fun2_values.append(fun2(i))
# good_fronts = fast_non_dominated_sort(fun1_values, fun2_values)
# for i in good_fronts:
#     print (i)
# Solve Multiobjective Traveling Salesman Problem
# Using NSGA-II
import random
import FastNonDominatedSort
import CrowdingDistance
import GenerateOffspring
import Selection
import Input
import matplotlib.pyplot as plt
# import matplotlib as mlt
# Generate Initial Population, by taking population size and num cities as parameters
def GeneratePopulation(size, num_cities):
    permutations = []
    for i in range(size):
        tour = [j for j in range(num_cities)]
        random.shuffle(tour)
        permutations.append(tour)
        pass
    return permutations

def Evaluate(tour, matrix):
    value = 0
    i = 0
    while i < (len(tour)-1):
        value += matrix[tour[i]][tour[i+1]]
        i += 1
        pass
    value += matrix[tour[-1]][tour[0]]
    return value
distance_matrix, cost_matrix = Input.getInput()
if __name__ == '__main__':
    population_size = 4
    num_cities = 6
    num_generations = 30
    # Initial Population
    parents = GeneratePopulation(population_size, num_cities)
    # Generate Children by Selection, Crossover and Mutation
    children = GenerateOffspring.GenerateOffspring(parents)
    population = parents[:]
    # NewPopulation = Parents + Children
    population.extend(children)
    gen_num = 0
    while gen_num < num_generations:
        children = GenerateOffspring.GenerateOffspring(parents)
        population = parents[:]
        # NewPopulation = Parents + Children
        population.extend(children)
        # print (gen_num, ":", len(population))
        # for i in population:
        #     print (i)
        fronts = FastNonDominatedSort.FastNonDominatedSort(population)
        for i in fronts:
            print (i)
        print ("--")
        new_parents = []
        for front in fronts:
            if (len(front) + len(new_parents)) <= population_size:
                for i in front:
                    # print (population[i])
                    new_parents.append(population[i])
            else:
                distance = CrowdingDistance.CrowdingDistance(front, population)
                indices = sorted(
                    range(len(distance)), 
                    key=lambda k: distance[k],
                    reverse=True
                )
                i = 0
                while len(new_parents) != population_size:
                    new_parents.append(population[indices[i]])
                    i += 1
        parents = new_parents[:]
        gen_num += 1
        # function1 = []
        # function2 = []
        # # print ("Sol")
        # for i in parents:
        #     # print (i)
        #     function1.append(Evaluate(i, distance_matrix))
        #     function2.append(Evaluate(i, cost_matrix))
        # plt.title("Generation "+str(gen_num))
        # plt.xlabel('Distance', fontsize=15)
        # plt.ylabel('Cost', fontsize=15)
        # plt.scatter(function1, function2)
        # if gen_num != num_generations:
        #     plt.pause(3)
        # else:
        #     plt.show()
        #     pass
        pass
    function1 = []
    function2 = []
    # print ("Sol")
    for i in parents:
        # print (i)
        function1.append(Evaluate(i, distance_matrix))
        function2.append(Evaluate(i, cost_matrix))
    plt.title("Generation "+str(gen_num))
    plt.xlabel('Distance', fontsize=15)
    plt.ylabel('Cost', fontsize=15)
    plt.scatter(function1, function2)
    plt.show()
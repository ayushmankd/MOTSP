import random
# Python Program for Selection of Parents
def Selection(population):
    a, b = random.sample(range(len(population)), 2)
    parentA = population[a]
    parentB = population[b]
    return parentA, parentB
# Permutation Swap Mutation
import random
def Mutation(chromosome):
    # Generate 2 Random Points
    a, b = sorted(random.sample(range(len(chromosome)), 2))
    chromosome[a], chromosome[b] = chromosome[b], chromosome[a]
    return chromosome


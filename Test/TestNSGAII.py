import random
def GenerateInitialPopulation(low, high, pop_size):
    population = random.sample(range(low, high+1), pop_size)
    return population
gen_itr = 0
num_itr = 20
while gen_itr < num_itr:
    
    gen_itr += 1
    pass
import random
def Mutation(chromosome):
    parent1Bin = "{0:b}".format(chromosome)
    parent1BinArr = list(map(int, parent1Bin))
    parent1BinArrLen = len(parent1BinArr)
    a, b = random.sample(range(parent1BinArrLen), 2)
    child1 = parent1BinArr[:]
    child1[a], child1[b] = child1[b], child1[a]
    child1Str = "".join(map(str, child1))
    return (int(child1Str, 2)) 

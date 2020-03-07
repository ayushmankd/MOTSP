import random
# Takes 2 Numbers and Return Two Different Numbers
def Crossover(parent1, parent2):
    parent1Bin = "{0:b}".format(parent1)
    parent2Bin = "{0:b}".format(parent2)
    parent1BinArr = list(map(int, parent1Bin))
    parent2BinArr = list(map(int, parent2Bin))
    parent1BinArrLen = len(parent1BinArr)
    parent2BinArrLen = len(parent2BinArr)
    if parent1BinArrLen < parent2BinArrLen:
        i = 0
        while i < (parent2BinArrLen-parent1BinArrLen):
            parent1BinArr.insert(0, 0)
            i += 1
            pass
        pass
    else:
        i = 0
        while i < (parent1BinArrLen-parent2BinArrLen):
            parent2BinArr.insert(0, 0)
            i += 1
            pass
        pass
    cross_point = random.randint(0, len(parent1BinArr))
    child1 = parent1BinArr[:cross_point]
    child1.extend(parent2BinArr[cross_point:])
    child2 = parent2BinArr[:cross_point]
    child2.extend(parent1BinArr[cross_point:])
    child1Str = "".join(map(str, child1))
    child2Str = "".join(map(str, child2))
    return (int(child1Str, 2), int(child2Str, 2))
# Order - 1 Crossover
import random
def Crossover(parent1, parent2):
    if len(parent1) != len(parent2):
        return False
    else:
        child1 = [None for i in parent1]
        child2 = [None for i in parent2]

        # Generate 2 Random Points
        a, b = sorted(random.sample(range(len(parent1)+1), 2))

        # Indices to be Swapped
        unfilled_indinces = []
        for i in range(a):
            unfilled_indinces.append(i)
            pass
        for i in range(b, len(parent1)):
            unfilled_indinces.append(i)
            pass

        # Copy the Contents as it is
        for i in range(a, b):
            child1[i] = parent1[i]
            child2[i] = parent2[i]
            pass

        # Swap from Parent2 to Child1
        ind = 0
        for i in parent2:
            if i not in child1:
                child1[unfilled_indinces[ind]] = i
                ind += 1
            pass

        # Swap from Parent1 to Child2
        ind = 0
        for i in parent1:
            if i not in child2:
                child2[unfilled_indinces[ind]] = i
                ind += 1
            pass
        return (child1, child2)

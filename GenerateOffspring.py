import Selection
import Crossover
import Mutation
def GenerateOffspring(parents):
    offspring = []
    while (len(offspring) != len(parents)):
        parentA, parentB = Selection.Selection(parents)
        childA, childB = Crossover.Crossover(parentA, parentB)
        childA = Mutation.Mutation(childA)
        childB = Mutation.Mutation(childB)
        offspring.append(childA)
        offspring.append(childB)
    return offspring
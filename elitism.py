from evaluate import *
import random
def WeakParent(current_pop, parents, mutants):
    '''
    current_pop - (list) - list containing current population of fixed size
    parents - (list) - consists of two parents selected for mating
    mutants - (list) - consists of offspring which may or maynot have been mutated
    '''
    fitness = []
    tour = parents + mutants
    for chrom in tour:
        fitness.append(evaluate(chrom))
        
    ind1 = fitness.index(max(fitness))
    max1 = tour.pop(ind1)
    ind2 = fitness.index(max(fitness))
    max2 = tour.pop(ind2)
    for ohoh in tour:
        current_pop.remove(ohoh)
    current_pop.append(max1)
    current_pop.append(max2)
        
    return current_pop    
    
########################################################################    
    
def Random(current_pop, mutant):
    '''
    current_pop - (list) - list containing current population of fixed size
    mutant - (list) - consists of offspring which may or maynot have been mutated
    '''
    removee = random.sample(current_pop,1)
    current_pop.remove(removee)
    current_pop.append(mutant)
    return current_pop
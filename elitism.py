from evaluate import *
import random
def WeakParent_elitism(current_pop, parents, mutants):
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
    
def random_elitism(current_pop, mutants):
    '''
    current_pop - (list) - list containing current population of fixed size
    mutants - (list) - consists of offspring which may or maynot have been mutated
    '''
    # here selected parents 
    scapegoats = random.sample(initial_pop,2)
    for scapegoat in scapegoats:
        current_pop.remove(scapegoat)
    current_pop + mutants
    return current_pop
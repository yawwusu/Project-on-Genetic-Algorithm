import random
def UniformCrossover(mating_pool, Pc):
    '''
    mating_pool - list from the selection function
    Pc - float (0<Pc<1) - Probability of crossover
    '''
    [parent1,parent2] = random.sample(mating_pool,2)
    
    offspring1 = parent1[:]
    offspring2 = parent2[:]
    mask = [round(random.uniform(0,1)) for i in range(4)]
    ind = 0
    for j in range(4):
        if mask[j] == 1 and random.uniform(0,1) < Pc:
            offspring1[ind] = parent2[ind]
            offspring2[ind] = parent1[ind]
        ind += 1
    return (offspring1,offspring2)
    
    
def OnePointCrossover(mate_pool,Pc):
    [parent1,parent2] = random.sample(mate_pool,2)
    offspring1 = parent1
    offspring2 = parent2
    
    mask = random.randint(1,4)
    if random.uniform(0,1) < Pc:
        for j in range(mask-1):
    
            offspring1[j] = parent2[j]
            offspring2[j] = parent1[j]
    return offspring1,offspring2
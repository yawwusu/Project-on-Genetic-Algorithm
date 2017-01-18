#All necessary functions
from numpy import *
import random
import math

#Initialization function definition
def initialize(pop,size):
    '''
    pop - (list) A list containing all chromosomes
    size - (int) Representing the size of the initial population
    '''
    import random
    initial_pop = random.sample(pop,size)
    return initial_pop
    
    
#Evaluation function definition
def evaluate(initial_pop, dist_mat= 'Data/c.csv', serv_mat = 'Data/x.csv', potential = 'Data/d.csv'):
    '''
    initial_pop - list containing all chromosomes
    dist_mat - csv file containing distance matrix
    serv_mat - csv file containing service matrix 
    potential - csv file containing potentials for the nodes
    '''
    #Reading in csv files
    c = loadtxt(dist_mat, delimiter = ',')
    x = loadtxt(serv_mat, delimiter = ',')
    d = loadtxt(potential,delimiter = ',')
    no_chromosomes = len(initial_pop)
    count = 0
    fitness = []
    while count < no_chromosomes:
        total = 0
        for i in initial_pop[count]:
            for j in initial_pop[count]:
                total += math.exp(-1*c[i-1][j-1])*x[i-1][j-1]*d[i-1]  
        fitness.append(total)
        count += 1
    return fitness
    
#helper function for selection function
def inside(range_dict, val):
    '''
    This is a helper function for the selection function
    range_dict - (dict) range dictionary with mapping of fitness values and corresponding chromosome
    val - (float) a value which will 
    '''
    for item in range_dict.keys():
        if val >= item[0] and val < item[1]:
            return range_dict[item]


#Selection Function definition
def RouletteWheelSelection(chromosome,fitness,n=2):
    '''
    chromosome - list containing chromosomes
    fitness - list containing fitness values of chromosomes in corresponding index
    n - int : number of elements desired in mating pool
    '''
    sum_fitness = sum(fitness)
    range_dict = {}
    mating_pool = []
    so_far = 0
    count = 0
    while count < len(fitness):
        x,y = so_far,so_far+fitness[count]
        range_dict[x,y] = chromosome[count]
        so_far += fitness[count]
        count += 1

    for i in range(n):
        rnd = random.uniform(0.0,sum_fitness) 
        temp = inside(range_dict,rnd)
        mating_pool.append(temp)
    return mating_pool
        
#Crossover function definition
def UniformCrossover(mating_pool, Pc):
    '''
    mating_pool - list from the selection function
    Pc - float (0<Pc<1) - Probability of crossover
    '''
    [parent1,parent2] = random.sample(mating_pool,2)
    
    offspring1 = parent1[:]
    offspring2 = parent2[:]
    if random.uniform(0,1) < Pc
        mask = [round(random.uniform(0,1)) for i in range(4)]
        ind = 0
        for j in range(4):
            if mask[j] == 1:
                offspring1[ind] = parent2[ind]
                offspring2[ind] = parent1[ind]
            ind += 1
    return [parent1,parent2],[offspring1,offspring2]
        
        
#Mutation function definition
def mutate(chromosome, Pm):
    """
    chromosome - a single chromosome string
    Pm - probability of mutation
    """
    if random.uniform(0,1) < Pm:
        i = random.randrange(0,4)
        ran = get_good_gene(chromosome)
        chromosome[i] = ran
    return sorted(chromosome)

    #elitism    
def WeakParent_elitism(current_pop, parents, mutants):
    '''
    current_pop - (list) - list containing current population of fixed size
    parents - (list) - consists of two parents selected for mating
    mutants - (list) - consists of offspring which may or maynot have been mutated
    '''
    #NB: This assumes the parents are still part of the current population
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

# Helper function to find chromosome which occurs most
def max_occurs(initial_pop):
    max_num = 0
    winner = 0
    so_far = []
    for chrom in initial_pop:
        if chrom in so_far:
            continue
        else:
            current = initial_pop.count(chrom)
            so_far.append(chrom)
            if current > max_num:
                max_num = current
                winner = chrom
    return max_num,winner
    

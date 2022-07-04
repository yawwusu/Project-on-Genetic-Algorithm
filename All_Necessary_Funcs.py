#All necessary functions
from itertools import combinations
from numpy import loadtxt
import random
import math
#################################################################################
#Encoding function definition
def encode(candidates, k):
    """
    candidates - (list) - a list containing candidate nodes eg.[1,2,3]
    k - (int) - number of required terminals
    """
    combn = list(combinations(candidates,k))
    return combn
    
################################################################################
#Initialization function definition
def initialize(pop,size):
    '''
    pop - (list) A list containing all chromosomes
    size - (int) Representing the size of the initial population
    '''
    #import random
    initial_pop = random.sample(pop,size)
    return initial_pop
    
###################################################################################################################################    
#Evaluation function definition
def evaluate(initial_pop, dist_mat='Data/c.csv',serv_mat='Data/x.csv',potential='Data/d.csv',neighbours='Data/J_star.csv'):
    '''
    initial_pop - list containing all chromosomes
    dist_mat - csv file containing distance matrix
    serv_mat - csv file containing service matrix 
    potential - csv file containing potentials for the nodes
    neighbours - csv file containing neighbours for candidate nodes
    '''
    #Reading in csv files
    c = loadtxt(dist_mat, delimiter = ',')
    x = loadtxt(serv_mat, delimiter = ',')
    d = loadtxt(potential,delimiter = ',')
    J_star = loadtxt(neighbours,delimiter = ',')

    no_chromosomes = len(initial_pop)
    count = 0
    fitness = []
    while count < no_chromosomes:
        total = 0
        for i in initial_pop[count]:
            print (total)   #comment out
            for j in range(1,21):
                total += math.exp(-1*c[i-1][j-1])*x[i-1][j-1]*d[j-1]*J_star[i-1][j-1]
        fitness.append(total)
        count += 1
    return fitness

############################################################################################################        
#helper function for selection process
def inside(range_dict, val):
    '''
    This is a helper function for the selection function
    range_dict - (dict) range dictionary with mapping of fitness values and the
                    corresponding chromosome
    val - (float) a value which will 
    '''
    for item in range_dict.keys():
        if val >= item[0] and val < item[1]:
            return range_dict[item]


#Selection Function definitions
def Roulette(chromosome,fitness,n=2):
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
    #This creates the wheel
    while count < len(fitness):
        x,y = so_far,so_far+fitness[count]
        range_dict[x,y] = chromosome[count]
        so_far += fitness[count]
        count += 1

    #This selects randomly from the wheel
    for i in range(n):
        rnd = random.uniform(0.0,sum_fitness) 
        temp = inside(range_dict,rnd)
        mating_pool.append(temp)
    return mating_pool

    
def Tournament(Pop, Tour_Size , rounds = 2):
    ini_sample = random.sample(Pop , Tour_Size)
    #fitness  = []
    pool = []
    max_fit = 0
    max_chrom = 0
    for num in range(rounds):
        for chrom in ini_sample:
            fit = evaluate(chrom)
            if fit > max_fit:
                max_fit = fit
                max_chrom = chrom
        pool.append(max_chrom)
    return pool
    

#########################################################################################
#helper function for crossover and mutation functions
def get_good_candidates(chrom,candidates= [1,8,9,11,13,16,19]):
    """
    A Helper function for mutation
    chrom - (list) - a chromosome
    candidates - (list) - list containing candidate nodes
    """
    can_copy = candidates[:]
    for gene in chrom:
        can_copy.remove(gene)
    return can_copy
    
    
#Crossover function definitions
def NewCrossover(mating_pool, Pc):
    '''
    mating_pool - list from the selection function
    Pc - float (0<Pc<1) - Probability of crossover
    '''
    parents = random.sample(mating_pool,2)
    offspring = []
    for gene in parents[0]:
        if gene in parents[1]:
            offspring.append(gene)
    left = len(parents[0])-len(offspring)
    good_can = get_good_candidates(offspring)
    offspring.append(random.sample(good_can,left))
    return parents,sorted(offspring)
    
def Uniform(mating_pool, Pc):
    '''
    mating_pool - list from the selection function
    Pc - float (0<Pc<1) - Probability of crossover
    '''
    if random.uniform(0,1) < Pc:
        mating_pool = [list(i) for i in mating_pool]   #converts mating pool from tuple into list
        [parent1,parent2] = random.sample(mating_pool,2)
        
        offspring1 = parent1[:]
        offspring2 = parent2[:]
        mask = [random.randint(0,1) for i in range(4)]
        ind = 0
        for j in range(4):
            if mask[j] == 1:
                offspring1[ind] = parent2[ind]
                offspring2[ind] = parent1[ind]
            ind += 1
    return [parent1,parent2],[offspring1,offspring2]

        
def OnePoint(mate_pool,Pc):
    [parent1,parent2] = random.sample(mate_pool,2)
    offspring1 = parent1
    offspring2 = parent2
    
    mask = random.randint(1,4)
    if random.uniform(0,1) < Pc:
        for j in range(mask-1):
    
            offspring1[j] = parent2[j]
            offspring2[j] = parent1[j]
    return offspring1,offspring2
################################################################################ 
#Mutation function definition
def mutate(chromosome, Pm):
    """
    chromosome - a single chromosome string
    Pm - probability of mutation
    """
    rnd = random.uniform(0,1)
    if rnd < Pm:
        ind = random.randint(0,3)
        good_candidates = get_good_candidates(chromosome)
        new_gene = random.sample(good_candidates,1)
        chromosome[ind] = new_gene[0]
    return sorted(chromosome)


#######################################################################################
    #elitism    
def WeakParent(current_pop, parents, mutants):
    '''
    current_pop - (list) - list containing current population of fixed size
    parents - (list) - consists of two parents selected for mating
    mutants - (list) - consists of offspring which may or maynot have been mutated
    '''
    fitness = []
    tour = parents + mutants
    print (tour)
    for chrom in tour:
        fitness.append(evaluate([chrom]))
        print (fitness)
    ind1 = fitness.index(max(fitness))
    max1 = tour.pop(ind1)
    ind2 = fitness.index(max(fitness))
    max2 = tour.pop(ind2)
    for ohoh in tour:
        current_pop.remove(ohoh)
    current_pop.append(max1)
    current_pop.append(max2)
        
    return current_pop   

def Random(current_pop, mutant):
    '''
    current_pop - (list) - list containing current population of fixed size
    mutant - (list) - consists of offspring which may or maynot have been mutated
    '''
    removee = random.sample(current_pop,1)
    #print (removee,current_pop)
    current_pop.remove(removee[0])
    current_pop.append(mutant)
    return current_pop
    

# Helper function
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
    
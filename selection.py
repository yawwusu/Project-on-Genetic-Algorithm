from evaluate import *
import random
def inside(range_dict,val):
    '''
    This is a helper function for selection function
    dic - range dictionary
    val - (float)
    '''
    for item in range_dict.keys():
        if val >= item[0] and val < item[1]:
            return range_dict[item]

def Roulette_wheel(chromosome,fitness,n):
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
    #for fit_1 in fitness:
    while so_far < sum_fitness:
        x,y = so_far,so_far+fitness[count]
        range_dict[x,y] = chromosome[count]
        so_far += fitness[count]
        count += 1
        
    for i in range(n):
        rnd = random.uniform(0,sum_fitness)  #or randrange (i dont know the difference)
        print rnd
        temp = inside(range_dict,rnd)
        mating_pool.append(temp)
    return range_dict, mating_pool
        
##################################################################################
    
def Tournament(Pop, Tour_Size , rounds = 2):
    ini_sample = random.sample(Pop , Tour_Size)
    #fitness  = []
    pool = []
    max_fit = 0
    max_chrom = 0
    for num in range(rounds):
        for chrom in ini_sample:
            fit = evaluate(chrom)
            #fitness.append(fit)    #There's really no use for it
            if fit > max_fit:
                max_fit = fit
                max_chrom = chrom
        pool.append(max_chrom)
    return pool
        
################################################################################3        
        
#def Rank(Ini_Pop , fitness , n = 2):
#    '''
#    Ini_Pop - list containing chromosomes
#    fitness - list containing fitness values of chromosomes in corresponding index
#    n - int : number of elements desired in mating pool
#    '''
#    sum_fitness = sum(fitness)
#    range_dict = {}
#    mating_pool = []
#    so_far = 0
#    count = 0
#
#    while count < len(fitness):
#        x,y = so_far,so_far+fitness[count]
#        range_dict[x,y] = chromosome[count]
#        so_far += fitness[count]
#        count += 1
#
#    for i in range(n):
#        rnd = random.uniform(0,sum_fitness) 
#        temp = inside(range_dict,rnd)
#        mating_pool.append(temp)
#    return mating_pool    

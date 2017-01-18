import random
import math
from numpy import *

def initialize(pop,size):
    initial_pop = []
    for i in range(size):
        rnd = random.randint(0,len(pop))
        initial_pop.append(pop[rnd])
        
    return initial_pop
    
                
def evaluate(initial_pop, dist_mat, serv_mat,potential):
    '''
    initial_pop - list containing all chromosomes
    c - csv file containing distance matrix
    x - csv file containing service matrix 
    '''
    c = loadtxt(dist_mat, delimiter = ',')
    x = loadtxt(serv_mat, delimiter = ',')
    d = loadtxt(potential, delimiter = ',')
    no_chromosomes = len(initial_pop)
    count = 0
    fitness = []
    while count < no_chromosomes:
        total = 0
        for i in initial_pop[count]:
            for j in initial_pop[count]:
                total += math.exp(-1*c[i-1][j-1])*x[i-1][j-1]*d[i-1]   #differences in indexing(change)
        fitness.append(total)
        count += 1
    return fitness
    
def inside(range_dict, val):
    '''
    This is a helper function for selection function
    dic - range dictionary
    val - (float)
    '''
    for item in range_dict.keys():
        if val >= item[0] and val < item[1]:
            return range_dict[item]

#Selection Function definition
def selection(chromosome,fitness,n):
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
    print range_dict
        
    for i in range(n):
        rnd = random.uniform(0,sum_fitness)  #or randrange (i dont know the difference)
        print rnd
        temp = inside(range_dict,rnd)
        mating_pool.append(temp)
    return mating_pool
                  
                                              
                
                
                
                
    
pop = list()
for i in range(1,21):
    for j in range(i+1,21):
        for k in range(j+1,21):
            for l in range(k+1,21):
                pop.append([i,j,k,l])     
                
#Initialization
#initial_pop = initialize(pop,500)

#Evaluation
eval_list = evaluate(pop, 'c.csv', 'x3.csv','d.csv')

##Selection
#mate_pool = selection(initial_pop, eval_list, 2)  # 2 offspring in the pool

##Crossover
#(off_1,off_2) = crossover(mate_pool, 0.8)   #Pc = 0.8
#
##Mutate
#mut_off_1 = mutate(off_1,0.2)    #Pm = 0.2
#mut_off_2 = mutate(off_2,0.2)
#
##Elitism
#initial_pop.append(mut_off_1)     #Basic form of elitism ##change
#initial_pop.append(mut_off_2)
index = eval_list.index(max(eval_list))
print pop[index]
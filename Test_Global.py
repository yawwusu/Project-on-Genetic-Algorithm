from numpy import *
import random
import math
   
                
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

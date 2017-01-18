from numpy import *
import random
import math
   
                
def evaluate(initial_pop, dist_mat='c.csv', serv_mat='x3.csv',potential='d.csv'):
    '''
    dist_mat - csv file containing distance matrix
    serv_mat - csv file containing service matrix
    potential - csv file containing service matrix 
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

#Evaluation
eval_list = evaluate(pop, 'c.csv', 'x3.csv','d.csv')

index = eval_list.index(max(eval_list))
print(pop[index])   #to make it compatible with python 3 onwards

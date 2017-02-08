from numpy import *
import math
def evaluate(initial_pop, dist_mat= 'Data/c.csv', serv_mat = 'Data/x_m.csv', potential = 'Data/d.csv'):
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
    J = (loadtxt('J.csv', delimiter = ','))
    no_chromosomes = len(initial_pop)
    count = 0
    fitness = []
    while count < no_chromosomes:
        total = 0
        for i in initial_pop[count]:
            for j in range(1,21):
                total += math.exp(-1*c[i-1][j-1])*x[i-1][j-1]*d[i-1]*J[i-1][j-1]  
        fitness.append(total)
        count += 1
    return fitness
    
from itertools import combinations
initial_pop = list(combinations([1,8,9,11,13,16,19],4))  

fitness = evaluate(initial_pop , 'c.csv' , 'x_m.csv' , 'd.csv')
print fitness     
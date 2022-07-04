import math
from numpy import *
import random

class Population:
    def __init__(self,pop):
        """
        pop - (list) - a list containing lists of encoded chromosomes
        """
        self.pop = pop
        
    def Getpop(self):
        """
        returns the population object (self.pop)
        """
        return self.pop
        
    def Setpop(self,pop):
        """
        pop - (list) - a list containing encoded chromosomes
        sets self.pop to pop
        """
        self.pop = pop
        
    def AddTopop(self,new_elem):
        """
        new_elem - (list) list containing new chromosomes to be added
        """
        self.pop.append(new_elem)
        
    def RemoveFrompop(self, old_elem):
        """
        old_elem - (list) list representing a chromosome in self.pop
        """
        self.pop.remove(old_elem)
        
    def __str__(self):
        """
        returns self.pop with nice formatting
        """
        string = "There are " + len(self.Getpop()) + "elements in the population. They are: "
        return string, self.Getpop()
        
        
##############################################################################################3        
     
class Genetic(Population):
    def __init__(self,pop):
        """
        pop - A population object
        """
        Population.__init__(self,pop)
        self.initital_pop = []
        self.fitness = []
        self.mating_pool = []
        
        
    def Initialize(self,size):
        """
        size - (int) - indicates the size of the initial population
        """
        ini_pop = random.sample(self.pop.Getpop(),size) 
        self.initial_pop = Population(ini_pop)
        
    def Evaluate(self, dist_mat= 'c.csv', serv_mat = 'x.csv', potential = 'd.csv'):
        '''
        dist_mat - csv file containing distance matrix
        serv_mat - csv file containing service matrix 
        potential - csv file containing potentials for the nodes
        '''
        #Reading in csv files
        c = loadtxt(dist_mat, delimiter = ',')
        x = loadtxt(serv_mat, delimiter = ',')
        d = loadtxt(potential,delimiter = ',')
        
        Ini_Pop = self.initial_pop.Getpop()
        for count in range(len(Ini_Pop)):
            total = 0
            for i in Ini_Pop[count]:
                for j in Ini_Pop[count]:
                    total += math.exp(-1*c[i-1][j-1])*x[i-1][j-1]*d[i-1]  
            self.fitness.append(total)
        #return self.fitness
        
    def Selection(self, Pool_Size = 2):
        '''
        Pool_Size - (int) : number of elements desired in mating pool
        '''
        range_dict = {}
        ini_pop = self.initial_pop.Getpop()
        print (len(ini_pop))
        print (len(self.fitness))
        so_far = 0
        count = 0
        while count < len(self.fitness):
            (x,y) = (so_far , so_far + self.fitness[count])
            range_dict[(x,y)] = ini_pop[count]
            so_far += self.fitness[count]
            count += 1
    
        for i in range(Pool_Size):
            rnum = random.uniform(0 , sum(self.fitness)) 
            temp = inside(range_dict,rnum)
            self.mating_pool.append(temp)
        #return self.mating_pool
        
    def Crossover(self , Pc):
        '''
        Pc - (float) - Probability of crossover, 0 < Pc < 1
        '''
        [parent1,parent2] = random.sample(self.mating_pool , 2)
    
        offspring1 = parent1
        offspring2 = parent2
        
        mask = [random.randint(0,1) for i in range(4)]
    
        for j in range(4):
            if mask[j] == 1 and random.uniform(0,1) < Pc:
                offspring1[j] = parent2[j]
                offspring2[j] = parent1[j]
            
        return (offspring1,offspring2)
            
            
    #Mutation function definition
    def Mutate(self,chromosome, Pm):
        """
        chromosome - a single chromosome string
        Pm - probability of mutation
        """
        for i in range(4):
            rnd = random.uniform(0,1)
            if rnd < Pm:
                chromosome[i] = random.randint(1,20)
                
        return chromosome
        
        
    
    
    
#####################################################################
#The following are helper functions used in the Genetic object
def inside(range_dict, val):
    '''
    This is a helper function for the selection function
    range_dict - (dict) range dictionary with mapping of fitness values and corresponding chromosome
    val - (float) a value which will 
    '''
    for item in range_dict.keys():
        if val >= item[0] and val < item[1]:
            return range_dict[item]
            
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
#########################################################################
    

import random
from Genetic_oops import *
def genetic_oop(dist_mat = 'c.csv', serv_mat = 'x3.csv', potential = 'd.csv', max_iter = 100):
    #Encoding
    pop = list()
    for i in range(1,21):
        for j in range(i+1,21):
            for k in range(j+1,21):
                for l in range(k+1,21):
                    pop.append([i,j,k,l])
                    
    Pop = Population(pop)
    Test1 = Genetic(Pop)
    #Initialization
    random.seed(1)
    Test1.Initialize(50)
    
    
    index = 0
    while index < 5:       #stopping criteria 100 for now
        #Evaluation
        Test1.Evaluate(dist_mat , serv_mat , potential)
        #Selection
        Test1.Selection(5)  # 5 offspring in the pool
        #Crossover
        (off_1,off_2) = Test1.Crossover(0.8)   #Pc = 0.8
        #Mutate
        #problem here,  ##genes can repeat
        mut_off_1 = Test1.Mutate(off_1 , 0.2)    #Pm = 0.2
        mut_off_2 = Test1.Mutate(off_2 , 0.2)
        #Elitism
        Test1.initial_pop.AddTopop(mut_off_1)
        Test1.initial_pop.AddTopop(mut_off_2)     
        # form of elitism ##change
        index += 1
    
    print len(Test1.initial_pop.Getpop())
    return max_occurs(Test1.initial_pop.Getpop())
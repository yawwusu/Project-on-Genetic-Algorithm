from All_Necessary_Funcs import *
def genetic(dist_mat = 'c.csv', serv_mat = 'x3.csv', potential = 'd.csv', max_iter = 100, Pc = 0.8, Pm = 0.2, Pop_Size = 50):
    #Encoding
    pop = list()
    for i in range(1,21):
        for j in range(i+1,21):
            for k in range(j+1,21):
                for l in range(k+1,21):
                    pop.append([i,j,k,l])
                    
    #Initialization
    random.seed(1)
    initial_pop = initialize(pop,Pop_Size)
    
    
    index = 0
    while index < max_iter:       #stopping criteria 100 for now
        
        #Evaluation
        eval_list = evaluate(initial_pop, 'c.csv', 'x3.csv','d.csv')
        
        #Selection
        mate_pool = selection(initial_pop, eval_list, 5)  # 2 offspring in the pool
        
        #Crossover
        (off_1,off_2) = crossover(mate_pool, Pc)   #
        print index
        #Mutate
        #problem here,  ##genes can repeat
        mut_off_1 = mutate(off_1,Pm)    #
        mut_off_2 = mutate(off_2,Pm)
        
        #Elitism
        initial_pop.append(mut_off_1)
        initial_pop.append(mut_off_2)     
        # form of elitism ##change
        index += 1
    
    print 'There are ', len(initial_pop), 'chromosomes in the final generation. The best is:'
    return max_occurs(initial_pop)
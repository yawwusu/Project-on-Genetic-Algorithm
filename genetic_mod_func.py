from All_Necessary_Funcs import *
def genetic(Pop_Size = 50 , Pc = 0.8, Pm = 0.2, max_iter = 100, selection = Roulette, crossover = NewCrossover,elitism = Random):
    #Encoding
    Population = encode([1,8,9,11,13,16,19],4)
                    
    #Initialization
    random.seed(1)
    initial_pop = initialize(Population,Pop_Size)
    
    
    index = 0
    while index < max_iter:       #stopping criteria 100 for now
        
        #Evaluation
        eval_list = evaluate(initial_pop)
        
        #Selection
        mate_pool = selection(initial_pop, eval_list, 5)  # 2 offspring in the pool
        
        #Crossover
        parents,offspring = crossover(mate_pool, Pc)   #
        
        #Mutate
        #problem here,  ##genes can repeat
        mutant = mutate(offspring,Pm)    #
        
        #Elitism
        initial_pop = elitism(initial_pop,mutant)   
        # form of elitism ##change
        
        index += 1
    
    print ('There are ', len(initial_pop), 'chromosomes in the final generation. The best is:')
    return max_occurs(initial_pop)
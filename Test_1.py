from All_Necessary_Funcs import *
import random
#Encoding
pop = list()
for i in range(1,21):
    for j in range(i+1,21):
        for k in range(j+1,21):
            for l in range(k+1,21):
                pop.append([i,j,k,l])
                
#Initialization
random.seed(1)
initial_pop = initialize(pop,50)


index = 0
while index < 100:       #stopping criteria 100 for now
    
    #Evaluation
    eval_list = evaluate(initial_pop, 'c.csv', 'x3.csv','d.csv')
    
    #Selection
    mate_pool = selection(initial_pop, eval_list, 5)  # 2 offspring in the pool
    #Crossover
    parents,offspring = Uniform_crossover(mate_pool, 0.8)   #Pc = 0.8
    #Mutate
    #problem here,  ##genes can repeat
    mutant = mutate(winning_offspring,0.2)    #Pm = 0.2
    
    #Elitism
    initial_pop = WeakParent_elitism(initial_pop,parents,mutant)
    
    index += 1

print index,len(initial_pop)
print max_occurs(initial_pop)
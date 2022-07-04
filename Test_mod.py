from All_Necessary_Funcs import *
import random
#Encoding
Population = encode([1,8,9,11,13,16,19],4)

random.seed(1)  #Check to ensure reproducibility. ##Comment out afterwards
              
#Initialization
initial_pop = initialize(Population,10)

index = 0
while index < 100:       #stopping criteria 100 for now
    
    #Evaluation
    eval_list = evaluate(initial_pop)
    
    #Selection
    mate_pool = Roulette(initial_pop, eval_list, 2)  # 2 offspring in the pool

    #Crossover      #problem here. genes can repeat
    parents,offspring = NewCrossover(mate_pool, 0.8)   #Pc = 0.8

    #Mutate
    mutant = mutate(offspring,0.2)    #Pm = 0.2
    
    #Elitism        #problem here. change in corresponding with crossover and make same input as Random
    initial_pop = Random(initial_pop,mutant)
    
    index += 1

print (index,len(initial_pop))
print (max_occurs(initial_pop))
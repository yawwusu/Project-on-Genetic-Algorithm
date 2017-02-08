import random
def mutate(chromosome, Pm):
    """
    chromosome - a single chromosome string
    Pm - probability of mutation
    """
    for i in range(4):
        rnd = random.uniform(0,1)
        if rnd < Pm:
            indicator = True
            while indicator:
                chromosome[i] = random.randint(1,20)
                counter = chromosome.count(chromosome[i]) 
                if counter == 1:
                    indicator = False
    return sorted(chromosome)
from genetic import *
def RunSim(numTrials, Ini_Pop_Size,max_iterations):
    for trial in range(numTrials):
        genetic(max_iter = max_iterations)
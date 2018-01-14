# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 12:07:33 2018

@author: SUBHANNITA
"""
import random
import numpy

def representation():
    """
    generate population of size pop_size, each having n items (either 0 or 1) with 
    associated cost c[i] (i=0 to n-1)
    """
    population=[]
    for i in range(popSize):
        
        
        while True:
            c=0
            candidate=[]
            for j in range(numberOfItems):
                while True:
                    r=random.uniform(0.0,1.0)
                    if r != 0.5: break
                if r<0.5:
                    candidate.append(0)
                else:
                    candidate.append(1)
                    c += cost[j]
                    if c > maxCost: break #if cost is already more than capacity, no use finding rest of chromosomes
            if c <= maxCost: break #break if this candidate satisfies cost limitation
        population.append(candidate)

    
    return population



def fitness_evaluation(candidate):
    #returns the value of a candidate
    
    fitness=sum(candidate[i]*value[i] for i in range(numberOfItems))
    
    return fitness


def parent_selection(population):
    #tournament slection
    
    while True:
        #pick two distinct random candidates
        r1=random.randint(0,popSize-1)
        r2=random.randint(0,popSize-1)
        if r1!=r2: break
    #return the parent with highest value
    parent = [e for _, e in sorted(zip([fitness_evaluation(population[r1]),fitness_evaluation(population[r2])] , [population[r1],population[r2]]), reverse=True)]
    return(parent[0])



def cost_evaluation(child):
    #returns the cost of a candidate (used in survivor selection)
    c = sum(child[i]*cost[i] for i in range(numberOfItems))
    return c
    
    

def crossover(parent1,parent2):
    #either crossover 2 parents or pass through
    children=[]
    crossoverProbability = float(7/10)
    r = random.uniform(0.0,1.0)
    if r < crossoverProbability:
        crossoverPoint=random.randint(0,numberOfItems-1)
        children.append(parent1[:crossoverPoint] + parent2[crossoverPoint:])
        children.append(parent2[:crossoverPoint] + parent1[crossoverPoint:])
            
    else:
        children.append(parent1)
        children.append(parent2)
    return children


def mutation(child):
    #mutation where probability of each chromosome flipping is Pm    
    mutationProbability = float(1/numberOfItems)
    for i in range(numberOfItems):
        r=random.uniform(0.0,1.0)
        if r<mutationProbability:
            child[i] = int(not child[i])
    return child


#GA parameters
popSize = 500
numberOfItems = 20
cost = [29,65,71,60,45,70,22,97,6,91,57,60,49,89,2,30,90,25,82,19]
maxCost = 524
value = [91,60,61,9,79,46,19,57,8,84,20,72,32,31,28,81,55,43,100,27]
#generate initial population
population = representation()
bestFitness=[] #highest fitness (value) of 25 successive generations of best solutions 
bestFitness.append(max(fitness_evaluation(x) for x in population)) 
iteration=1 #generation counter

while True:
    bestChildren=[] #best set of solutions
    print("Generation: ",iteration)
    #continue to produce and select children untill popSize best solutions
    while len(bestChildren) < popSize:
        children=[]
        #parent selection
        parent1 = parent_selection(population)
        parent2 = parent_selection(population)
        #crossover
        children += crossover(parent1,parent2)
        #mutation
        children[0] = mutation(children[0])
        children[1] = mutation(children[1])
        #check for cost constraints 
        """
        these may not be the best solutions for this generation as there may be other children who not only
        meet cost constraints but also have higher value
        But these children happen to come first
        """
        if cost_evaluation(children[0]) <= maxCost:
            bestChildren.append(children[0])
        if cost_evaluation(children[1]) <= maxCost:
            bestChildren.append(children[1])
            
    #update population; survivor selection is generational
    population = bestChildren
    #only interested in last 25 generations
    if len(bestFitness) == 25:
        bestFitness.pop(0)
    bestFitness.append(max(fitness_evaluation(x) for x in population))
    print("Highest Value: ",bestFitness[len(bestFitness)-1])
    g=numpy.gradient(bestFitness)
    g = abs(float(sum(g)/len(g)))
    #terminal condition
    if g == 0.0 or iteration==2000: break
    iteration += 1
    
    
    
            


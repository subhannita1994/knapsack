# knapsack

 Python implementation of Genetic algorithm for knapsack problem

 Reresentation: each candidate solution is n-bit long string where n is the number of items. 
               n<sub>i</sub> = 0 if item<sub>i</sub> is included
                             = 1 if not included
               Value of each candidate = sum(n<sub>i</sub> * v<sub>i</sub>) where v is set of values of all items
               Condition - sum(n<sub>i</sub> * v<sub>i</sub>) <= maximum capacity where c is set of costs of all items
               
 Parent selection operator: tournament
 Variation operators: single point crossover and flip mutation
 Survivor selection: generational

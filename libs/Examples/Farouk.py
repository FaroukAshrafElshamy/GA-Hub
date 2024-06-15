# _____Copyright © 2024 FaroukAshraf_____

# _________Libraries__________
from random import *
import time
from .Fqueen import Queen


def Farouk():
    # ___Libraries___
    import random

    # ___Parameters___
    QUEEN_NUM = 8
    MUTATION_RATE = 0.2
    POPULATION_SIZE = 10
    NUM_OF_GENERATIONS = 500
    MAX_FIT = (QUEEN_NUM*(QUEEN_NUM-1))//2


    # ___Alogrithm___

    def Population(QUEEN_NUM):
        population = []
        for _ in range(POPULATION_SIZE):
            x = list(range(1,QUEEN_NUM+1))
            random.shuffle(x)
            population.append(x)
        return population


    def Fitness(Chrom):
        Conf = 0
        for i in range(QUEEN_NUM):
            for j in range(i+1, QUEEN_NUM):
                if Chrom[i] == Chrom[j] or abs(Chrom[i] - Chrom[j]) == j - i:
                    Conf += 1
        return MAX_FIT - Conf


    # ___Breeding___
    def Selection(population):
        parents = []
        fit = [Fitness(x) for x in population]
        Idx = fit.index(max(fit))
        for _ in range(2):
            parents.append(population[Idx])
            fit[Idx] = -9999999
        return parents

    # Orderd crossover
    def Crossover(parent1, parent2):
        Child = [-1] * QUEEN_NUM
        Start, End = sorted(random.sample(range(QUEEN_NUM),2))
        Child[Start:End] = parent1[Start:End]
        i = End
        for item in parent2:
            if item not in Child:
                if i >= QUEEN_NUM:
                    i = 0
                Child[i] = item
                i += 1
        return Child


    def SinglePointCrossover(parent1, parent2):
        a = random.randint(0,QUEEN_NUM)
        parent1[:a] = parent2[:a]
        return parent1


    def Mutation(Child):
        Ind1, Ind2  = random.sample(range(QUEEN_NUM),2)
        Child[Ind1], Child[Ind2] = Child[Ind2], Child[Ind1]
        return Child


    def Replacement():
        population = Population(QUEEN_NUM)
        global gen 
        gen = 0
        for _ in range(NUM_OF_GENERATIONS):
            NewPopulation = []
            parents = Selection(population)
            gen+=1
            for _ in range(POPULATION_SIZE - 2):
                parent1, parent2 = random.sample(parents,2)
                Child = Crossover(parent1, parent2)
                if random.random() < MUTATION_RATE:
                    Child = Mutation(Child)
                NewPopulation.append(Child)
                if Fitness(Child) == MAX_FIT:
                    Queen(Child, QUEEN_NUM)
                    return Child
            population = NewPopulation + parents
        if True:
            print("Run Again Please")
    
    Replacement()
        

    # # ____ parameters _____

    # POPULATION_SIZE = 50
    # QUEEN_NUM = 6
    # MUTAION_RATE = 0.1


    # #____ Functions ____

    # # Create a Cromosome
    # def Cromosome(size):
    #     return [randint(1,size) for _ in range(size)] # Encoding is a way to represent genes randint(1,size)


    # # Fitness function
    # def FitnessFunc(Chrom):
    #     H_conf,D_conf = sum([Chrom.count(Q)-1 for Q in Chrom])/2,0
    #     L_diag,R_diag = [0]*2*QUEEN_NUM,[0]*2*QUEEN_NUM
    #     for i in range(QUEEN_NUM):
    #         L_diag[i+Chrom[i] -1] += 1
    #         R_diag[QUEEN_NUM-i+Chrom[i]-2] += 1
    #     for i in range(2*QUEEN_NUM-1):
    #         c=0
    #         if L_diag[i] > 1: c+=L_diag[i]-1
    #         elif R_diag[i] > 1: c+=R_diag[i]-1
    #         D_conf += c/(QUEEN_NUM - abs(i-QUEEN_NUM+1))
    #     return int(maxFitness - (H_conf + D_conf))

    # # ___________ Types of CrossOver _____________

    # # 1) Crossover (single point crossover)
    # # def CrossOver(parent1, parent2):
    # #     R = randint(0, QUEEN_NUM -1)
    # #     return parent1[:R] + parent2[R:]

    # # 2) Crossover (Two point crossover)
    # def CrossOver(parent1, parent2):
    #     R1,R2 = randint(0, QUEEN_NUM//2),randint(QUEEN_NUM//2, QUEEN_NUM-1)
    #     return parent1[:R1] + parent2[R1:R2] + parent2[R2:]

    # # 3) Crossover (Uniform crossover)
    # # def CrossOver(Parent1, Parent2):
    # #     mask = [randint(0,1) for _ in range(QUEEN_NUM)]
    # #     for i in range(QUEEN_NUM):
    # #         if mask[i]:
    # #             Parent1[i],Parent2[i] = Parent2[i],Parent1[i]
    # #     return Parent1

    # # 4) Crossover (Shuffle crossover)
    # # def CrossOver(parent1, parent2):
    # #   ShufOrder = sample(range(QUEEN_NUM), QUEEN_NUM)
    # #   ShufP1 = [parent1[i] for i in ShufOrder]
    # #   ShufP2 = [parent2[i] for i in ShufOrder]
    # #   R = randint(1, QUEEN_NUM - 1)
    # #   child1 = ShufP1[:R] + ShufP2[R:]
    # #   return child1


    # # Mutation
    # def Mutate(Chrom):
    #     R = randint(0, QUEEN_NUM -1)
    #     num = randint(1, QUEEN_NUM)
    #     Chrom[R] = num
    #     return Chrom


    # # Get-select best parent Rolletwheel
    # def Get_Parent(population, fitness):
    #     T = sum(x for x in fitness)
    #     R, Up = uniform(0, T),0
    #     for a,b in zip(population, fitness):
    #         if Up + b >= R:
    #             return a
    #         Up += b


    # # New population by doing crossover and mutaion for chromosomes
    # def NewPopulation(pop):
    #     N_pop = []
    #     for _ in range(POPULATION_SIZE):
    #         X1,X2 = Get_Parent(pop, [FitnessFunc(n) for n in pop]),Get_Parent(pop, [FitnessFunc(n) for n in pop])
    #         child = CrossOver(X1, X2)
    #         if random() < MUTAION_RATE: child = Mutate(child)
    #         N_pop.append(child)
    #         if FitnessFunc(child) == maxFitness: break   
    #     return N_pop


    # # ____ main program ____
    # startTime  = time.time()
    # population = [Cromosome(QUEEN_NUM) for _ in range(POPULATION_SIZE)]
    # maxFitness = (QUEEN_NUM * (QUEEN_NUM - 1)) / 2
    # generation = 1
    # while not maxFitness in [FitnessFunc(Chrom) for Chrom in population]:
    #     population = NewPopulation(population)
    #     generation += 1

    # for Chrom in population:
    #     if FitnessFunc(Chrom) == maxFitness:
    #         endTime = time.time()
    #         print("==== Solved in Gen {} ====".format(generation))
    #         print("Best Solution is {}".format(Chrom))
    #         print("This Algorithm takes {:.2f}".format(endTime - startTime))                                                
    #         board = [["X"]*QUEEN_NUM for _ in range(QUEEN_NUM)]        
    #         Queen(Chrom,QUEEN_NUM)
    #         for i in range(QUEEN_NUM):
    #             board[QUEEN_NUM - Chrom[i]][i] = 'Q'
    #         for z in board:
    #             print(*z)
    #         break

if __name__ == "__main__":
    Farouk()
    # Ans = Replacement()
    # print(f"Solved in Generation => {gen} <=")
    # print(f"Best answer is: {Ans}\nIt's Fitness = {Fitness(Ans)}\n")
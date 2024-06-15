import random
import matplotlib.pyplot as plt

def Rahma():
    # Compile time: bind a variable to a particular data type at compile time.
    # Load time: bind a variable to a memory cell (ex. C static variables)
    # Runtime: bind a nonstatic local variable to a memory cell
    # impeartive programming
    # unlimited name_length,case_senstitive,allow special character and underscore at beginig
    # allow data type :string,int,float,complex,bool
    # dynamic binding at runtime ,type infernce,interpreter
    NUM_TASKS = 5
    # name  type:(type inferenece):int   #value
    MAX_DURATION = 10
    # The type of POPULATION_SIZE is bound at compile time
    # The set of possible values of POPULATION_SIZE is bound at compiler design time
    # The internal representation of the literal 10 is bound at compiler design time
    # The value of POPULATION_SIZE is bound at execution times with this statement
    POPULATION_SIZE = 10
    # implicit decleration(int) ,static binding,readability propblem ,#writiability advantage
    # scope:global (static scope)
    # lifetime:end of program
    # lexeme           token
    # NUM_GENERATIONS  identifier
    #  =              equal sign
    # 5             int literal
    NUM_GENERATIONS = 5
    MUTATION_RATE = 0.1

    # list bounding
    # lifetime until they are no longer referenced
    # orthogonality #cost and readability problem
    tasks = [
        ("Plc", 0, random.randint(1, MAX_DURATION)),
        ("Genetic", 1, random.randint(1, MAX_DURATION)),
        (".Net", 2, random.randint(1, MAX_DURATION)),
        ("Track", 3, random.randint(1, MAX_DURATION)),
        ("Adv SW", 4, random.randint(1, MAX_DURATION))
    ]
    print(tasks)


    # def:keyword
    # function binding    #parameter binding
    def fitness(schedule):
        completion_time = 0
        current_time = 0
        for task_index in schedule:
            task_duration = tasks[task_index][2]
            current_time = max(current_time, tasks[task_index][1])  # Start time
            # operator overloading (multipicity)
            current_time += task_duration  # Finish time
            completion_time = max(completion_time, current_time)
        return completion_time


    def generate_population(pop_size):
        population = []
        for _ in range(pop_size):
            schedule = random.sample(range(NUM_TASKS), NUM_TASKS)
            population.append(schedule)
        return population


    # Tournament selection
    def selection(population, fitness_scores, tournament_size=3):
        selected = []
        for _ in range(len(population)):
            # special word:reserved word(random,choices)
            #  lifetime within the scope of their respective functions
            contestants = random.choices(population, k=tournament_size)
            # min:reserved word,Writability advantages come from the concise use of list comprehensions
            winner_index = contestants.index(min(contestants, key=lambda x: fitness_scores[population.index(x)]))
            selected.append(contestants[winner_index])
        # keyword:return
        return selected


    def crossover(parent1, parent2):
        crossover_point = random.randint(0, len(parent1) - 1)
        child = parent1[:crossover_point] + [gene for gene in parent2 if gene not in parent1[:crossover_point]]
        return child


    def mutation(schedule):
        # if:keyword
        if random.random() < MUTATION_RATE:
            idx1, idx2 = random.sample(range(NUM_TASKS), 2)
            schedule[idx1], schedule[idx2] = schedule[idx2], schedule[idx1]
        return schedule


    def evolve(population):
        for _ in range(NUM_GENERATIONS):
            fitness_scores = [fitness(schedule) for schedule in population]
            selected = selection(population, fitness_scores)
            offspring = []
            for i in range(0, len(selected), 2):
                offspring.extend([selected[i], selected[i + 1]])
            mutated_offspring = [mutation(schedule) for schedule in offspring]
            population = mutated_offspring

        return population


    def visualize_best_schedule(population):
        best_schedule = min(population, key=fitness)
        print("Best Schedule:", best_schedule)
        print("Total Completion Time:", fitness(best_schedule))
        plt.figure(figsize=(8, 6))
        start_times = [0] * len(best_schedule)
        current_time = 0
        for i, task_index in enumerate(best_schedule):
            start_times[i] = current_time
            current_time += tasks[task_index][2]

        plt.bar(range(len(best_schedule)), [tasks[i][2] for i in best_schedule],
                bottom=start_times, color='skyblue')
        plt.xticks(range(len(best_schedule)), [tasks[i][0] for i in best_schedule])

        # plt.xlabel('Task')
        plt.ylabel('Time')
        plt.title('Best Schedule')
        plt.text(7/ 2, -3.2, "By: Nourseen Mohsen and ", ha='center', fontsize=10)
        plt.text(9.5 / 2, -3.2, "Rahma Akmal", ha='center', fontsize=10)
        plt.show()

    population = generate_population(POPULATION_SIZE)
    evolved_population = evolve(population)
    visualize_best_schedule(evolved_population)

if __name__ == "__main__":
    Rahma()
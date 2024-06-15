#BY Nada Gamal SharafEldin
import turtle
import random

def Nada():
    # Magic square size
    N = 3
    POPULATION_SIZE = 100
    MAX_GENERATIONS = 1000
    # Magic sum
    MAGIC_SUM = int(N * (N ** 2 + 1) / 2)

    def create_individual():
        # Create a random permutation of numbers from 1 to N^2 without repetitions.
        numbers = list(range(1, N ** 2 + 1))
        random.shuffle(numbers)
        return numbers

    def create_population():
        # Create a population of individuals.
        return [create_individual() for _ in range(POPULATION_SIZE)]

    def calculate_fitness(individual):
        # Calculate fitness as the difference between the sum of each row, column, and diagonal and the magic sum. Penalize solutions with repeated numbers.
        diff = sum(abs(sum(individual[i * N : (i + 1) * N]) - MAGIC_SUM) for i in range(N)) \
            + sum(abs(sum(individual[i : N * (N - 1) + i + 1 : N]) - MAGIC_SUM) for i in range(N)) \
            + abs(sum(individual[i * (N + 1)] for i in range(N)) - MAGIC_SUM) \
            + abs(sum(individual[(i + 1) * (N - 1)] for i in range(N - 1)) + individual[N * (N - 1)] - MAGIC_SUM)

        # Penalize solutions with repeated numbers
        penalty = len(set(individual)) - N ** 2
        diff += penalty * 100  # Adjust penalty weight as needed
        return diff

    def selection(population, fitness_values):
        # Perform roulette wheel selection.
        total_fitness = sum(fitness_values)
        probabilities = [fitness / total_fitness for fitness in fitness_values]
        return random.choices(population, probabilities)[0]

    def crossover(parent1, parent2):
        # Perform single-point crossover.
        crossover_point = random.randint(1, N - 1)
        child = parent1[:crossover_point] + [gene for gene in parent2 if gene not in parent1[:crossover_point]]
        return child

    def mutation(individual):
        # Perform swap mutation.
        index1, index2 = random.sample(range(N ** 2), 2)
        individual[index1], individual[index2] = individual[index2], individual[index1]
        return individual

    def draw_square(size, x, y, number):
        # Draw a square with the given size, position, and number.
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color("black")
        turtle.pensize(5)
        turtle.fillcolor("white")
        turtle.begin_fill()

        for _ in range(4):
            turtle.forward(size)
            turtle.right(90)

        turtle.end_fill()
        turtle.color("purple")
        turtle.penup()
        turtle.goto(x + size / 2, y + size / 2 - 120)
        turtle.write(number, align="center", font=("Arial", 25, "bold"))

    def draw_magic_square(solution):
        # Clear the screen and set up the turtle.
        turtle.clearscreen()
        turtle.speed(0)
        turtle.hideturtle()
        # Set background color
        turtle.bgcolor("lightgray")
        
        square_size = 100
        start_x = -square_size * N / 2
        start_y = square_size * N / 2
        # Write "Magic Square" above the square
        turtle.penup()
        turtle.goto(0, start_y + 50)
        turtle.pendown()
        turtle.pencolor("black")
        turtle.write("Magic Square", align="center", font=("Georgia", 50, "bold"))
        # Draw the magic square.
        for i in range(N):
            for j in range(N):
                number = solution[i * N + j]
                draw_square(square_size, start_x + j * square_size, start_y - i * square_size, number)

    

    def genetic_algorithm():
        """Run the genetic algorithm."""
        # Initialize population
        population = create_population()

        for _ in range(MAX_GENERATIONS):
            # Evaluate population fitness
            fitness_values = [calculate_fitness(individual) for individual in population]

            # Check for termination condition
            if min(fitness_values) == 0:
                best_individual = population[fitness_values.index(0)]
                return best_individual, 0

            # Select parents
            parent1 = selection(population, fitness_values)
            parent2 = selection(population, fitness_values)

            # Perform crossover
            offspring = crossover(parent1, parent2)

            # Perform mutation
            offspring = mutation(offspring)

            # Replace worst individual with offspring
            idx_worst = fitness_values.index(max(fitness_values))
            population[idx_worst] = offspring

        # If termination condition is not met, return the best solution found
        best_individual = population[fitness_values.index(min(fitness_values))]
        return best_individual, calculate_fitness(best_individual)

    # Function to prompt the user to try again
    def try_again_prompt():
        return turtle.textinput("Try Again?", "Do you want to try again for a better solution? (yes/no)").lower().strip()

    # Main function
    def main():
        while True:
            # Run the genetic algorithm
            best_solution, fitness_value = genetic_algorithm()

            # Draw the magic square using turtle
            draw_magic_square(best_solution)

            # Write fitness value on the screen
            turtle.penup()
            turtle.goto(0, -280)
            turtle.pendown()
            turtle.write(f"Fitness Value: {fitness_value}", align="center", font=("Arial", 18, "bold"))

            # Write "Try again for a better solution" message
            turtle.penup()
            turtle.goto(0, -320)
            turtle.pendown()
            turtle.pencolor("indigo")
            turtle.write("Try again for a better solution", align="center", font=("Arial", 18, "italic"))
            turtle.penup()
            turtle.goto(-250, -350)
            turtle.pendown()
            turtle.pencolor("maroon")
            turtle.write("Note:lower fitness value gives better solution", align="center", font=("Arial", 10, "bold"))
            turtle.penup()
            turtle.goto(260, -380)
            turtle.pendown()
            turtle.pencolor("purple")
            turtle.write("By: Nada Gamal Sharaf El-din", align="center", font=("Georgia", 15, "bold"))

            # Ask the user to try again
            user_input = try_again_prompt()
            if user_input != 'yes':
                break

    main()
    turtle.done()
if __name__ == "__main__":
    Nada()
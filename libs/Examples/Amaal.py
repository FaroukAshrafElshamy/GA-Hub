import turtle
import random

def Amaal():
    maze = [
        [1, 1, 0, 0, 1, 1, 1, 0, 1],
        [1, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 2],
    ]

    Maze_size = len(maze)  # 10

    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.title("Maze")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.penup()
    t.goto(-100, 250)
    t.write("Amaal Selim", font=("Arial", 24, "normal"))
    t.speed(0)
    t.penup()
    t.goto(-250, 250)
    turtle.tracer(1, 0)
    t.pendown()


    # Draw the maze
    def draw_maze():
        cell_size = 500 / Maze_size
        for row in range(Maze_size):
            for col in range(Maze_size):
                if maze[row][col] == 0:  # wall
                    t.fillcolor("black")
                elif maze[row][col] == 2:  # Goal
                    t.fillcolor("red")
                else:
                    t.fillcolor("white")
                t.begin_fill()
                for _ in range(4):
                    t.forward(cell_size)
                    t.right(90)
                t.end_fill()
                t.forward(cell_size)
            t.backward(cell_size * Maze_size)
            t.right(90)
            t.forward(cell_size)
            t.left(90)


    # Draw the path for an individual
    def draw_path(path):
        t.penup()
        t.goto(-250 + 500 / Maze_size / 2, 250 - 500 / Maze_size / 2)
        t.pendown()
        t.width(3)
        t.color("green")
        x, y = 0, 0
        for direction in path:
            if direction == "U" and x > 0 and maze[x - 1][y] != 0:
                t.setheading(90)
                t.forward(500 / Maze_size)
                x -= 1
            elif direction == "D" and x < Maze_size - 1 and maze[x + 1][y] != 0:
                t.setheading(270)
                t.forward(500 / Maze_size)
                x += 1
            elif direction == "L" and y > 0 and maze[x][y - 1] != 0:
                t.setheading(180)
                t.forward(500 / Maze_size)
                y -= 1
            elif direction == "R" and y < Maze_size - 1 and maze[x][y + 1] != 0:
                t.setheading(0)
                t.forward(500 / Maze_size)
                y += 1

            # Stop if goal is reached
            if maze[x][y] == 2:
                break


    def fitness_function(path):
        x, y = 0, 0
        for direction in path:
            if direction == "U" and x > 0 and maze[x - 1][y] != 0:
                x -= 1
            elif direction == "D" and x < Maze_size - 1 and maze[x + 1][y] != 0:
                x += 1
            elif direction == "L" and y > 0 and maze[x][y - 1] != 0:
                y -= 1
            elif direction == "R" and y < Maze_size - 1 and maze[x][y + 1] != 0:
                y += 1
            if maze[x][y] == 2:
                return 1  # Destination reached

        # If the destination is not reached, return the reciprocal of the Manhattan distance
        return 1 / (abs(x - (Maze_size - 1)) + abs(y - (Maze_size - 1)) + 1)


    def generate_random_path():
        return "".join(random.choice(["U", "D", "L", "R"]) for _ in range(40))


    # Generate random paths for individuals
    def generate_population(population_size):
        return [generate_random_path() for _ in range(population_size)]


    # Draw the maze
    draw_maze()


    population_size = 20
    generations = 100

    population = generate_population(population_size)
    # print(population)

    for generation in range(generations):
        fitness_scores = []
        for individual in population:
            fitness_scores.append(fitness_function(individual))
        best_individual_index = fitness_scores.index(max(fitness_scores))
        best_individual = population[best_individual_index]
        print(f"Generation: {generation + 1}, Best Path:", best_individual)
        print("Fitness Score:", fitness_function(best_individual))

        # Draw paths for all individuals in this generation
        for individual in population:
            draw_path(individual)

        if fitness_function(best_individual) == 1:
            t.hideturtle()
            print("Goal reached in generation", generation + 1)
            print("Best Path:", best_individual)
            print("Fitness Score: 1")
            break

        new_generation = []
        # crossover
        for _ in range(population_size):
            parent1, parent2 = random.choices(population, weights=fitness_scores, k=2)
            crossover_point = random.randint(0, min(len(parent1), len(parent2)))
            child = parent1[:crossover_point] + parent2[crossover_point:]
            new_generation.append(child)
        # Mutation
        for i in range(population_size):
            if random.random() < 0.1:  # Mutation rate
                mutation_point = random.randint(0, len(new_generation[i]) - 1)
                new_generation[i] = (
                    new_generation[i][:mutation_point]
                    + random.choice(["U", "D", "L", "R"])
                    + new_generation[i][mutation_point + 1 :]
                )
        population = new_generation


    turtle.mainloop()
if __name__ == "__main__":
    Amaal()
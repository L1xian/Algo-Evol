import random

# Exemple de tâches avec leurs durées
tasks = {
    'Tâche 1': 3,
    'Tâche 2': 2,
    'Tâche 3': 1,
    'Tâche 4': 4
}

# Fonction de fitness
def fitness(individual):
    # Exemple simple : le temps total d'achèvement
    return sum([tasks[task] for task in individual])

# Sélection par roulette
def roulette_selection(population):
    total_fitness = sum(fitness(ind) for ind in population)
    selection_probs = [fitness(ind) / total_fitness for ind in population]
    return random.choices(population, weights=selection_probs, k=2)

# Croisement
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child = parent1[:point] + [task for task in parent2 if task not in parent1[:point]]
    return child

# Mutation
def mutate(individual, mutation_rate=0.1):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

# Boucle principale
population_size = 10
num_generations = 50
population = [random.sample(list(tasks.keys()), len(tasks)) for _ in range(population_size)]

for generation in range(num_generations):
    new_population = []
    while len(new_population) < population_size:
        parent1, parent2 = roulette_selection(population)
        child = crossover(parent1, parent2)
        mutate(child)
        new_population.append(child)
    population = new_population

# Meilleure solution
best_solution = min(population, key=fitness)
print("Meilleure solution :", best_solution)
print("Fitness de la meilleure solution :", fitness(best_solution))

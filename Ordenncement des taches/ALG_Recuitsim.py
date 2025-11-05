import random
import math

# Exemple de tâches avec leurs durées
tasks = {
    'Tâche 1': 3,
    'Tâche 2': 2,
    'Tâche 3': 1,
    'Tâche 4': 4
}

# Fonction de coût
def cost(solution):
    return sum([tasks[task] for task in solution])

# Générer une solution initiale aléatoire
def generate_initial_solution():
    solution = list(tasks.keys())
    random.shuffle(solution)
    return solution

# Perturbation de la solution
def perturb(solution):
    new_solution = solution[:]
    idx1, idx2 = random.sample(range(len(new_solution)), 2)
    new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return new_solution

# Algorithme de recuit simulé
def simulated_annealing():
    current_solution = generate_initial_solution()
    current_cost = cost(current_solution)
    temperature = 1000  # Température initiale
    cooling_rate = 0.95  # Taux de refroidissement

    while temperature > 1:
        new_solution = perturb(current_solution)
        new_cost = cost(new_solution)

        # Acceptation de la nouvelle solution
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
            current_solution = new_solution
            current_cost = new_cost

        # Refroidissement
        temperature *= cooling_rate

    return current_solution, current_cost

# Exécution de l'algorithme
best_solution, best_cost = simulated_annealing()
print("Meilleure solution :", best_solution)
print("Coût de la meilleure solution :", best_cost)

import random

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

# Générer des solutions voisines
def generate_neighbors(solution):
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]  # Échange de deux tâches
            neighbors.append(neighbor)
    return neighbors

# Algorithme de recherche tabou
def tabu_search(max_iterations, tabu_tenure):
    current_solution = generate_initial_solution()
    best_solution = current_solution
    best_cost = cost(best_solution)
    tabu_list = []

    for _ in range(max_iterations):
        neighbors = generate_neighbors(current_solution)
        best_neighbor = None
        best_neighbor_cost = float('inf')

        for neighbor in neighbors:
            if neighbor not in tabu_list:
                neighbor_cost = cost(neighbor)
                if neighbor_cost < best_neighbor_cost:
                    best_neighbor_cost = neighbor_cost
                    best_neighbor = neighbor

        if best_neighbor:
            current_solution = best_neighbor
            if best_neighbor_cost < best_cost:
                best_solution = best_neighbor
                best_cost = best_neighbor_cost

            # Mise à jour de la liste taboue
            tabu_list.append(current_solution)
            if len(tabu_list) > tabu_tenure:
                tabu_list.pop(0)  # Retirer la plus ancienne solution taboue

    return best_solution, best_cost

# Exécution de l'algorithme
best_solution, best_cost = tabu_search(max_iterations=100, tabu_tenure=5)
print("Meilleure solution :", best_solution)
print("Coût de la meilleure solution :", best_cost)

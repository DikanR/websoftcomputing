import numpy as np
# import pandas as pd
import random

# path = '3.b. TSP - AG.xlsx'
# df = pd.read_excel(path, index_col=0)
# cities = list(df.index)
# dist_matrix = df.values.astype(float)
# items = [cities, dist_matrix]

# print(cities)
# print(dist_matrix)

# POP_SIZE = 100
# GENERATIONS = 500
# TOURNAMENT_K = 5
# PC = 0.9
# PM = 0.2
# ELITE_SIZE = 1

def route_distance(route, dist_matrix):
    d = sum([dist_matrix[route[i], route[(i+1)%len(route)]] for i in range(len(route))])
    # d = sum(dist_matrix[route[i]][route[(i+1) % len(route)]] for i in range(len(route)))
    return d

def create_individual(n):
    ind = list(range(n))
    random.shuffle(ind)
    return ind

def initial_population(size, n):
    return [create_individual(n) for _ in range(size)]

def tournament_selection(pop, dist_matrix,tournament_k):
    k = random.sample(pop, tournament_k)
    return min(k, key=lambda ind: route_distance(ind, dist_matrix))

def ordered_crossover(p1, p2):
    a, b = sorted(random.sample(range(len(p1)), 2))
    child = [-1]*len(p1)
    child[a:b+1] = p1[a:b+1]
    p2_idx = 0
    for i in range(len(p1)):
        if child[i] == -1:
            while p2[p2_idx] in child:
                p2_idx += 1
            child[i] = p2[p2_idx]
    return child

def swap_mutation(ind):
    a, b = random.sample(range(len(ind)), 2)
    ind[a], ind[b] = ind[b], ind[a]

def genetic_algorithm(pop_size=0, generations=0, crossover_rate=0, mutation_rate=0, tournament_k=0, items=[], elite_size=1):
    # items = [['A', 'B', 'C', 'D', 'E'], [[1, 2, 9, 10, 7],
    #                                      [2, 1, 6, 4, 3],
    #                                      [9, 6, 1, 8, 5],
    #                                      [10, 4, 8, 1, 6],
    #                                      [7, 3, 5, 6, 1]]]
    
    cities, dist_matrix = items # makan RAM dikit tapi biar gak bingung daripada itemsp[0], items[1]. readibility over performance, python udh berat duluan aowkaokwaok
    dist_matrix = np.array(dist_matrix, dtype=float) # ini karena "list indices must be integers or slices, not tuple" exception di route_distance
    # print(mutation_rate)
    # print(crossover_rate)
    # print(pop_size)
    print(generations)
    # print(cities)
    # print(dist_matrix)
    pop = initial_population(pop_size, len(cities))
    best = min(pop, key=lambda ind: route_distance(ind, dist_matrix))
    best_dist = route_distance(best, dist_matrix)
    history = []

    for g in range(generations):
        # print(f"Generation {g+1}/{generations}")
        new_pop = []
        
        pop = sorted(pop, key=lambda ind: route_distance(ind, dist_matrix))
        
        if route_distance(pop[0], dist_matrix) < best_dist:
            best = pop[0]
            best_dist = route_distance(best, dist_matrix)
        
        new_pop.extend(pop[:elite_size])
        
        while len(new_pop) < pop_size:
            p1 = tournament_selection(pop, dist_matrix,tournament_k)
            p2 = tournament_selection(pop, dist_matrix,tournament_k)
            
            child = ordered_crossover(p1, p2) if random.random() < crossover_rate else p1[:]
            
            if random.random() < mutation_rate:
                swap_mutation(child)
            
            new_pop.append(child)
        
        pop = new_pop
        
        history.append(best_dist)
        
        # if g % 50 == 0:
        #     print(f"Gen {g}: Best Distance = {best_dist:.4f}")

    best_route = [cities[i] for i in best]

    return history, best_route, best_dist

    # print("\nRute terbaik:", " -> ".join(best_route + [best_route[0]]))
    # print("Jarak total:", best_dist)
    # pd.DataFrame({'city': best_route}).to_csv('hasil_TSP_GA.csv', index=False)
    # print("\nHasil tersimpan di: hasil_TSP_GA.csv")
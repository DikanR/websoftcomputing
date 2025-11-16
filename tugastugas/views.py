from django.http import HttpResponse
from django.shortcuts import render
from .algorithms import algoritma_genetika as ag
import random

# def index(request):
#     test = "ini adalah teks"
#     with open("tugastugas/html/tugas.html", "r") as file:
#         bruh = file.read()
#         bruh = bruh.format(test=test)
#         return HttpResponse(bruh)

def index(request):
    context = {
        'test': "ini adalah teks"
    }
    return render(request, 'tugas.html', context)

def tugas2(request):
    items = {
        'A': {'weight': 7, 'value': 5},
        'B': {'weight': 2, 'value': 4},
        'C': {'weight': 1, 'value': 7},
        'D': {'weight': 9, 'value': 2},
    }
    capacity = 15
    generations = 8

    random.seed(42)  # replikasi konsisten menggunakan seed ini global menyeluruh
    results, best_result = ag.genetic_algorithm(pop_size=8, generations=generations, crossover_rate=0.8, items=items, capacity=capacity, mutation_rate=0.1)

    # print(results)
    # print(best_result)

    context = {
        'generations': generations,
        'items': items,
        'capacity': capacity,
        'results': results,
        'best_result': best_result
    }
    return render(request, 'tugas2.html', context)
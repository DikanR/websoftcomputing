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

def tugas3(request):
    items_count = 0
    items = {}
    results = []
    best_result = {}
    capacity = 0
    generations = 0
    crossover_rate = 0.0
    mutation_rate = 0.0

    if request.method == "POST":
        if request.POST.get('items_count') is not None and request.POST.get('items_count') != '':
            items_count = int(request.POST.get('items_count'))
        # print(f"ini adlaah array: {request.POST.getlist('weight[]')[0]}")
        if request.POST.getlist('weight[]') is not None and request.POST.getlist('value[]') is not None:
            weight = request.POST.getlist('weight[]')
            value = request.POST.getlist('value[]')
        if request.POST.get('capacity') is not None and request.POST.get('capacity') != '': # ini buat ngecek klo misalnya bukan NoneType atau pun '' string kosong saat submit
            capacity = int(request.POST.get('capacity'))
        if request.POST.get('generations') is not None and request.POST.get('generations') != '':
            generations = int(request.POST.get('generations'))
        if request.POST.get('crossover_rate') is not None and request.POST.get('crossover_rate') != '':
            crossover_rate = float(request.POST.get('crossover_rate'))
        if request.POST.get('mutation_rate') is not None and request.POST.get('mutation_rate') != '':
            mutation_rate = float(request.POST.get('mutation_rate')) 
        
        if items_count > 0 and len(weight) == items_count and len(value) == items_count and weight[0] != '' and value[0] != '' and capacity > 0 and generations > 0:
            for i in range(int(items_count)):
                items[f'item {i+1}'] = {
                    # 'weight': int(weight[i]) if weight[i] != '' else 0,
                    'weight': int(weight[i]),
                    'value': int(value[i])
                }
            random.seed(42)  # replikasi konsisten menggunakan seed ini global menyeluruh
            results, best_result = ag.genetic_algorithm(pop_size=8, generations=generations, crossover_rate=(crossover_rate / 100), items=items, capacity=capacity, mutation_rate=(mutation_rate / 100))

    # items = {
    #     'A': {'weight': 7, 'value': 5},
    #     'B': {'weight': 2, 'value': 4},
    #     'C': {'weight': 1, 'value': 7},
    #     'D': {'weight': 9, 'value': 2},
    # }


    # print(results)
    # print(best_result)
    context = {
        'generations': generations,
        'items_count': items_count,
        'capacity': capacity,
        'generations': generations,
        'crossover_rate': crossover_rate,
        'mutation_rate': mutation_rate,
        'items_count_range': range(1, int(items_count)+1),
        'items': items,
        'capacity': capacity,
        'results': results,
        'best_result': best_result
    }
    return render(request, 'tugas3.html', context)
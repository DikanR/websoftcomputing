from django.http import HttpResponse
from django.shortcuts import render

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
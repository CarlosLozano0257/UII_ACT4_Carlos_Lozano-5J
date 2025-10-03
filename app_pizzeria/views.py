from django.shortcuts import render

def index(request):
    empleados = [
        {'nombre': 'Alice', 'edad': 30, 'puesto': 'Desarrollador Senior'},
        {'nombre': 'Bob', 'edad': 24, 'puesto': 'Diseñador UI/UX'},
        {'nombre': 'Charlie', 'edad': 35, 'puesto': 'Gerente de Proyecto'},
    ]
    context = {'empleados': empleados}
    return render(request, 'index.html', context)
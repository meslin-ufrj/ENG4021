from django.shortcuts import render
from CarsApp.models import MTCars

# Create your views here.

def searchf(request):
    if request.method == 'GET':
        return render(request, 'CarsApp/home.html')
    else:
        search_query = request.POST.get('search')
        # Aqui você pode adicionar a lógica para filtrar os carros com base na pesquisa
        carros = MTCars.objects.filter(name__icontains=search_query)
        # contexto é uma variável do tipo dicionário 
        # que armazena os dados a serem enviados para o template.
        # No template, você pode acessar esses dados usando as chaves do dicionário.
        contexto = {
            'search_query': search_query,   # o texto pesquisado
            'carros': carros                # os resultados da pesquisa
        }
        return render(request, 'CarsApp/home.html', contexto)

def detalhes(request, carro_id):
    # Ao criar uma entrada no dicionário contexto com o nome carro (string constante),
    # você vai criar uma variável carro no template associado pela função render.
    # Essa variável é um objeto carro, com todas as suas propriedades.
    carro = MTCars.objects.get(id=carro_id)
    contexto = {
        'carro': carro
    }
    return render(request, 'CarsApp/detalhes.html', contexto)

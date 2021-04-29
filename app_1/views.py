from django.shortcuts import render
from .models import Address

# Create your views here.
# def home(request):
#     query_city = request.GET.get('city')
#     data = Address.objects.raw('SELECT * FROM app_1_address where city={query_city}')
#     return render(request, 'index.html', {'data':data})

def home(request):
    return render(request, 'home.html')
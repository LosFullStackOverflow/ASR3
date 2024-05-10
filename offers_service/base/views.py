from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
from offers_service.offers_service.auth0backend import getRole

@login_required
def landing_page(request):
    role = getRole(request)
    context = {
        'username': request.user.username,
        'role': role,
        'is_asesor_bancario': role == "Asesor bancario",
        'is_cliente': role == "Cliente"
    }
    return render(request, 'clientes/landing_page.html', context) 

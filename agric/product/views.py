from django.db.models import fields
from django.shortcuts import render
from . models import farmer,farm
from django.views.generic import CreateView,TemplateView

# Create your views here.

def index(request):
    return render(request, 'index.html')

# def farmers(request):
#     return render(request, 'farmers.html')

class farmers(CreateView):
    model=farmer
    fields = ['name_of_organization','Full_address_location','crop','why_do_you_seeking_land','how_much_you_invest','passport','national_ID_card','farm_location']
    template_name = "farmers.html"
    success_url = "/"


def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def lands(request):
    return render(request, 'lands.html')

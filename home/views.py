import re
from turtle import ht
from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from home.models import Drug,Pubmed,Conditionstype,Brandtype

# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse('This is the homepage')


def signin(request):
    return render(request, "signin.html")


def explore(request):
    return render(request, "explore.html")


def drug(request):
    context = {}
    drug_name = request.GET.get('drug_name', '')
    if drug_name:
        drugs = Drug.objects.filter(drug_name__icontains=drug_name).select_related('brands_id')
        processed_drugs = [
            {
                'drug_id': drug.drug_id,
                'drug_name': drug.drug_name,
                'brands': ', '.join(filter(None, [drug.brands_id.brand_name1, drug.brands_id.brand_name2, drug.brands_id.brand_name3]))
            }
            for drug in drugs
        ]
        context['drugs'] = processed_drugs

    return render(request, "drug_list.html", context)


def pubmed(request):
    references = Pubmed.objects.all()
    return render(request, "reference.html", {"references": references})


def conditions(request):
    conditions = Conditionstype.objects.all()
    return render(request, "conditiontype.html", {"conditions": conditions})

def brands(request):
    brand_name = Brandtype.objects.all()
    print(brand_name)
    return render(request, "brands.html", {"brands": brand_name})
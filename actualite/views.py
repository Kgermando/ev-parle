from django.shortcuts import render,redirect
from django.contrib import messages # for message
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from actualite.models import Actualite

# Create your views here.
def actualite_view_home(request):
    actualite = Actualite.objects.all().order_by("-created")
    paginator_home = Paginator(actualite, 1)
    paginator_laterale = Paginator(actualite, 3)
    paginator = Paginator(actualite, 9)
    page = request.GET.get('page')
    try:
        actualite_list_home = paginator_home.page(page)
        actualite_list_laterale = paginator_laterale.page(page)
        actualite_list = paginator.page(page)
    except PageNotAnInteger:
        actualite_list_home = paginator_home.page(1)
        actualite_list_laterale = paginator_laterale.page(1)
        actualite_list = paginator.page(1)
    except EmptyPage:
        actualite_list_home = paginator_home.page(paginator_home.num_pages)
        actualite_list_laterale = paginator_laterale.page(paginator_laterale.num_pages)
        actualite_list = paginator.page(paginator.num_pages)
    
    context = {
        'actualite_list_home': actualite_list_home,
        'actualite_list_laterale': actualite_list_laterale,
        'actualite_list': actualite_list
    }
    template_name = 'pages/actualite.html'
    return render(request, template_name, context)


def actualite_view_detail(request, id):
    actualite_list = Actualite.objects.get(id=id)
    context = {
        "actualite_list": actualite_list
    }
    template_name = 'pages/actualite-view.html'
    return render(request, template_name, context)



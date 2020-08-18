from django.shortcuts import render,redirect
from django.contrib import messages # for message
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from app.models import Home, Lois, ContactForm
from app.forms import CommentForm, Comment

from actualite.models import Actualite
from sondage.models import Sondage
# Create your views here.

def home_view(request):
    home_list = Home.objects.all()
    actualite = Actualite.objects.all().order_by("-created")
    lois = Lois.objects.all().order_by("-created")
    sondage = Sondage.objects.all().order_by("-created")

    paginator_actualite = Paginator(actualite, 2)
    paginator_lois = Paginator(lois, 2)
    paginator_sondage = Paginator(sondage, 2)
    page = request.GET.get('page')
    try:
        actualite_list = paginator_actualite.page(page)
        lois_list = paginator_lois.page(page)
        sondage_list = paginator_lois.page(page)
    except PageNotAnInteger:
        actualite_list = paginator_actualite.page(1)
        lois_list = paginator_lois.page(1)
        sondage_list = paginator_sondage.page(1)
    except EmptyPage:
        actualite_list = paginator_actualite.page(paginator_actualite.num_pages)
        lois_list = paginator_lois.page(paginator_lois.num_pages)
        sondage_list = paginator_sondage.page(paginator_sondage.num_pages)

    context = {
        'home_list': home_list,
        'actualite_list': actualite_list,
        'lois_list': lois_list,
        'sondage_list': sondage_list
    }
    template_name = 'pages/home.html'
    return render(request, template_name, context)


def lois_view(request):
    """
        List des lois
    """
    lois = Lois.objects.all().order_by("-created")
    paginator = Paginator(lois, 10)
    page = request.GET.get('page')
    try:
        lois_list = paginator.page(page)
    except PageNotAnInteger:
        lois_list = paginator.page(1)
    except EmptyPage:
        lois_list = paginator.page(paginator.num_pages)

    context = {
        "lois_list":lois_list
    }
    template_name = 'pages/lois.html'
    return render(request, template_name, context)


def lois_view_detail(request, id):
    """
        Vue detail de la lois
    """
    lois = Lois.objects.get(id=id)
    comments = Comment.objects.filter(lois= id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.comment_title = request.user
            form.lois = lois
            form.comment = request.POST['comment']
            form.save()
            return redirect('app:lois-view', id)
    else:
        form = CommentForm()
    context = {
        'lois': lois,
        'comments': comments,
        'form': form, 
        }
    template_name = 'pages/lois-view.html'
    return render(request, template_name, context)


def contact_view(request):
    template_name = 'pages/contact.html'

    if  request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        objet_name = request.POST['objet_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        message = request.POST['message']
        #print(first_name,last_name,objet_name,email_id,phone_num,message)
        if len(first_name)<3 or len(last_name)<3 or len(email_id)<5 or len(phone_num)<10 or len(message)<10:
            messages.error(request,'Svp, remplissez les champs correctement')
        else:
            contact_us = ContactForm(first_name=first_name,last_name=last_name,objet_name=objet_name,email_id=email_id,phone_num=phone_num,message=message)
            contact_us.save()
            messages.success(request, 'Merci! Nous avons réçu votre message')
            return redirect('/contact')

    return render(request, template_name, context=None)

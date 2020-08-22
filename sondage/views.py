from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from sondage.models import Sondage

# Create your views here.
def sondage_view(request):
    sondage_list = Sondage.objects.all().order_by('-created')
    context = {
        'sondage_list': sondage_list
    }
    template_name = 'pages/sondage.html'
    return render(request, template_name, context)


def sondage_view_detail(request, sondage_id):
    sondage_list = Sondage.objects.get(id= sondage_id)
    context = {
        'sondage_list': sondage_list
    }
    template_name = 'pages/sondage-view.html'
    return render(request, template_name, context)


# @login_required(login_url='/accounts/login/')
def vote(request, sondage_id):
    # sondage = Sondage.objects.get(id= sondage_id)
    sondage = get_object_or_404(Sondage, pk=sondage_id)
    # if not sondage.user_can_vote(request.user):
    #     messages.error(
    #         request, "You already voted this poll", extra_tags='alert alert-warning alert-dismissible fade show')
    #     return redirect("sondage:sondage")

    if request.method == 'POST':
        selected_option = request.POST['sondage']
        if selected_option == 'option1':
            sondage.vote_yes +=1
        elif selected_option == 'option2':
            sondage.vote_no +=1
        elif selected_option == 'option3':
            sondage.vote_null +=1
        else:
            return HttpResponse(400, 'Invalid Form')

        sondage.save()

        return redirect('sondage:vote', sondage_id)    
    context = {
        'sondage' : sondage
    }
    template_name = 'pages/vote.html'
    return render(request, template_name, context)




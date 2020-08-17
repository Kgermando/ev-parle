from django.shortcuts import render

# Create your views here.
def team_view(request):
    template_name = 'pages/team.html'
    return render(request, template_name, context=None)

def about_view(request):
    template_name = 'pages/about.html'
    return render(request, template_name, context=None)

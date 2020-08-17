from django.shortcuts import render

# Create your views here.
def actualite_view(request):
    template_name = 'pages/actualite.html'
    return render(request, template_name, context=None)


def actualite_view_detail(request, pk):
    context = {}
    template_name = 'pages/actualite-view.html'
    return render(request, template_name, context)
from django.urls import path

from actualite.views import actualite_view, actualite_view_detail

app_name = 'actualite'
urlpatterns = [
    path('actualite/', actualite_view, name='actualite'),
    path('actualite/<int:id>', actualite_view_detail, name= 'actualite-view-detail'),
]

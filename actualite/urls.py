from django.urls import path

from actualite.views import actualite_view_home, actualite_view_detail

app_name = 'actualite'
urlpatterns = [
    path('actualite/', actualite_view_home, name='actualite'),
    path('actualite-view/<int:id>', actualite_view_detail, name= 'actualite-view-detail'),
]

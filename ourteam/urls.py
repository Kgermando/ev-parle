from django.urls import path

from ourteam.views import about_view, team_view


app_name = 'ourteam'
urlpatterns = [
    path('', about_view, name='about'),
    path('ourteam<int:id>', team_view, name='ourteam'),
]

from django.urls import path

from sondage.views import sondage_view, sondage_view_detail, vote

app_name = 'sondage'
urlpatterns = [
    path('sondage/', sondage_view, name='sondage'),
    path('sondage-view/<sondage_id>', sondage_view_detail, name='sondage-view'),
    path('vote/<sondage_id>/', vote, name='vote')
]

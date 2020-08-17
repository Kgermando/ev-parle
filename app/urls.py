from django.urls import path

from app.views import home_view, contact_view, lois_view, lois_view_detail

app_name = 'app'
urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('lois/', lois_view, name='lois'),
    path('lois-view/<int:id>', lois_view_detail , name="lois-view"),
]

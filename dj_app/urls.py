from django.urls import path
from django.views.generic import TemplateView


app_name = 'dj_app'


urlpatterns = [
    path('', TemplateView.as_view(template_name='dj_app/index.html'), name='index'),
]
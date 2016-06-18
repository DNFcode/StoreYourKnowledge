from django.conf.urls import url
from views import *
from django.views.generic import TemplateView
from django.forms import ModelForm

app_name = 'main'
urlpatterns = [
    url(r'^home/$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^goal/$', TemplateView.as_view(template_name='goal.html'), name='goal'),

]
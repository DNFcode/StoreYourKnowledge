from django.conf.urls import url
from django.contrib.auth.views import login, logout
from .views import *
from .forms import UserAuthForm
from django.core.urlresolvers import reverse_lazy

app_name = 'users'
urlpatterns = [
    url(r'^create/', create, name='create'),
    url(r'^login/', login,
        {
            'template_name': 'login.html',
            'authentication_form': UserAuthForm,
            # 'redirect_authenticated_user': True
        }, name='login'),
    url(r'^logout/', logout,
        {
            'next_page': reverse_lazy('index')
        }, name='logout')
]
from django.conf.urls import url
from django.views.generic import TemplateView

app_name = 'storage'
urlpatterns = [
    url(r'^create/', TemplateView.as_view(template_name="storage_index.html"), name='index')
]
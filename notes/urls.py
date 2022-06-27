from django.urls import path
from django.views.generic import TemplateView

app_name = 'notes'

urlpatterns = [
    path('', TemplateView.as_view(template_name="notes/index.html")),
]

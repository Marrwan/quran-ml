from django.urls import path
from .views import RecitationView

urlpatterns = [
    path('recite/', RecitationView.as_view(), name='recitation'),
]

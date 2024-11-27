from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_email, name='generate_email'),
    path('inbox/<int:email_id>/', views.view_inbox, name='view_inbox'),
    # other paths
]

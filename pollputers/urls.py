from django.urls import path
from django.views.generic import TemplateView
from .views import *
from . import views
# used to link url to thing I actually coded
urlpatterns = [
    path('', views.processlist, name='list'),
    path('subpross/', views.create_view_process, name='subpross'),
    path('subpross/thank/', views.endsubmission, name='thank'),
    path('<id>/delete', delete_view)
]
"""
URL configuration for HABIT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from . import views
urlpatterns = [
    path('', views.habit_list, name='habit_list'),
    path('add/', views.habit_create, name='habit_create'),
    path('habit/<int:habit_id>/', views.habit_detail, name='habit_detail'),
    path('habit/<int:habit_id>/complete/', views.habit_mark_complete, name='habit_mark_complete'),
    path('habit/<int:habit_id>/incomplete/', views.habit_mark_incomplete, name='habit_mark_incomplete'),
    path('habit/<int:habit_id>/edit/', views.habit_edit, name='habit_edit'),
    path('habit/<int:habit_id>/delete/', views.habit_delete, name='habit_delete'),
]

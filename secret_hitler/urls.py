"""secret_hitler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from laws import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('quemequem', views.how_is_how, name="how_is_how"),
    path('shuffle_players', views.shuffle_players, name="shuffle_players"),
    path('take_three', views.take_three, name="take_three"),
    path('take_one', views.take_one, name="take_one"),
    path('cards_shuffle', views.cards_shuffle, name="cards_shuffle"),
    path('game', views.game, name="game"),
]

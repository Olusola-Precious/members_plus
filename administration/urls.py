from django.urls import path
from . import views
urlpatterns = [
    path('', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('panel', views.index, name="home"),
    path('edit', views.edit, name="edit"),
    path('view', views.view, name="view"),
    path('add', views.addMember, name="add"),
]

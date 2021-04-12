from django.urls import path
from homepage import views

urlpatterns = [
    # path('', views.index, name="index"),


    path('', views.index, name="index-bookmark"),
    path('new/', views.new_update_bookmark, name="new-bookmark"),

    path('<int:pk>/update/', views.new_update_bookmark, name="update-bookmark"),

    path('<int:pk>/deleted/', views.delete_bookmark, name="delete-bookmark"),

    path('search/', views.search, name="search"),


]
from django.urls import path
from homepage import views

urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new_update_bookmark, name="new-bookmark"),

    path('<int:pk>/update/', views.new_update_bookmark, name="update-bookmark"),

    path('<int:pk>/deleted/', views.delete_bookmark, name="delete-bookmark"),

    path('<int:b_id>/copy-to/<int:f_id>/', views.copy_to_folder, name="copy-to-folder"),

    path('search/', views.search, name="search"),

    path('folder/<int:id>/', views.display_folder_content, name="folder-content"),

    path('folder/rename/<int:id>/', views.folder_rename, name="folder-rename"),

    path('folder/<int:id>/delete/', views.folder_delete, name="folder-delete"),



]
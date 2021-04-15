from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from homepage.models import Bookmark, Folder


def index(request):
    bookmarks = Bookmark.objects.filter(folder_name=None).order_by('-timestamp')

    folders = Folder.objects.all()
    params = {
        'bookmarks': bookmarks,
        'folders': folders,
    }
    return render(request, 'homepage/index.html', params)


def new_update_bookmark(request, pk=None):

    if request.method == 'POST':

        name = request.POST['name']
        description = request.POST['description']
        url = request.POST['url']
        tags = request.POST['tags']


        if request.POST.get("new") == "new":
            bookmark_obj = Bookmark(name=name, url=url, tags=tags, description=description)
            bookmark_obj.save()
            messages.success(request, f"Your bookmark '{name}' has been successfully.")
            return redirect('index')

        if request.POST.get("update") == "update":
            bookmark_obj = Bookmark.objects.get(pk=pk)
            bookmark_obj.name = name
            bookmark_obj.description = description
            bookmark_obj.url = url
            bookmark_obj.tags = tags
            bookmark_obj.save()

        messages.success(request, f"Your bookmark '{bookmark_obj.name}' has been successfully updated.")
        return redirect('index')

    else:
        return HttpResponse("<h1>Get request not available</h1>")


def delete_bookmark(request, pk):
    if request.method == "POST":
        bookmark_obj = Bookmark.objects.get(pk=pk)
        bookmark_obj.delete()
        messages.success(request, f"Your bookmark was successfully deleted.")
        return redirect('index')


def search(request):
    if request.method == 'GET':
        search_query = request.GET['search']
        bookmark_search = Bookmark.objects.filter(name__icontains=search_query)
        params = {
            'searches': bookmark_search,
            'search_query': search_query,
        }
        return render(request, 'homepage/search.html', params)


def copy_to_folder(request, b_id=None, f_id=None):
    bookmark_id = Bookmark.objects.get(id=b_id)
    bookmark_id.folder_name = Folder.objects.get(id=f_id)
    bookmark_id.save()
    messages.success(request, f"Your bookmark was successfully sent to '{bookmark_id.folder_name}'.")
    return redirect('index')


def display_folder_content(request, id):
    folder_object = Folder.objects.get(id=id)
    bookmark_object = Bookmark.objects.filter(folder_name=folder_object)
    params = {
        'bookmarks': bookmark_object,
    }

    return render(request, 'homepage/display_folder_content.html', params)


def folder_rename(request, id):
    if request.method == 'POST':
        folder_obj = Folder.objects.get(id=id)
        folder_obj.name = request.POST['name']
        folder_obj.save()
        messages.success(request, f"Your bookmark folder was successfully renamed.")
        return redirect('index')


def folder_delete(request, id):
    folder_delete_object = Folder.objects.get(id=id)
    deleted_folder_name = folder_delete_object.name
    bookmark_objects_to_delete = Bookmark.objects.filter(folder_name=folder_delete_object)
    folder_delete_object.delete()

    for bookmark in bookmark_objects_to_delete:
        bookmark.delete()
    messages.success(request, f"Your bookmark folder '{deleted_folder_name}'.")
    return redirect('index')


def new_folder(request):
    if request.method == 'POST':
        new_folder_name = request.POST['name']
        folder_object = Folder(name=new_folder_name)
        folder_object.save()
        messages.success(request, f"Folder '{new_folder_name}' was successfully created.")
        return redirect('index')


def view_bookmark(request, id):
    bookmark_obj = Bookmark.objects.get(id=id)
    params = {
        'bookmark': bookmark_obj,
    }

    return render(request, 'homepage/view_bookmark.html', params)
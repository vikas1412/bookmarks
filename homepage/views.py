from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from homepage.models import Bookmark


def index(request):
    bookmarks = Bookmark.objects.all()
    params = {
        'bookmarks': bookmarks,
    }
    return render(request, 'homepage/index.html', params)


def new_update_bookmark(request, pk=None):

    if request.method == 'POST':

        name = request.POST['name']
        description = request.POST['description']
        url = request.POST['description']
        tags = request.POST['tags']

        if request.POST.get("new") == "new":
            bookmark_obj = Bookmark(name=name, url=url, tags=tags, description=description)
            bookmark_obj.save()
            return redirect('index-bookmark')

        if request.POST.get("update") == "update":
            bookmark_obj = Bookmark.objects.get(pk=pk)
            bookmark_obj.name = name
            bookmark_obj.description = description
            bookmark_obj.url = url
            bookmark_obj.tags = tags
            bookmark_obj.save()

        return redirect('index-bookmark')

    else:
        return HttpResponse("<h1>Get request not available</h1>")


def delete_bookmark(request, pk):
    if request.method == "POST":
        bookmark_obj = Bookmark.objects.get(pk=pk)
        bookmark_obj.delete()
        return redirect('index-bookmark')


def search(request):
    if request.method == 'GET':
        search_query = request.GET['search']
        bookmark_search = Bookmark.objects.filter(name__icontains=search_query)
        params = {
            'searches': bookmark_search,
            'search_query': search_query,
        }
        return render(request, 'homepage/search.html', params)

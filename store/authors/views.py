from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from authors.forms import AuthorModelForm
from authors.models import Authors


@login_required(login_url='/users/login/')
def authors_create_form(request):
    form = AuthorModelForm()
    if request.method == 'POST':
        form = AuthorModelForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            url = reverse("home")
            return redirect(url)
    return render(request, 'authors/forms/create.html',
                  context={"form": form})


def authors_list(request):
    authors = Authors.get_all_authors()
    return render(request, 'authors/list.html',
                  context={"authors": authors})


def authors_detail(request, id):
    author = Authors.get_author_by_id(id)
    return render(request, 'authors/authorDetails.html',
                  context={"author": author})


@login_required(login_url='/users/login/')
def authors_delete(request, id):
    author =Authors.get_author_by_id(id)
    author.delete()
    return redirect('/authors/list')

@login_required(login_url='/users/login/')
def authors_update(request, id):
    author = Authors.get_author_by_id(id)
    form = AuthorModelForm(instance=author)
    if request.method == 'POST':
        form = AuthorModelForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect(author.list_url)
    return render(request, 'authors/forms/update.html',
                  context={"form": form})

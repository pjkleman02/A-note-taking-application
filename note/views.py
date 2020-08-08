from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post
from django.urls import reverse

def home(request):
    context = {'notes': Post.objects.all()}
    return render(request, 'note/home.html', context)

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def get_success_url(self):
        return reverse('notepad')

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']

    def get_success_url(self):
        return reverse('notepad')

class PostDeleteView(DeleteView):
    model = Post
    
    def get_success_url(self):
        return reverse('notepad')

from django.views.generic import DetailView, DeleteView, ListView, UpdateView, CreateView

from .models import Joke


class JokeCreateView(CreateView):
    model = Joke
    fields = ['question', 'answer']


class JokeDetailView(DetailView):
    model = Joke


class JokeListView(ListView):
    model = Joke


class JokeUpdateView(UpdateView):
    model = Joke
    fields = ['question', 'answer']

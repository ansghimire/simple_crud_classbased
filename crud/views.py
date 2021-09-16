from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import Profile
from .forms import ProfileForm
from django.urls import reverse_lazy


class Create(CreateView):
    template_name = 'crud/create.html'
    form_class = ProfileForm
    success_url = reverse_lazy('list')


class List(ListView):
    template_name = 'crud/list.html'
    model = Profile
    context_object_name = 'data'


class Detail(DetailView):
    model = Profile
    template_name = 'crud/detail.html'
    context_object_name = 'data'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(uuid=pk)

        obj = queryset.get()
        return obj


class Delete(DeleteView):
    model = Profile
    success_url = reverse_lazy('list')

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(uuid=pk)

        obj = queryset.get()
        return obj


class Update(UpdateView):
    form_class = ProfileForm
    model = Profile
    template_name = "crud/update.html"
    success_url = reverse_lazy('list')

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(uuid=pk)

        obj = queryset.get()
        return obj





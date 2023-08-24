from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)

from .models import Publications


class PublicationsListView(ListView):
    model = Publications
    template_name = 'posts/home.html'
    context_object_name = 'posts'
    paginate_by = 50


    def get_queryset(self):
        return Publications.objects.all()
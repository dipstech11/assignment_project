from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserList(generic.ListView):
    context_object_name = 'user_list'
    queryset = User.objects.all()
    template_name = 'user_list.html'

class UserDetailView(generic.DetailView):
    model = User
    template_name = 'user_detail.html'

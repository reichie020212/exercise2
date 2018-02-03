# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import ValidWord
from .forms import ValidWordForm

# Create your views here.

def printed(request, pk):
    validword = get_object_or_404(ValidWord, pk=pk)
    return render(request, 'exercise1/printed.html', {'validword': validword})

def print_exercise1(request):
    if request.method == "POST":
        form = ValidWordForm(request.POST)
        if form.is_valid():
            validword = form.save(commit=False)
            validword.saveValid()
            validword.listword = validword.__str__()
            validword.save()
            return redirect('printed', pk=validword.pk)     
    else:
        form = ValidWordForm()
    	return render(request, 'exercise1/home.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
           # user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def create(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))

    else:
        form = UserCreateForm()

    return render(request, "create.html", {"form": form})



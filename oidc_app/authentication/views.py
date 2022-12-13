
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import View


class CustomLoginView(View):
    def get(self, request):
        user = User.objects.get(username="admin")
        login(request, user)
        return redirect(reverse("home"))
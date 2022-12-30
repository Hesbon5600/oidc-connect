from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

from django.contrib.auth.views import LogoutView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from oidc_app.core.oidc_logout import oidc_logout


class CustomLoginView(View):
    def get(self, request):
        user = User.objects.get(username="admin")
        login(request, user)
        return redirect(reverse("home"))


class LogoutViewSet(LogoutView):
    """
    API endpoint that handles user logout
    """

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        """
        Override the dispatch method to add the okta logout functionality
        """

        oidc_logout(request)  # This is the function that does the oidc logout
        logout(request)  # This is the django logout
        redirect_to = self.get_success_url()
        if redirect_to != request.get_full_path():
            # Redirect to target page once the session has been cleared.
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

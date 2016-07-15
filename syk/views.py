from django.views.generic.base import RedirectView
from django.conf import settings


class HomePageRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            url = getattr(settings, "LOGIN_REDIRECT_URL")
        else:
            url = getattr(settings, "LOGOUT_REDIRECT_URL")
        return url

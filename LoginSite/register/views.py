from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
from .forms import LoginForm


class Top(LoginRequiredMixin, generic.TemplateView):
    template_name = 'register/top.html'
    
    def get(self, request, **kwargs):
        ctx = {
            'username': self.request.user.username
        }
        return self.render_to_response(ctx)

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'register/login.html'


class Logout(LogoutView):
    """ログアウトページ"""
    template_name = 'register/logout.html'
    
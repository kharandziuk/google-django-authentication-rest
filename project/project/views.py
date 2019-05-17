from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class PageView(LoginRequiredMixin, TemplateView):
        template_name = 'home.html'
        login_url = reverse_lazy('social:begin', args=['facebook'])

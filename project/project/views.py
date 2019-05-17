from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class AboutView(LoginRequiredMixin, TemplateView):
        template_name="about.html"
        login_url = reverse_lazy('social:begin', args=['facebook'])

class IndexView(TemplateView):
        template_name="index.html"

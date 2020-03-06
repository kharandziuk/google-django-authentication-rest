from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.urls import reverse_lazy
from facepy import SignedRequest
from facepy.exceptions import SignedRequestError

from social_django.models import UserSocialAuth

class AboutView(LoginRequiredMixin, TemplateView):
    template_name="about.html"
    login_url = reverse_lazy('social:begin', args=['google-oauth2'])

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        return context


class IndexView(TemplateView):
        template_name="index.html"

class DeauthorizeView(View):
    def post(self, request, *args, **kwargs):
        try:
            signed_request = request.POST['signed_request']
        except (KeyError):
            return HttpResponse(status=400, content='Invalid request')
        try:
            signed_request_data = SignedRequest.parse(
                signed_request,
                settings.SOCIAL_AUTH_FACEBOOK_SECRET
            )
        except (SignedRequestError):
            return HttpResponse(status=400, content='Invalid request')
        user_id = signed_request_data['user_id']
        try:
            user = UserSocialAuth.objects.get(uid=user_id, provider=facebook).user
        except(UserSocialAuth.DoesNotExist):
            return HttpResponse(status=400, content='Invalid request')
        user.update(is_active=False)
        return HttpResponse(status=201)

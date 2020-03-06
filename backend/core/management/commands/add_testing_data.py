import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from oauth2_provider.models import Application

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        root = User.objects.create_superuser(settings.DEFAULT_ROOT_USER, 'admin@example.com', settings.DEFAULT_ROOT_PASS)
        Application.objects.create(
            client_id=settings.OUR_OAUTH2_CLIENT_ID,
            client_secret=settings.OUR_OAUTH2_CLIENT_SECRET,
            user=root,
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_PASSWORD,
            name='OAuth2 App For Tesing',
        )

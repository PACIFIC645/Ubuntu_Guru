from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission, User


class Command(BaseCommand):
    help = 'Assigns the manage_polls permission to a specified user.'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='The username to assign the permission to')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        permission = Permission.objects.get(codename='manage_polls', content_type__app_label='user_auth')
        user, _ = User.objects.get_or_create(username=username)
        user.user_permissions.add(permission)
        user.save()
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission, User


class Command(BaseCommand):
    help = 'Assigns the manage_polls permission to a specified user.'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='The username to assign the permission to')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        permission = Permission.objects.get(codename='manage_polls', content_type__app_label='user_auth')
        user, _ = User.objects.get_or_create(username=username)
        user.user_permissions.add(permission)
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully assigned "manage_polls" permission to "{username}"'))
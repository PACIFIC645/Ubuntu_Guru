# ubuntu_guru/apps.py

from django.apps import AppConfig

class UbuntuGuruConfig(AppConfig):
    """
    Configuration class for the Ubuntu_Guru Django application.

    This class configures the Ubuntu_Guru application, setting the default
    auto field type and the application name used within the Django project.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Ubuntu_Guru'


from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # Import the signals in the app
    def ready(self):
        import users.signals

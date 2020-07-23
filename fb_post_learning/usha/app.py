from django.apps import AppConfig


class UshaAppConfig(AppConfig):
    name = "usha"

    def ready(self):
        from usha import signals # pylint: disable=unused-variable

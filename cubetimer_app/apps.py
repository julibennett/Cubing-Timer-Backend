from django.apps import AppConfig


class CubetimerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cubetimer_app'

    def ready(self):
        import cubetimer_app.signals
        

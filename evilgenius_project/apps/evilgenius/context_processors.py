from django.conf import settings

def configuration(request):
    return {
        "settings": settings,
    }
# Imports
import os
from django.core.asgi import get_asgi_application
# End Imports


# Config
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uyuchun.settings')
application = get_asgi_application()
# End Config

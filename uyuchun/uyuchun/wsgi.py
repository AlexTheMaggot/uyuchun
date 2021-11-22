# Imports
import os
from django.core.wsgi import get_wsgi_application
# End Imports


# Config
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uyuchun.settings')
application = get_wsgi_application()
# End Config

"""
WSGI config for universidad project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/DGV2019/universidad'

if path not in sys.path:
	sys.path.append(path)

from django.core.wsgi import get_wsgi_application
from whitwnoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'universidad.settings')

#application = get_wsgi_application()
application = DjangoWhiteNoise(get_wsgi_application())

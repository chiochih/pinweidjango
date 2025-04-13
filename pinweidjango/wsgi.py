"""
WSGI config for pinweidjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pinweidjango.settings')

# application = get_wsgi_application()




import os
import sys
from django.core.wsgi import get_wsgi_application

# Debug log
with open("C:/pinweidjango/wsgi_log.txt", "w") as f:
    f.write("wsgi.py 執行成功\n")
    f.write(f"Python 可執行檔：{sys.executable}\n")
    f.write(f"系統路徑：{sys.path}\n")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pinweidjango.settings')
application = get_wsgi_application()

import os, sys
sys.path.append('/var/www/mightylemon/apps')
sys.path.append('/usr/local/lib/python2.5/site-packages/django')
sys.path.append('/usr/lib/python2.5/site-packages/')
sys.path.append('/var/www/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mightylemon.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

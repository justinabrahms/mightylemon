import os, sys, site
sys.path.append('/var/www/mightylemon/')
sys.path.append('/var/www/mightylemon/mightylemon/apps')
site.addsitedir('/var/www/mightylemon/env/lib/python2.6/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'mightylemon.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

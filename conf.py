# conf.py 

import os
import sys
import django
sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'YUbuntu_Guru.settings'
django.setup()


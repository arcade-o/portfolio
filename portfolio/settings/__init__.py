import os

if get_secret('PIPELINE') == 'production':
    from .production import *
else:
    from .local import *

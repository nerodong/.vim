Vim�UnDo� ��+v_b�Lf�A_1Ǧ�2%y��f   �          w         /       /   /   /    S�ŝ   	 _�                     o        ����                                                                                                                                                                                                                                                                                                                                                             S���     �   o   q   �          �   o   q   �    5�_�                    p       ����                                                                                                                                                                                                                                                                                                                                                             S���     �   o   q   �          /home/dumap5�_�                    p       ����                                                                                                                                                                                                                                                                                                                                                             S���     �   o   q   �          /home/duma5�_�                    p   .    ����                                                                                                                                                                                                                                                                                                                                                             S���     �   o   q   �      .    /home/dumasdong/Github/Django-Practice/Tem5�_�                    p       ����                                                                                                                                                                                                                                                                                                                                                             S��     �   o   q   �      3    /home/dumasdong/Github/Django-Practice/Template5�_�                    p   4    ����                                                                                                                                                                                                                                                                                                                                                             S��    �   o   q   �      4    "/home/dumasdong/Github/Django-Practice/Template5�_�                    s        ����                                                                                                                                                                                                                                                                                                                p   5                                        S��     �               �   ## Django settings for waka project.       DEBUG = True   TEMPLATE_DEBUG = DEBUG       
ADMINS = (   .    # ('Your Name', 'your_email@example.com'),   )       MANAGERS = ADMINS       DATABASES = {       'default': {   j        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.   U        'NAME': '',                      # Or path to database file if using sqlite3.   ;        # The following settings are not used with sqlite3:           'USER': 'Nerodong',           'PASSWORD': 'dongke',   �        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.   O        'PORT': '8000',                      # Set to empty string for default.       }   }       M# Hosts/domain names that are valid for this site; required if DEBUG is False   G# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts   ALLOWED_HOSTS = []       C# Local time zone for this installation. Choices can be found here:   7# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name   E# although not all choices may be available on all operating systems.   E# In a Windows environment this must be set to your system time zone.   TIME_ZONE = 'America/Chicago'       E# Language code for this installation. All choices can be found here:   :# http://www.i18nguy.com/unicode/language-identifiers.html   LANGUAGE_CODE = 'en-us'       SITE_ID = 1       I# If you set this to False, Django will make some optimizations so as not   -# to load the internationalization machinery.   USE_I18N = True       E# If you set this to False, Django will not format dates, numbers and   ,# calendars according to the current locale.   USE_L10N = True       I# If you set this to False, Django will not use timezone-aware datetimes.   USE_TZ = True       O# Absolute filesystem path to the directory that will hold user-uploaded files.   (# Example: "/var/www/example.com/media/"   MEDIA_ROOT = ''       G# URL that handles the media served from MEDIA_ROOT. Make sure to use a   # trailing slash.   D# Examples: "http://example.com/media/", "http://media.example.com/"   MEDIA_URL = ''       E# Absolute path to the directory static files should be collected to.   H# Don't put anything in this directory yourself; store your static files   <# in apps' "static/" subdirectories and in STATICFILES_DIRS.   )# Example: "/var/www/example.com/static/"   STATIC_ROOT = ''       # URL prefix for static files.   E# Example: "http://example.com/static/", "http://static.example.com/"   STATIC_URL = '/static/'       &# Additional locations of static files   STATICFILES_DIRS = (   K    # Put strings here, like "/home/html/static" or "C:/www/django/static".   2    # Always use forward slashes, even on Windows.   =    # Don't forget to use absolute paths, not relative paths.   )       ># List of finder classes that know how to find static files in   # various locations.   STATICFILES_FINDERS = (   :    'django.contrib.staticfiles.finders.FileSystemFinder',   >    'django.contrib.staticfiles.finders.AppDirectoriesFinder',   ?#    'django.contrib.staticfiles.finders.DefaultStorageFinder',   )       4# Make this unique, and don't share it with anybody.   ASECRET_KEY = 'kjzz2v&atsrl54qo3%gya&p%1z4-__+ge*r^c&f2kcpr%*5d-2'       K# List of callables that know how to import templates from various sources.   TEMPLATE_LOADERS = (   0    'django.template.loaders.filesystem.Loader',   5    'django.template.loaders.app_directories.Loader',   ,#     'django.template.loaders.eggs.Loader',   )       MIDDLEWARE_CLASSES = (   0    'django.middleware.common.CommonMiddleware',   ;    'django.contrib.sessions.middleware.SessionMiddleware',   0    'django.middleware.csrf.CsrfViewMiddleware',   >    'django.contrib.auth.middleware.AuthenticationMiddleware',   ;    'django.contrib.messages.middleware.MessageMiddleware',   A    # Uncomment the next line for simple clickjacking protection:   ?    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',   )       ROOT_URLCONF = 'waka.urls'       H# Python dotted path to the WSGI application used by Django's runserver.   *WSGI_APPLICATION = 'waka.wsgi.application'       TEMPLATE_DIRS = (   X    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".   6    "/home/dumasdong/Github/Django-Practice/Template",   2    # Always use forward slashes, even on Windows.   =    # Don't forget to use absolute paths, not relative paths.   )       INSTALLED_APPS = (       'django.contrib.auth',   "    'django.contrib.contenttypes',       'django.contrib.sessions',       'django.contrib.sites',       'django.contrib.messages',   !    'django.contrib.staticfiles',   2    # Uncomment the next line to enable the admin:       # 'django.contrib.admin',   <    # Uncomment the next line to enable admin documentation:   !    # 'django.contrib.admindocs',   )       ;# A sample logging configuration. The only tangible logging   8# performed by this configuration is to send an email to   ;# the site admins on every HTTP 500 error when DEBUG=False.   =# See http://docs.djangoproject.com/en/dev/topics/logging for   ># more details on how to customize your logging configuration.   LOGGING = {       'version': 1,   &    'disable_existing_loggers': False,       'filters': {            'require_debug_false': {   6            '()': 'django.utils.log.RequireDebugFalse'   	        }       },       'handlers': {           'mail_admins': {               'level': 'ERROR',   /            'filters': ['require_debug_false'],   9            'class': 'django.utils.log.AdminEmailHandler'   	        }       },       'loggers': {           'django.request': {   (            'handlers': ['mail_admins'],               'level': 'ERROR',               'propagate': True,   
        },       }   }5�_�      	              v       ����                                                                                                                                                                                                                                                                                                                p   5                                        S�7�     �   u   w   �          'django.contrib.auth',    �   v   x   �          �   v   x   �    5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                p   5                                        S�O     �         �              'USER': 'Nerodong',5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                p   5                                        S�O     �         �              'USER': 'erodong',5�_�   
                        ����                                                                                                                                                                                                                                                                                                                p   5                                        S�O     �         �              'USER': 'rodong',5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5                                        S�O     �         �              'USER': 'odong',5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5                                        S�O     �         �              'USER': 'dong',5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5                                        S�O     �         �              'USER': 'ong',5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5                                        S�O     �         �              'USER': 'ng',5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5                                        S�O     �         �              'USER': 'g',5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5                                        S�O     �         �              'USER': '',5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5                                        S�O	     �         �              'PASSWORD': 'dongke',5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5                                        S�O	     �         �              'PASSWORD': 'ongke',5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5                                        S�O	     �         �              'PASSWORD': 'ngke',5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5                                        S�O	     �         �              'PASSWORD': 'gke',5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5                                        S�O	     �         �              'PASSWORD': 'ke',5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5                                        S�O
     �         �              'PASSWORD': 'e',5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5                                        S�O    �         �              'PASSWORD': '',5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5          +          S       v   S    S��:     �         �      �        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5          +          S       v   S    S��:     �         �      �        'HOST': '27.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5          +          S       v   S    S��:     �         �      �        'HOST': '7.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5          +          S       v   S    S��:     �         �      �        'HOST': '.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5          +          S       v   S    S��:     �         �      �        'HOST': '0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.5�_�                           ����                                                                                                                                                                                                                                                                                                                p   5          +          S       v   S    S��:     �         �      �        'HOST': '.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.5�_�                            ����                                                                                                                                                                                                                                                                                                                p   5          +          S       v   S    S��:     �         �      �        'HOST': '0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.5�_�      !                      ����                                                                                                                                                                                                                                                                                                                p   5          +          S       v   S    S��;     �         �      �        'HOST': '.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                p   5          +          S       v   S    S��;    �         �      �        'HOST': '1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.5�_�   !   #           "          ����                                                                                                                                                                                                                                                                                                                             +          S       v   S    S��?     �         �      O        'PORT': '8000',                      # Set to empty string for default.5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                             +          S       v   S    S��?     �         �      N        'PORT': '000',                      # Set to empty string for default.5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                             +          S       v   S    S��?     �         �      M        'PORT': '00',                      # Set to empty string for default.5�_�   $   &           %          ����                                                                                                                                                                                                                                                                                                                             +          S       v   S    S��@    �         �      L        'PORT': '0',                      # Set to empty string for default.5�_�   %   '           &          ����                                                                                                                                                                                                                                                                                                                             +          S       v   S    S��Q    �         �      U        'NAME': '',                      # Or path to database file if using sqlite3.5�_�   &   (           '   v       ����                                                                                                                                                                                                                                                                                                                             +          S       v   S    S��     �   v   x   �          �   v   x   �    5�_�   '   )           (   w       ����                                                                                                                                                                                                                                                                                                                             +          S       v   S    S��     �   v   x   �          ''5�_�   (   *           )   w       ����                                                                                                                                                                                                                                                                                                                             +          S       v   S    S��!     �   v   x   �          'waka.'5�_�   )   +           *   w       ����                                                                                                                                                                                                                                                                                                                             +          S       v   S    S��!     �   v   x   �      
    'aka.'5�_�   *   ,           +   w       ����                                                                                                                                                                                                                                                                                                                             +          S       v   S    S��"     �   v   x   �      	    'ka.'5�_�   +   -           ,   w       ����                                                                                                                                                                                                                                                                                                                             +          S       v   S    S��"     �   v   x   �          'a.'5�_�   ,   .           -   w       ����                                                                                                                                                                                                                                                                                                                             +          S       v   S    S��"     �   v   x   �          '.'5�_�   -   /           .   w       ����                                                                                                                                                                                                                                                                                                                             +          S       v   S    S��#    �   v   x   �          ''5�_�   .               /   w       ����                                                                                                                                                                                                                                                                                                                w   	          +          S       v   S    S�Ŝ   	 �   v   x   �          'books'5��
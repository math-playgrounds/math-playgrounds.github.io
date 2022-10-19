from mathplayground.settings import *  # noqa: F403,F401

project = 'mathplayground'
s3prefix = 'ctl'

# serve static files off S3
AWS_STORAGE_BUCKET_NAME = s3prefix + "-" + project + "-static-stage"
AWS_S3_OBJECT_PARAMETERS = {
    'ACL': 'public-read',
}
AWS_PRELOAD_METADATA = True
STATICFILES_STORAGE = 'cacheds3storage.CompressorS3BotoStorage'

S3_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = ('https://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME)
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_ROOT = STATIC_ROOT  # noqa: F405
COMPRESS_URL = STATIC_URL
DEFAULT_FILE_STORAGE = 'cacheds3storage.MediaRootS3BotoStorage'
COMPRESS_STORAGE = 'cacheds3storage.CompressorS3BotoStorage'
MEDIA_URL = S3_URL + 'uploads/'
AWS_QUERYSTRING_AUTH = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/' + project + '.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

try:
    from mathplayground.local_settings import *  # noqa: F403,F401
except ImportError:
    pass

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage,S3ManifestStaticStorage


class StaticStorage(S3ManifestStaticStorage):
    location = 'static'
    file_overwrite = False

class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False
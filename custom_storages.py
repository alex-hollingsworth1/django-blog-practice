from storages.backends.s3boto3 import S3Boto3Storage


class StaticFileStorage(S3Boto3Storage):
    location = "static"
    default_acl = "public-read"
    file_overwrite = False
    querystring_auth = False  # Don't add auth querystrings to URLs


class MediaFileStorage(S3Boto3Storage):
    location = "media"
    file_overwrite = False

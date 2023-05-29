import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


TRUE_FLAGS = ('true', 'True', '1')
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
VK_API_VERSION = '5.131'

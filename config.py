from os import environ, path as p

# module vars
_basedir = p.dirname(__file__)
_parentdir = p.dirname(_basedir)

# configuration
class Config(object):
    db_name = 'scraperwiki.sqlite'
    DATA_URL = 'http://www.devinfo.org/libraries/ws/REST/1/en/JSON/ALL/MRD/ALL'
    DATA_LOCATION = 'Data.item.Observation.item'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % p.join(_basedir, db_name)
    DEBUG = False
    TESTING = False
    CHUNK_SIZE = 10000
    ROW_LIMIT = None


class Scraper(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % p.join(_parentdir, db_name)


class Production(Config):
    pass


class Development(Config):
    DEBUG = True
    ROW_LIMIT = 50


class Test(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    DEBUG = True
    ROW_LIMIT = 3
    TESTING = True

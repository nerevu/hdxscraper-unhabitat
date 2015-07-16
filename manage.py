#!/usr/bin/env python
import os.path as p

from subprocess import call
from pprint import pprint
from urllib2 import urlopen
from ijson import items

from flask import current_app as app
from flask.ext.script import Manager
from app import create_app, db, utils
from app.models import Data

manager = Manager(create_app)
manager.add_option('-m', '--mode', dest='mode', default='Development')
manager.main = manager.run


@manager.command
def check():
    """Check staged changes for lint errors"""
    call(p.join(_basedir, 'bin', 'check-stage'), shell=True)


@manager.command
def lint():
    """Check style with flake8"""
    call('flake8 ckanutils tests', shell=True)


@manager.command
def pipme():
    """Install requirements.txt"""
    call('pip install -r requirements.txt', shell=True)


@manager.command
def require():
    """Create requirements.txt"""
    cmd = 'pip freeze -l | grep -vxFf dev-requirements.txt > requirements.txt'
    call(cmd, shell=True)


@manager.command
def test():
    """Run nose and script tests"""
    call('nosetests -xv', shell=True)


@manager.command
def createdb():
    """Creates database if it doesn't already exist"""

    with app.app_context():
        db.create_all()
        print 'Database created'


@manager.command
def cleardb():
    """Removes all content from database"""

    with app.app_context():
        db.drop_all()
        print 'Database cleared'


@manager.command
def setup():
    """Removes all content from database and creates new tables"""

    with app.app_context():
        cleardb()
        createdb()


@manager.command
def run():
    """Removes all content from database and creates new tables"""
    limit = 0

    with app.app_context():
        f = urlopen(app.config['DATA_URL'])
        objects = items(f, app.config['DATA_LOCATION'])
        row_limit = app.config['ROW_LIMIT']
        chunk_size = min(row_limit or 'inf', app.config['CHUNK_SIZE'])
        debug = app.config['DEBUG']

        if app.config['TESTING']:
            createdb()

        for records in utils.chunk(objects, chunk_size):
            count = len(records)
            limit += count
            flattened = [dict(utils.flatten_fields(r)) for r in records]

            if debug:
                print('Inserting %s records into the database...' % count)
                # pprint(flattened)

            db.engine.execute(Data.__table__.insert(), flattened)

            if row_limit and limit >= row_limit:
                break

        if debug:
            print('Successfully inserted %s records into the database!' % limit)


if __name__ == '__main__':
    manager.run()

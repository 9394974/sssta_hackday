from app import create_app, db

import pytest


@pytest.fixture(scope='session')
def app():
    app = create_app(test=True)

    with app.app_context():
        db.create_all()
        yield app

        db.session.remove()
        db.drop_all()


@pytest.fixture(scope='function')
def client(app):

    with app.test_client() as client:
        yield client


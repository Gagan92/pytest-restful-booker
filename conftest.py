import pytest
from tinydb import TinyDB, Query

from core.datastore import TinyDBManager


def pytest_addoption(parser):
    """
    py.test hook for adding command line switches which can accept values
    at runtime.
    """
    # Generic cmdline switches

    parser.addoption('--env', action='store', default=[],
                     help='env name for the primary app')
    parser.addoption('--run_id', action='store', default='NA',
                     help='run id of the test cases')
    parser.addoption('--product', action='store', default=[],
                     help='env name for the leankit app')


@pytest.fixture(scope='session')
def tiny_db_store():
    tiny_db=TinyDBManager()
    yield tiny_db


@pytest.fixture(scope='session')
def initialize_db():
    db_handler = None
    return db_handler

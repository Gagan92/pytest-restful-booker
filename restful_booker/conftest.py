import pytest
from utils import file_utils as utils


@pytest.fixture(scope="session", autouse=True)
def read_urls():
    return utils.read_yml("restful_booker/core/constants.yml")


@pytest.fixture(scope="session")
def set_cmdline_opts(request):
    """
    Picks cmdline args passed by the user from request.config and
    stores in a dict (cmd_opts)
    Also initializes logging level in PyTestLogger.
    :param user_account:
    :type user_account:
    :param request: py.test request fixture
    :return: populated cmd_opts dict
    """
    product=request.config.getoption('--product')
    env = request.config.getoption('--env')
    connector_details=utils.read_yml("/connectors.yml")

    return {"env": connector_details[product.upper()][env.upper()]['ENV']}


@pytest.fixture(scope='session', autouse=True)
def read_connectors(request):
    """
    This is to read the connector details from yml file
    :param request:
    :return: dict containing environment and user
    """

    product= request.config.getoption('--product')
    connectors = read_constants(product)
    env = request.config.getoption('--env')
    return connectors[product.upper()][env]


def read_constants(product):
    """
    This is to read the constants from yml file
    :param product:
    :type product:
    :param request:
    :return: dict containing environment and user
    """
    return utils.read_yml(f"{product.lower()}/core/constants.yml")
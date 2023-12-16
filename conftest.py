import pytest


def pytest_addoption(parser):
    parser.addoption("--url", default='http://localhost:8080')
    parser.addoption('--debug_log', action='store_true')


@pytest.fixture(scope="session")
def config(request):
    url = request.config.getoption('--url')
    debug_log = request.config.getoption('--debug_log')

    return {
        'url': url,
        'debug': debug_log
    }

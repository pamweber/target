import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--term", action="store", default=" ",
        help="the string that we will search for (default = space)"
    )
    parser.addoption(
        "--method", action="store", default="1",
        help="the string method that we will use for the search [1, 2, 3] (default = 1)"
    )
    parser.addoption(
        "--times", action="store", default=1,type=int,
        help="the number of times we should run the test (default = 1)")


@pytest.fixture
def term(request):
    return request.config.getoption("--term")

@pytest.fixture
def method(request):
    return request.config.getoption("--method")

@pytest.fixture
def times(request):
    return request.config.getoption("--times")

import pytest



def pytest_addoption(parser):
    parser.addoption(
        "--suite-name",
        action="store",
        default="yoyo",
        help="'Default yoyo"
    )


def pytest_configure(config):
    name = config.getoption("--suite-name")
    if name:
        config._inicache['junit_suite_name']=name

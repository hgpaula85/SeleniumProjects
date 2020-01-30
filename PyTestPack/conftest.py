import pytest


@pytest.yield_fixture(scope="module")
def one_time_set_up():
    print("\nRun conftest one time set up")

    yield
    print("Run conftest one time tear down")
    print("_" * 50)


@pytest.yield_fixture(scope="function")
def set_up():
    print("\nRun conftest function set up")

    yield
    print("\nRun conftest function tear down")
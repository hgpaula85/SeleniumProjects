import pytest


@pytest.yield_fixture()
def set_up():
    print("\nRun demo 2 set up")

    yield
    print("\nRun demo 2 tear down")
    print("-" * 50)


def test_demo_2_test_01(set_up):
    print("Running demo 2 test 01")


def test_demo_2_test_02(set_up):
    print("Running demo 2 test 01")

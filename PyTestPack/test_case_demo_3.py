"""
py.test test_mod.py                     # run tests in module
py.test somepath                        # run all tests below somepath
py.test test_module.py::test_method     # only run test_method in test_module

-s to print statements
-v verbose
"""

import pytest


@pytest.fixture()
def set_up():
    print("\nRun demo 3 set up")

    yield
    print("\nRun demo 3 tear down")
    print("-" * 50)


def test_demo_3_test_01(set_up):
    print("Running demo 3 test 01")


def test_demo_3_test_02(set_up):
    print("Running demo 3 test 02")

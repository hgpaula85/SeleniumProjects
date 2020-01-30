"""
PyTest Naming Conventions
When using pytest, it is very important to follow naming conventions.
If we don't follow naming conventions, then pytest will not pick up tests from the file.
-> File names should start or end with “test”, as in test_example.py or example_test.py
-> Class name should start with “Test”, as in TestExample
-> Test method names should start with “test_”, as in test_example

You can refer to the official documentation for more details:
https://docs.pytest.org/en/latest/

Fixture finalization / executing teardown code
pytest supports execution of fixture specific finalization code when the fixture goes out of scope.
By using a yield statement instead of return, all the code after the yield statement serves as the teardown code
"""

import pytest


@pytest.fixture()
def set_up():
    print("\nRun demo 1 set up")

    yield
    print("\nRun demo 1 tear down")
    print("-" * 50)


def test_demo_1_test_01(set_up):
    print("Running test 01")


def test_demo_1_test_02(set_up):
    print("Running test 02")

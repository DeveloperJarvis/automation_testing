#automation testing conditions for web application
import pytest

@pytest.fixture
def setup():
    print("open browser")
    yield
    print("close browser")

def test_1(setup):
    print("test_1")
    
def test_2():
    print("test_2")

def test_3():
    print("test_3")

def test_4():
    print("test_4")

def test_5():
    print("test_5")

def test_6():
    print("test_6")

def test_7():
    print("test_7")

def test_8():
    print("test_8")
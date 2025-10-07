import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator import add

def test_add_positive():
    assert add(2, 3) == 5
    assert add(100, 1042) == 1142

def test_add_negative():
    assert add(-2, -3) == -5
    assert add(-100, -123) == -223

def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(0, -3) == -3
    assert add(4, -4) == 0

def test_add_large():
    assert add(1000000000, 2000000000) == 3000000000

def test_add_float():
    assert add(2.5, 3.1) == 5.6
    assert add(-2.5, -3.1) == -5.6

def test_add_invalid():
    with pytest.raises(TypeError):
        add("2", 4)
    with pytest.raises(TypeError):
        add(2, "3")

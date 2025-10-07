import pytest
import sys
import os
from calculator import add, subtract

# 添加项目根目录到 Python 路径，以便导入 calculator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_add_positive():
    """测试正数相加"""
    assert add(2, 3) == 5
    assert add(100, 1042) == 1142


def test_add_negative():
    """测试负数相加"""
    assert add(-2, -3) == -5
    assert add(-100, -123) == -223


def test_add_zero():
    """测试零的边界情况"""
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(0, -3) == -3
    assert add(4, -4) == 0


def test_add_large():
    """测试大数相加"""
    assert add(1000000000, 2000000000) == 3000000000


def test_add_float():
    """测试浮点数相加"""
    assert add(2.5, 3.1) == 5.6
    assert add(-2.5, -3.1) == -5.6


def test_add_invalid():
    """测试无效输入"""
    with pytest.raises(TypeError):
        add("2", 4)
    with pytest.raises(TypeError):
        add(2, "3")


def test_subtract_positive_numbers():
    """测试正数相减"""
    assert subtract(5, 3) == 2
    assert subtract(10, 5) == 5


def test_subtract_negative_numbers():
    """测试负数相减"""
    assert subtract(-2, -3) == 1
    assert subtract(-5, 3) == -8


def test_subtract_zero():
    """测试零的边界情况"""
    assert subtract(5, 0) == 5
    assert subtract(0, 3) == -3
    assert subtract(0, 0) == 0


def test_subtract_float_numbers():
    """测试浮点数相减"""
    assert subtract(5.5, 2.5) == 3.0
    assert subtract(1.5, 0.5) == pytest.approx(1.0)

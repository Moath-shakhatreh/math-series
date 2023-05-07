import pytest
from Functions.series import febonacci
from Functions.series import lucas
from Functions.series import sum



def test_1():
    actual= febonacci(0)
    expected = 0
    assert actual == expected

def test_2():
    actual= febonacci(1)
    expected = 1
    assert actual == expected

def test_3():
    actual= febonacci(5)
    expected = 5
    assert actual == expected

def test_4():
    actual= febonacci(10)
    expected = 55
    assert actual == expected


def test_5():
    actual= lucas(0)
    expected = 2
    assert actual == expected

def test_6():
    actual= lucas(1)
    expected = 1
    assert actual == expected

def test_7():
    actual= lucas(5)
    expected = 11
    assert actual == expected

def test_8():
    actual= lucas(10)
    expected = 123
    assert actual == expected

def test_9():
    actual= sum(0,2,3)
    expected = 2
    assert actual == expected

def test_10():
    actual= sum(1,3,4)
    expected = 4
    assert actual == expected

def test_11():
    actual= sum(1,3,4)
    expected = 4
    assert actual == expected

def test_12():
    actual= sum(5,4,5)
    expected = 37
    assert actual == expected

def test_13():
    actual= sum(11,1,1)
    expected = 144
    assert actual == expected
import pytest 
import bloomdata as ld

def test_increment_int():
    assert ld.increment_num(3) == 4
    assert ld.increment_num(100) == 101

def test_increment_float():
    assert ld.increment_num(5.5) == 6.5 

def test_increment_neg_int():
    assert ld.increment_num(-5) == -4

'''This function will assert that one (1) float value will 
be added to the negative float called in the function.'''

def test_increment_neg_float():
    assert ld.increment_num(-5.2) == -4.2

'''This function will assert that '''

def test_multiply_num():
    assert ld.multiply_num(4) == 16

def test_subtract_num():
    assert ld.subtract_num(4) == 3

def test_sq_rt_num():
    assert ld.sq_rt_num(5) == 25 
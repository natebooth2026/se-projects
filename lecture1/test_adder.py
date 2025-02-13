# TEST ADDER
# bash command used: pytest test_adder.py

from adder import add
import pytest

def test_add():
    assert(add(0,0) == 0) # just this (didn't know add only returned 0) == weak evidence
    assert(add(1,1) == 2) # just this (when it returned x+x) == not convincing 
    assert(add(7,5) == 12) # fails when "return x+x", passes with 1st below
    assert(add(-7,-5) == -12) # fails when "return abs(x) + abs(x)" & "return abs(x) + abs(y)"
    assert(add(-3.25, 5.25) == 2.0) # passes when "return int(x) + int(y)"
    assert(add(3.25, 5.25) == 8.5) # fails with above, passes with below
    assert(add(0.1234, 0.1234) == 0.2468) # fails when x == 0.1234 returns 0, passes with below
    assert(add(10**6, 10**6) == 2 * 10**6) #passes --> "return x+y"

"""
def test_invalid_inputs():
    with pytest.raises(type): #DOESN'T WORK
        assert("1", 2)
"""
import pytest 
from proj.sample_module import SampleClass

class TestSample:

    def test_add(self):
        obj = SampleClass(2,3,4)
        assert obj.add() == 9

    def test_mul(self):
        obj = SampleClass(2,3)
        assert obj.mul() == 6
    
    def test_divide(self):
        obj = SampleClass(4,2)
        assert obj.divide() == 2
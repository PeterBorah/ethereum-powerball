from eth_tools import Contract, address
from nose.tools import assert_equal, assert_true
from pyethereum import tester as t
from random import randint

RANDOM_NUMBERS = 0

class TestRNG:
    def setup(self):
        self.state = t.state()
        self.contract = Contract("contracts/rng.se", self.state)
        self.state.mine(2)

    def test_returns_array_of_numbers(self):
        assert_equal(len(self.contract.call(RANDOM_NUMBERS)), 6)

    def test_returns_sorted(self):
        result = self.contract.call(RANDOM_NUMBERS)
        assert_true(result[0] > 0)
        assert_true(result[0] <= result[1])
        assert_true(result[1] <= result[2])
        assert_true(result[2] <= result[3])
        assert_true(result[3] <= result[4])

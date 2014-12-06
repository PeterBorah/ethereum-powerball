from eth_tools import Contract, address
from nose.tools import assert_equal
from pyethereum import tester as t
from random import randint

RANDOM_NUMBERS = 0

class TestRNG:
    def setup(self):
        self.state = t.state()
        self.contract = Contract("contracts/rng.se", self.state)
        self.state.mine(1)

    def test_returns_array_of_numbers(self):
        assert_equal(len(self.contract.call(RANDOM_NUMBERS)), 6)

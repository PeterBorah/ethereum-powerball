from eth_tools import Contract, address
from nose.tools import assert_equal
from pyethereum import tester as t

INITIALIZE = 0
SET_PAYOUTS = 1
BUY_TICKET = 2
GET_TICKET_OWNER = 3
GET_TICKET_NUMBERS = 4
TRANSFER_TICKET = 5

class TestLotto:
    def setup(self):
        self.state = t.state()
        self.contract = Contract("contracts/lotto.se", self.state)

    def test_buying_ticket(self):
        numbers = [1, 3, 4, 5, 9, 35]
        ticket_id = self.contract.call(BUY_TICKET, numbers)[0]

        assert_equal(address(self.contract.call(GET_TICKET_OWNER, [ticket_id])[0]), t.a0)
        assert_equal(self.contract.call(GET_TICKET_NUMBERS, [ticket_id]), numbers)

        new_numbers = [1, 5, 7, 8, 10, 35]
        new_ticket_id = self.contract.call(BUY_TICKET, new_numbers)[0]

        assert_equal(address(self.contract.call(GET_TICKET_OWNER, [new_ticket_id])[0]), t.a0)
        assert_equal(self.contract.call(GET_TICKET_NUMBERS, [new_ticket_id]), new_numbers)

    def test_transfering_ticket(self):
        numbers = [1, 3, 4, 5, 9, 35]
        ticket_id = self.contract.call(BUY_TICKET, numbers)[0]

        self.contract.call(TRANSFER_TICKET, [ticket_id, t.a1])

        assert_equal(address(self.contract.call(GET_TICKET_OWNER, [ticket_id])[0]), t.a1)

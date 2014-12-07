ethereum-powerball
==================

"Powerball"-style lottery written in Serpent, for prophetx's bounty.


# Basic setup:

* Create contract on the blockchain, and call `initialize` to set yourself as the admin.
* Send an appropriate amount of funds to support the prizes you are configuring. Because Powerball-style lotteries have set prizes, you cannot rely on ticket sales to cover payouts.
* Set the ticket price, length of lottery and redemption period with the `set_configuration` method.
* If desired, you can set a custom RNG contract as well. The default one uses `block.prevhash` for its entropy.
* Set the desired payouts with `set_payouts`. See [Wikipedia](http://en.wikipedia.org/wiki/Powerball#Payout_and_odds) for odds. Note that you will also need to specify how much the Jackpot goes up if it's not won.
* Start the lottery with `start_lotto`! You will be unable to make changes to configuration or withdraw money until it has ended.
* As you make profits, use `withdraw` between lottos to claim them!

# For players

* Buy tickets by picking 5 (unique) numbers between 1 and 59, and one "powerball" number between 1 and 35. The return value of `buy_ticket` will be your ticket ID.
* You can transfer your tickets with `transfer_tickets`.
* After the lotto has ended, and before the redemption period ends, call `claim_winnings` with your ticket ID to claim your prize!

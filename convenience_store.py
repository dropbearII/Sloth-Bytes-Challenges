"""Weekly Challenge

Given a total due and an array representing the amount of change in your pocket, determine whether or not you are able to pay for the item.
Change will always be represented in the following order: quarters, dimes, nickels, pennies.
Example: changeEnough([25, 20, 5, 0], 4.25) return true because:
25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50.
This means you can afford the item, so return true.

Examples
    changeEnough([2, 100, 0, 0], 14.11) ➞ false
    changeEnough([0, 0, 20, 5], 0.75) ➞ true
    changeEnough([30, 40, 20, 5], 12.55) ➞ true
    changeEnough([10, 0, 0, 50], 3.85) ➞ false
    changeEnough([1, 0, 5, 219], 19.99) ➞ false

Notes
    quarter = 25 cents / $0.25
    dime= 10 cents / $0.10
    nickel = 5 cents / $0.05
    penny = 1 cent / $0.01
"""


def change_enough(change: list[int], price: float) -> bool:
    """
    Check if you have enough change to pay the price.

    Parameters
    ----------
    change : list[int]
        List represents change available as [quarter, dime, nickel, penny].
            quarter = 25 cents / $0.25
            dime= 10 cents / $0.10
            nickel = 5 cents / $0.05
            penny = 1 cent / $0.01
    price : float
        Total price to pay.

    Returns
    -------
    Boolean
        True - enough change available
        False - not enough change available
    """
    total_change: float = change[0]*0.25 + change[1]*0.1 + change[2]*0.05 + change[3]*0.01
    if total_change >= price:
        return True
    else:
        return False

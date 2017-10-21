import pandas as pd


def rebalance_contributions(current_balance, target_allocation,
                            future_contributions):
    """
    :param current_balance: Current balances as {"name": amount}
    :param target_allocation: Target allocation as {"name": percentage}
    :param future_contributions: Future contributions to tweak.
    :return: pd.DataFrame
                   Allocation abs  Allocation %
        A            26.0          0.26
        B            38.0          0.38
        C            36.0          0.36
    """
    total = sum(current_balance.values()) + future_contributions
    if current_balance.keys() != target_allocation.keys():
        raise ValueError("current_balance and target_allocation must have the "
                         "same keys!")
    assets = sorted(current_balance.keys())
    allocation_abs = [target_allocation[k] * total - current_balance[k]
                      for k in assets]
    df = pd.DataFrame({"Allocation abs": allocation_abs},
                       index=assets)
    df["Allocation %"] = df["Allocation abs"] / sum(df["Allocation abs"])
    return df


import unittest


class FuncTest(unittest.TestCase):

    def test_rebalance_contributions(self):
        current_balance = {"A": 110, "B": 98, "C": 100}
        target_allocation = {"A": 1/3, "B": 1/3, "C": 1/3}
        df = rebalance_contributions(current_balance, target_allocation, 100)
        self.assertAlmostEqual(df["Allocation %"]["A"], 0.26)


if __name__ == "__main__":
    unittest.main()
import json
from decimal import Decimal


with open("trades.json", "r") as file:
    trades = json.load(file)


earned_money = 0
mate_account = 0
for trade in trades:
    if trade["bought"] is not None:
        mate_account += Decimal(trade["bought"])
        earned_money -= (Decimal(trade["bought"])
                         * Decimal(trade["matecoin_price"]))
    if trade["sold"] is not None:
        mate_account -= Decimal(trade["sold"])
        earned_money += (Decimal(trade["sold"])
                         * Decimal(trade["matecoin_price"]))

dict_of_trades = dict(
    earned_money=str(earned_money),
    matecoin_account=str(mate_account)
)

with open("profit.json", "w") as file:
    json_trades = json.dump(dict_of_trades, file, indent=2)

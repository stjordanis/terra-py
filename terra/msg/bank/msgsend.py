from typing import List

from terra.msg.coin import Coin
from terra.utils.jsonserializable import JsonSerializable


class MsgSend(JsonSerializable):
    def __init__(
        self, amount: List[Coin], from_address: str, to_address: str
    ) -> None:
        """Represent the top level of a MsgSend message."""
        self.type = "bank/MsgSend"
        self.value = MsgSendValue(amount, from_address, to_address)


class MsgSendValue(JsonSerializable):
    def __init__(
        self, amount: List[Coin], from_address: str, to_address: str
    ) -> None:
        """Values of a MsgSend message."""
        self.amount = sorted(amount, key=lambda o: o.denom)
        self.from_address = from_address
        self.to_address = to_address

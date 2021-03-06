from terra.msg.coin import Coin
from terra.utils.jsonserializable import JsonSerializable


class MsgUndelegate(JsonSerializable):
    def __init__(
        self, delegator_address: str, validator_address: str, amount: Coin
    ) -> None:
        """Represent the top level of a MsgUndelegate message."""
        self.type = "staking/MsgUndelegate"
        self.value = MsgUndelegateValue(
            delegator_address, validator_address, amount
        )


class MsgUndelegateValue(JsonSerializable):
    def __init__(
        self, delegator_address: str, validator_address: str, amount: Coin
    ) -> None:
        """Values of a MsgUndelegate message."""
        self.delegator_address = delegator_address
        self.validator_address = validator_address
        self.amount = amount

# Modules

Documentation of the modules apis.

# terra

Account:
```python
terra.Account(
    mnemonic: str,
    account: int = 0,
    index: int = 0,
    sequence: str = "0",
    account_number: str = "0",
    chain_id: str = "",
) -> None

terra.Account.generate() -> Account
```

# terra.msg

Coin:
```python
Coin(
    amount: str,
    denom: str,
) -> None

Coin().to_json(
    sort: bool = False,
) -> str
```

Fee:
```python
Fee(
    gas: str,
    amount: List[terra.msg.Coin],
) -> None

Fee().to_json(
    sort: bool = False,
) -> str
```

InOut:
```python
InOut(
    address: str,
    coins: List[terra.msg.Coin],
) -> None

InOut().to_json(
    sort: bool = False,
) -> str
```

ReturnType:
```python
ReturnType()

ReturnType.BLOCK
ReturnType.ASYNC
ReturnType.SYNC
```

Tx:
```python
Tx(
    fee: terra.msg.Fee,
    memo: str = "",
    mode: str = terra.msg.ReturnType.BLOCK,
    msg: List[terra.utils.JsonSerializable] = [],
    signatures: List[terra.msg.auth.StdSignMessage] = [],
) -> None

Tx().sign_with(
    account: terra.Account,
) -> None

Tx().to_json(
    sort: bool = False,
) -> str
```

## terra.msg.auth

StdSignMsg:
```python
StdSignMsg(
    signature: str,
    pub_key_value: str,
    pub_key_type: str = "tendermint/PubKeySecp256k1",
) -> None

StdSignMsg().to_json(
    sort: bool = False,
) -> str
```

StdTx:
```python
StdTx(
    fee: terra.msg.Fee,
    memo: str = "",
    msg: List[terra.utils.JsonSerializable] = [],  # all terra.msg classes inherit from JsonSerializable
    signatures: List[terra.msg.auth.StdSignMessage] = [],
) -> None

StdTx().sign_with(
    account: terra.Account,
) -> None

StdTx().to_json(
    sort: bool = False,
) -> str
```

## terra.msg.distribution

MsgSetWithdrawAddress:
```python
MsgSetWithdrawAddress(
    delegator_address: str,
    withdraw_address: str,
) -> None

MsgSetWithdrawAddress().to_json(
    sort: bool = False,
) -> str
```

MsgWithdrawDelegatorReward:
```python
MsgWithdrawDelegatorReward(
    delegator_address: str,
    validator_address: str,
) -> None

MsgWithdrawDelegatorReward().to_json(
    sort: bool = False,
) -> str
```

## terra.msg.market

MsgSwap:
```python
MsgSwap(
    trader: str,
    offer_coin: terra.msg.Coin,
    ask_denom: str,
) -> None

MsgSwap().to_json(
    sort: bool = False,
) -> str
```

## terra.msg.oracle

MsgPricePrevote:
```python
MsgPricePrevote(
    price: str,
    salt: str,
    denom: str,
    feeder: str,
    validator: str
) -> None

MsgPricePrevote().to_json(
    sort: bool = False,
) -> str
```

MsgPriceVote:
```python
MsgPriceVote(
    price: str,
    salt: str,
    denom: str,
    feeder: str,
    validator: str,
) -> None

MsgPriceVote().to_json(
    sort: bool = False,
) -> str
```

## terra.msg.pay

MsgMultiSend:
```python
MsgMultiSend(
    inputs: List[terra.msg.InOut],
    outputs: List[terra.msg.InOut],
) -> None

MsgMultiSend().to_json(
    sort: bool = False,
) -> str
```

MsgSend:
```python
MsgSend(
    amount: List[terra.msg.Coin],
    from_address: str,
    to_address: str
) -> None

MsgSend().to_json(
    sort: bool = False,
) -> str
```

## terra.msg.staking

MsgBeginRedelegate:
```python
MsgBeginRedelegate(
    delegator_address: str,
    validator_src_address: str,
    validator_dst_address: str,
    amount: terra.msg.Coin,
) -> None

MsgBeginRedelegate().to_json(
    sort: bool = False,
) -> str
```

MsgDelegate:
```python
MsgDelegate(
    delegator_address: str,
    validator_address: str,
    amount: terra.msg.Coin,
) -> None

MsgDelegate().to_json(
    sort: bool = False,
) -> str
```

MsgUndelegate:
```python
MsgUndelegate(
    delegator_address: str,
    validator_address: str,
    amount: terra.msg.Coin,
) -> None

MsgUndelegate().to_json(
    sort: bool = False,
) -> str
```

# terra.utils

JsonSerializable:
```python
JsonSerializable() -> None

JsonSerializable().to_json(
    sort: bool = False,
) -> str
```

## terra.utils.crypto

generate_salt:
```python
generate_salt() -> str
```

sha256_and_sign:
```python
sha256_and_sign(
    payload: str,
    private_key: str,
    curve: ecdsa.curves.Curve = ecdsa.SECP256k1,
    canonize: bool = True,
) -> bytes
```

sha256:
```python
sha256(
    payload: str,
) -> bytes
```
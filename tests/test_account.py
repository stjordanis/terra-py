from terra import Account

ACCOUNT = {
    "account_address": "terra1ganslgkvaen5gcqfpxu2fvqa08hxpfzn0ayw2s",
    "address": "47670fa2ccee6744600909b8a4b01d79ee60a453",
    "mnemonic": "bread genuine element reopen cliff power mean quiz mutual "
    "six machine planet dry detect edit slim clap firm jelly "
    "success narrow orange echo tomorrow",
    "operator_address": "terravaloper1ganslgkvaen5gcqfpxu2fvqa08hxpfzn0jgn6r",
    "private_key": "861c3746d1bf6bc83acac4c9e72dbe7cdcf944031823b1c7e1248d163"
    "c2b9c01",
    "public_key": "032c2f944ff74e5f40d6c01b171386d3a868c90b25c46ec39a3f4c0702"
    "d4e2cbc6",
    "seed": "271d8892dfc23ed6662a0023080144d0f538d1d002c701b98e813ecc7fab33a4"
    "eef5f9288fd6ba7d68bc53ebd61ed453167fe669a08151ea4113dfdbe856f47a",
}


def test_account():
    a = Account(ACCOUNT["mnemonic"])
    assert a.account_address == ACCOUNT["account_address"]
    assert a.address == ACCOUNT["address"]
    assert a.mnemonic == ACCOUNT["mnemonic"]
    assert a.operator_address == ACCOUNT["operator_address"]
    assert a.private_key == ACCOUNT["private_key"]
    assert a.public_key == ACCOUNT["public_key"]
    assert a.seed == ACCOUNT["seed"]


def test_account_generate():
    a = Account.generate()
    assert len(a.mnemonic.split()) == 24
    assert a.mnemonic != Account.generate().mnemonic

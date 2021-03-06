from httmock import all_requests, HTTMock
import pytest
import requests

from terra import api
from terra import exceptions


@all_requests
def response_200(url, request):
    return {"status_code": 200, "content": '{"test": "test"}'}


@all_requests
def response_404(url, request):
    return {"status_code": 404, "content": ""}


@all_requests
def response_timeout(url, request):
    raise requests.exceptions.Timeout


@all_requests
def response_not_json(url, request):
    return {"status_code": 200, "content": "test"}


@all_requests
def response_too_many_redirects(url, request):
    raise requests.exceptions.TooManyRedirects


@all_requests
def response_generic_exception(url, request):
    raise requests.exceptions.RequestException


def test_client_get_200():
    with HTTMock(response_200):
        assert api.client.Client.get("/") == {"test": "test"}


def test_client_get_404():
    with HTTMock(response_404):
        with pytest.raises(exceptions.ApiError) as e:
            api.client.Client.get("/")
            assert e.match("404")


def test_client_get_timeout():
    with HTTMock(response_timeout):
        with pytest.raises(exceptions.ApiError) as e:
            api.client.Client.get("/")
            assert e.match("timed out")


def test_client_get_not_json():
    with HTTMock(response_not_json):
        with pytest.raises(exceptions.ApiError) as e:
            api.client.Client.get("/")
            assert e.match("json")


def test_client_get_too_many_redirects():
    with HTTMock(response_too_many_redirects):
        with pytest.raises(exceptions.ApiError) as e:
            api.client.Client.get("/")
            assert e.match("redirections")


def test_client_get_generic_exception():
    with HTTMock(response_generic_exception):
        with pytest.raises(exceptions.ApiError) as e:
            api.client.Client.get("/")
            assert e.match("The endpoint could not be accessed")


def test_client_post_200():
    with HTTMock(response_200):
        assert api.client.Client.post("/", {"some": "json"}) == {
            "test": "test"
        }


def test_client_post_404():
    with HTTMock(response_404):
        with pytest.raises(exceptions.ApiError) as e:
            api.client.Client.post("/", {"some": "json"})
            assert e.match("404")


def test_client_post_timeout():
    with HTTMock(response_timeout):
        with pytest.raises(exceptions.ApiError) as e:
            api.client.Client.post("/", {"some": "json"})
            assert e.match("timed out")


def test_client_post_not_json():
    with HTTMock(response_not_json):
        with pytest.raises(exceptions.ApiError) as e:
            api.client.Client.post("/", {"some": "json"})
            assert e.match("json")


def test_client_post_too_many_redirects():
    with HTTMock(response_too_many_redirects):
        with pytest.raises(exceptions.ApiError) as e:
            api.client.Client.post("/", {"some": "json"})
            assert e.match("redirections")


def test_client_post_generic_exception():
    with HTTMock(response_generic_exception):
        with pytest.raises(exceptions.ApiError) as e:
            api.client.Client.post("/", {"some": "json"})
            assert e.match("The endpoint could not be accessed")


def test_get_tendermint_node_info():
    assert list(api.tendermint.node_info.get().keys())[0] == "node_info"


def test_get_tendermint_blocks_latest():
    assert list(api.tendermint.blocks.latest.get().keys())[0] == "block_meta"


def test_get_oracle_denoms_actives():
    assert list(api.oracle.denoms.actives.get().keys())[0] == "height"


def test_get_auth_accounts_by_address():
    address = "terra1d03dz5n3hj8qfzfjvrza8a9t0hejwnjcdsn5cw"
    assert (
        list(api.auth.accounts.by_address.get(address).keys())[0] == "height"
    )


def test_get_bank_balances_by_address():
    address = "terra1d03dz5n3hj8qfzfjvrza8a9t0hejwnjcdsn5cw"
    assert (
        list(api.bank.balances.by_address.get(address).keys())[0] == "height"
    )

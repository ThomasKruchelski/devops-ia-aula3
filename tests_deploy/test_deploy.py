import pytest # type: ignore
from src_alta.app import somar, dividir


def test_deploy_smoke_somar():
    assert somar(4, 6) == 10


def test_deploy_smoke_dividir():
    assert dividir(20, 4) == 5

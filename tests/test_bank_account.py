import pytest
from src.bank_acount import *

@pytest.mark.parametrize('value, extend_result',[
                            (1, 1)])
def test_deposit_possitive(value, extend_result):
    bank_account = BankAccount()
    bank_account.deposit(value)
    assert bank_account.get_balance() == extend_result

@pytest.mark.parametrize('value, extend_result',[
                            (-1, pytest.raises(ValueError)),
                            (0, pytest.raises(ValueError))])
def test_deposit_negative(value, extend_result):
    bank_account = BankAccount()

    with extend_result:
        assert bank_account.deposit(value) == extend_result


@pytest.mark.parametrize('value, extend_result',[
                            (10, 0),
    (0, 10),
    (1, 9)])
def test_withdraw_possitive(value, extend_result):
    bank_account = BankAccount()
    bank_account.deposit(10)
    bank_account.withdraw(value)
    assert bank_account.get_balance() == extend_result


@pytest.mark.parametrize('value, extend_result',[
                            (-1, pytest.raises(ValueError)),
                            (11, pytest.raises(ValueError))])
def test_withdraw_negative(value, extend_result):
    bank_account = BankAccount()

    with extend_result:
        assert bank_account.withdraw(value) == extend_result

@pytest.mark.parametrize('value, extend_result',[
                            (9, 9),
    (1, 1)])
def test_get_balance_possitive(value, extend_result):
    bank_account = BankAccount()
    bank_account.deposit(value)
    assert bank_account.get_balance() == extend_result
"""Parkomat Cash feature tests."""

from pytest_bdd import given, when, then, scenario, parsers
from datetime import datetime

from src.parking_end_time import parking_end_time


@scenario('parkomat-cash.feature', 'Compute end parking timestamp')
def test_compute_end_parking_timestamp():
    """Compute end parking timestamp."""


@scenario('parkomat-cash.feature', 'Not enough money to buy a ticket')
def test_not_enough_money_to_buy_a_ticket():
    """Not enough money to buy a ticket."""


@given(parsers.parse('current time is {current_time}'), target_fixture='current_time_fixture')
def current_time_fixture(current_time):
    """current time is <current_time>."""
    current_time_parsed = datetime.fromisoformat(current_time)
    return dict(current_time=current_time_parsed)


@given(parsers.parse('money amount is {money_amount:g}'))
def money_amount_fixture(money_amount):
    """money amount is <money_amount>."""
    assert isinstance(money_amount, float)


@when('end time is calculated', target_fixture='execution_fixture')
def execution_fixture(current_time_fixture, money_amount):
    """end time is calculated."""
    try:
        current_time_fixture['result'] = parking_end_time(money_amount, current_time_fixture['current_time'])
    except ValueError as error:
        current_time_fixture['result'] = str(error)


@then(parsers.parse('error message is {result}'))
def error_message_is_result(current_time_fixture, result):
    """error message is <result>."""
    assert result in current_time_fixture['result']


@then(parsers.parse('result is {result}'))
def error_message_is_result(current_time_fixture, result):
    """result is <result>."""
    result == current_time_fixture['result']

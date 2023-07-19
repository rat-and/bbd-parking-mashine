from behave import *
from datetime import datetime

from src.parking_end_time import parking_end_time


@given(u'money amount is {money_amount}')
def step_impl(context, money_amount):
    context.money_amount = float(money_amount)


@given(u'current time is {current_time}')
def step_impl(context, current_time):
    context.current_time = datetime.fromisoformat(current_time)


@when(u'end time is calculated')
def step_impl(context):
    try:
        context.calculated_time = parking_end_time(context.money_amount, context.current_time)
    except ValueError as e:
        context.exception = e


@then(u'result is {result}')
def step_impl(context, result):
    assert context.calculated_time == datetime.fromisoformat(result), context.calculated_time


@then(u'error message is {result}')
def step_impl(context, result):
    assert result in str(context.exception)

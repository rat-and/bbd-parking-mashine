from behave import *
from datetime import datetime, timedelta


def parking_end_time(money_amount: float, current_time: datetime, day_offset=False) -> datetime:
    """
    Implementation of parking-end-time calculation function in recurring style. At current stage it considers all days
    to be equally expensive - weekends included (open for coding :) )

    :arg money_amount - Amount of money that John wants to spend on his parking ticket
    :arg current_time - Start Time&Date when John wants to buy his parking ticket
    :arg day_offset - Auxiliary argument to call this function in recurrent fashion. DO NOT CHANGE UNLESS YOU'RE 100%
                      SURE WHAT YOU'RE DOING!

    :returns Time&Date of parking end time
    :raises ValueError if not enough money was inserted
    """
    price_list = [1.70, 7.00, 7.40, 7.90, 7.00]
    minute_offset = 0
    hour_offset = 0
    print(day_offset)

    if money_amount < min(price_list):
        # If function call by recursion day offset is included in current_date
        if not day_offset:
            raise (ValueError('Not enough money'))
    elif min(price_list) <= money_amount <= max(price_list):
        # You have to reach next price to buy more time
        if money_amount < price_list[1]:
            minute_offset = 15
        else:
            hour_offset = 1
    else:
        # >= 4h case
        if money_amount / (price_list[1] + price_list[2] + price_list[3] + price_list[4]) >= 1:
            four_hours_price = price_list[1] + price_list[2] + price_list[3] + price_list[4]
            hour_offset = int(4 + (money_amount - four_hours_price) // price_list[4])
        # 3h < x < 4h case
        elif money_amount / (price_list[1] + price_list[2] + price_list[3]) >= 1:
            hour_offset = 3
        # 2h < x < 3h case
        elif money_amount / (price_list[1] + price_list[2]) >= 1:
            hour_offset = 2
        # 1h < x < 2h case
        elif money_amount / (price_list[1]) >= 1:
            hour_offset = 1
        # x < 1h case
        else:
            hour_offset = 0

    # day offset as a recurred function call
    if hour_offset == 13:
        # twelve hours price
        overpriced_amount = price_list[1] + price_list[2] + price_list[3] + 9 * price_list[4]
        return parking_end_time(money_amount - overpriced_amount - price_list[1],
                                current_time.replace(day=current_time.day + 1),
                                True)
    elif hour_offset > 13:
        # over twelve hours price
        overpriced_amount = price_list[1] + price_list[2] + price_list[3] + 9 * price_list[4]
        return parking_end_time(money_amount - overpriced_amount,
                                current_time.replace(day=current_time.day + 1),
                                day_offset)

    # after paid hours move extra hours to the next day(s)
    if current_time.hour >= 20:
        return parking_end_time(money_amount,
                                current_time.replace(day=current_time.day + 1, hour=8, minute=0),
                                day_offset)
    # paid hours #1
    elif current_time.hour == 19:
        # > 19:45 and paid only for 15min
        if current_time.minute >= 45 and minute_offset == 15:
            return current_time.replace(day=current_time.day + 1, hour=8, minute=current_time.minute - 45)
        # 19:00 <= x < 19:45 and paid for at least 15 min
        elif current_time.minute < 45 and minute_offset == 15:
            return current_time + timedelta(minutes=minute_offset)
        # paid for at least 1 hour
        else:
            # Catch special case for day offset
            if day_offset:
                return current_time
            else:
                return current_time.replace(day=current_time.day + 1, hour=8 + hour_offset - 1)

    # paid hours #2
    elif 8 <= current_time.hour <= 19:
        # move extra hours to the next day(s)
        if current_time.hour + hour_offset > 20:
            overpriced_hours = (current_time.hour + hour_offset) - 20
            if overpriced_hours == 1:
                overpriced_amount = price_list[1]
            elif overpriced_hours == 2:
                overpriced_amount = price_list[1] + price_list[2]
            elif overpriced_hours == 3:
                overpriced_amount = price_list[1] + price_list[2] + price_list[3]
            elif overpriced_hours >= 4:
                overpriced_amount = price_list[1] + price_list[2] + price_list[3] + (overpriced_hours-3) * price_list[4]
            else:
                raise (Exception('Range error'))
            return parking_end_time(overpriced_amount,
                                    current_time.replace(day=current_time.day + 1, hour=8, minute=0),
                                    day_offset)
        else:
            return current_time.replace(hour=current_time.hour + hour_offset, minute=current_time.minute + minute_offset)

    # before paid hours
    elif current_time.hour < 8:
        return parking_end_time(money_amount,
                                current_time.replace(hour=8, minute=0),
                                day_offset)


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
    assert context.calculated_time == datetime.fromisoformat(result)


@then(u'error message is {result}')
def step_impl(context, result):
    assert result in str(context.exception)

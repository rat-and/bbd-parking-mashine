from behave import *


class Parkomat():
    price_list = [1.70, 7.00, 7.40, 7.90, 7.00]

    def __init__(self, time):
        self.time = time

    def get_cost(self):
        if self.time <= 15:
            return self.price_list[0]
        elif self.time > 15 and self.time <= 60:
            return self.price_list[1]
        elif self.time > 60 and self.time <= 120:
            return self.price_list[1] + self.price_list[2]
        elif self.time > 120 and self.time <= 180:
            return self.price_list[1] + self.price_list[2] + self.price_list[3]
        else:
            return self.price_list[1] + self.price_list[2] + self.price_list[3] + ((self.time - 180)//60 + 1) * self.price_list[4]


@when(u'parking time = 10 min')
def step_impl(context):
    context.parkomat = Parkomat(10)


@then(u'parking cost = 1.70 PLN')
def step_impl(context):
    assert context.parkomat.get_cost() == 1.70, context.parkomat.get_cost()


@when(u'parking time = 50 min')
def step_impl(context):
    context.parkomat = Parkomat(50)


@then(u'parking cost = 7.00 PLN')
def step_impl(context):
    assert context.parkomat.get_cost() == 7.00, context.parkomat.get_cost()


@when(u'parking time = 1:25 hours:mins')
def step_impl(context):
    context.parkomat = Parkomat(85)


@then(u'parking cost = 14.40 PLN')
def step_impl(context):
    assert context.parkomat.get_cost() == 14.40, context.parkomat.get_cost()


@when(u'parking time = 2:15 hours:mins')
def step_impl(context):
    context.parkomat = Parkomat(135)


@then(u'parking cost = 22.30 PLN')
def step_impl(context):
    assert context.parkomat.get_cost() == 22.30, context.parkomat.get_cost()


@when(u'parking time = 3:40 hours:mins')
def step_impl(context):
    context.parkomat = Parkomat(220)


@then(u'parking cost = 29.30 PLN')
def step_impl(context):
    assert context.parkomat.get_cost() == 29.30, context.parkomat.get_cost()


@when(u'parking time = 12 hours')
def step_impl(context):
    context.parkomat = Parkomat(720)


@then(u'parking cost = 92.3 PLN')
def step_impl(context):
    assert context.parkomat.get_cost() == 92.3, context.parkomat.get_cost()

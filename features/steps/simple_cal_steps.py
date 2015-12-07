from behave import *
from features.pages.simple_calculator import SimpleCalculator


step_matcher("re")

var1 = ''
var2 = ''
actual_result = ''

@given("I have two number (.*) and (.*) into the calculator")
def step_impl(context,param1, param2):
  global var1
  global var2
  var1 = float(param1)
  var2 = float(param2)


@when("I perform (addition|subtraction|multiplication|division)")
def step_impl(context,operator):
    global var1
    global var2
    global actual_result
    calc = SimpleCalculator(var1, var2)
    if operator == 'addition':
        actual_result = calc.addition()
    if operator == 'subtraction':
        actual_result = calc.subtraction()
    if operator == 'multiplication':
        actual_result = calc.multiplication()
    if operator == 'division':
        actual_result = calc.division()


@then("the result should be (.*) on the screen")
def step_impl(context,expected_result):
    global actual_result
    assert (actual_result == float(expected_result)) is True

from behave import given, when, then

@given("I have Behave installed")
def step_given_behave_installed(context):
    print("Behave is installed!")

@when("I run the tests")
def step_when_run_tests(context):
    print("Running Behave tests...")

@then("I should see the tests pass")
def step_then_tests_pass(context):
    print("Tests executed successfully!")

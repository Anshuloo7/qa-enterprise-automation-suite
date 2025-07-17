from behave import given, when, then

@given("I have Behave installed")
def step_given_behave_installed(context):
    print("Behave is installed!")

@when("I run the tests")
def step_when_run_tests(context):
    base_url = context.env_config["base_url"]
    print(f"Running tests against: {base_url}")

@then("I should see the tests pass")
def step_then_tests_pass(context):
    print("Tests executed successfully!")

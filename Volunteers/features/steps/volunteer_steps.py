from behave import given, when, then
from volunteer import VolunteerRegistration

@given("a volunteer provides valid registration details")
def step_valid_details(context):
    context.system = VolunteerRegistration()
    context.name = "Yosif Yosifov"
    context.email = "Yosif@example.com"
    context.age = 21

@given("a volunteer provides registration details without an email")
def step_missing_email(context):
    context.system = VolunteerRegistration()
    context.name = "Mario Balakchiev"
    context.email = ""
    context.age = 25

@given("a volunteer is under 16 years old")
def step_underage_volunteer(context):
    context.system = VolunteerRegistration()
    context.name = "Tom Hardy"
    context.email = "tom@example.com"
    context.age = 14

@when("the volunteer submits the registration form")
def step_submit_form(context):
    context.result = context.system.register_volunteer(
        context.name,
        context.email,
        context.age
    )

@then("the system should confirm successful registration")
def step_success_message(context):
    assert context.result == "Registration successful"

@then("the system should display an email required error")
def step_email_error(context):
    assert context.result == "Email is required"

@then("the system should reject the registration")
def step_underage_error(context):
    assert context.result == "Volunteer must be at least 16 years old"
Feature: Volunteer Registration
  As a non-profit organisation
  I want volunteers to register online
  So that I can manage volunteer participation efficiently

  Scenario: Successful volunteer registration
    Given a volunteer provides valid registration details
    When the volunteer submits the registration form
    Then the system should confirm successful registration

  Scenario: Missing email address
    Given a volunteer provides registration details without an email
    When the volunteer submits the registration form
    Then the system should display an email required error

  Scenario: Volunteer is under the minimum age
    Given a volunteer is under 16 years old
    When the volunteer submits the registration form
    Then the system should reject the registration
import re

class VolunteerRegistration:
    def __init__(self):
        self.volunteers = []

    def register_volunteer(self, name, email, age):
        if not name.strip():
            return "Name is required"

        if not email.strip():
            return "Email is required"

        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            return "Invalid email address"

        if age < 16:
            return "Volunteer must be at least 16 years old"

        volunteer = {
            "name": name,
            "email": email,
            "age": age
        }

        self.volunteers.append(volunteer)
        return "Registration successful"

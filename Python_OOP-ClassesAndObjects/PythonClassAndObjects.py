#!/usr/bin/python3
import datetime


class User:
    """A member of FriendFace. For now we are
        only storing their name and birthday.
        But soon we will store an uncomfortable
        amount of user information."""

    # Initialization (constructor in other Languages)
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday  # yyyymmdd

        # Extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Return the age of the user in years."""
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)  # Date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)


user = User("Dave Bowman", "19710315")
print(f"Full Name: {user.name}")
print(f"First Name: {user.first_name}")
print(f"Last Name: {user.last_name}")
print(f"BirthDay: {user.birthday}")
print(f"Age: {user.age()}")
# help(User) --> (DocString) This will display a useful overview of User class

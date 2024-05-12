from datetime import date
import inflect

p = inflect.engine()


class Birthday:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def age_in_minutes(self):
        today = date.today()
        difference = (today - date(self.year, self.month, self.day)).days
        return difference * 24 * 60

    def age_in_words(self):
        age_in_minutes = self.age_in_minutes()
        return p.number_to_words(age_in_minutes).replace("-", " ")


def main():
    dob = get_birthday()
    birthday = Birthday(dob.year, dob.month, dob.day)
    print("{} minutes".format(birthday.age_in_words()))
    print("{} moments so dear".format(birthday.age_in_words()))
    print("{} minutes".format(birthday.age_in_words()))
    print("How do you measure, measure a year?")


def get_birthday():
    while True:
        try:
            year = int(input("What year were you born in? "))
            month = int(input("What month were you born in? "))
            day = int(input("What day were you born in? "))
            return date(year, month, day)
        except ValueError:
            print("invalid date")


if __name__ == "__main__":
    main()

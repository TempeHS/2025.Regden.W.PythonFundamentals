from datetime import date
import inflect

p = inflect.engine()


def main():
    beep = date.today()
    dob = get_birthday()
    age_in_minutes = calculate_age_in_minutes(beep, dob)
    age_in_words = p.number_to_words(age_in_minutes)
    print("{} minutes".format(age_in_words.replace("-", " ")))
    print("{} moments so dear".format(age_in_words.replace("-", " ")))
    print("{} minutes".format(age_in_words.replace("-", " ")))
    print("How do you measure, measure a year?")


def get_birthday():
    year = int(input("What year were you born in? "))
    month = int(input("What month were you born in? "))
    day = int(input("What day were you born in? "))
    return date(year, month, day)


def calculate_age_in_minutes(current_date, birth_date):
    difference_in_days = (current_date - birth_date).days
    return difference_in_days * 24 * 60


if __name__ == "__main__":
    main()

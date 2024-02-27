def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not has_minimum_length(s):
        return False
    if not has_maximum_length(s):
        return False
    if not starts_with_letters(s):
        return False
    if not has_valid_structure(s):
        return False
    return True


def has_minimum_length(s):
    return len(s) >= 2


def has_maximum_length(s):
    return len(s) <= 6


def starts_with_letters(s):
    return s[:2].isalpha()


def has_valid_structure(s):
    if s[-1].isdigit() and s[0].isdigit():
        return False
    if s[-1].isdigit() and s[-2].isdigit():
        return False
    return True


main()

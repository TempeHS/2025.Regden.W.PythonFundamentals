months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
}

nmonths = {
    "1": "01",
    "2": "02",
    "3": "03",
    "4": "04",
    "5": "05",
    "6": "06",
    "7": "07",
    "8": "08",
    "9": "09",
    "10": "10",
    "11": "11",
    "12": "12",
}


def main():
    while True:
        try:
            print("Input a date in MM/DD/YYYY or month day, year ")
            date = input().replace(",", " ").replace("/", " ")
            month, day, year = date.split()
            month = month.title()
            day = day = int(day)
            if not 1 <= day <= 31:
                print("invalid date")
                continue
            else:
                pass
            if month in months:
                print(f"{year}-{months[month]}-{day:02d}")
                break
            elif month in nmonths:
                print(f"{year}-{nmonths[month]}-{day:02d}")
                break
            else:
                print("Invalid month")
        except ValueError:
            print("invalid date")


main()

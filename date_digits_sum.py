from datetime import date as date_module, timedelta


def date_iterator(start_date, end_date):
    for i in range((end_date - start_date).days):
        date = start_date + timedelta(i)
        yield (date.strftime("%m"), date.strftime("%d"), date.strftime("%y"))


occurrences = 0
start_date = date_module(2000, 1, 1)
for month, day, year in date_iterator(start_date, date_module.today()):
    first_digits_equality = int(month[0]) + int(day[0]) == int(year[0])
    second_digits_equality = int(month[1]) + int(day[1]) == int(year[1])

    if first_digits_equality and second_digits_equality:
        print(f"{month}/{day}/{year}")
        occurrences += 1

print(f"\nOccurrences: {occurrences}")
print("Average yearly occurrences: " \
    f"{occurrences // (date_module.today().year - start_date.year)}")

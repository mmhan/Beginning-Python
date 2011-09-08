#!/usr/bin/python2

months = [
          'Janurary',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'Spetember',
          'October',
          'November',
          'December'
          ]

endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] + 7 * ['th'] \
        + ['st'];
    
year = raw_input("Year : ")
month = raw_input("Month (1-12): ")
day = raw_input("Day (1-31): ")

month_number = int(month)
day_number = int(day)

print months[month_number] + " " + "%d" % day_number + endings[day_number - 1] + ", " + year

raw_input("<enter> to exit")
#!/usr/bin/python3


holidays_array = [
    ["Jan 01", "New Year's Day"],
    ["Feb 01", "Heroe's Day"],
    ["Apr 07", "Good Friday"],
    ["Apr 07", "Genocide against the Tutsi Memorial Day"],
    ["Apr 10", "Easter Monday"],
    ["Apr 22", "Eid Ul Fitr"],
    ["May 01", "Worker's Day"],
    ["Jun 29", "Eid El Haj"],
    ["Jul 01", "Independence Day"],
    ["Jul 04", "Liberation Day"],
    ["Aug 04", "Assumption Day"],
    ["Dec 25", "Christmas Day"],
    ["Dec 26", "Boxing Day"]
]


def holidays():
    print("Date   | Holiday Name")
    for holiday in holidays_array:
        print(holiday[0], "|", holiday[1])

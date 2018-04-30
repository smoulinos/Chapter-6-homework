
import calendar


cal = calendar.TextCalendar()
cal.setfirstweekday(3)
cal.pryear(2012)



print(cal.formatmonth(2018, 12))


"""
d = calendar.LocaleTextCalendar(6, "Latin")
d.pryear(2012)"



print(calendar.isleap(2020))

cal.pryear(10)
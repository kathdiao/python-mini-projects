import datetime
import calendar

class Calendar:
    def __init__(self):
        self.now = datetime.datetime.now()

    def get_datetime(self):
        return self.now.strftime("%d/%m/%Y %H:%M:%S")

    def get_month_calendar(self):
        return calendar.month(self.now.year, self.now.month)


app = Calendar()

print("Date and Time:")
print(app.get_datetime(), "\n")


print(app.get_month_calendar())

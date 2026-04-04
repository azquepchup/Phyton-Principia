
#Version class:
class Datetime:
    def __init__(self, year = 0, month = 0, day = 0, hour = 0, minute = 0, second = 0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        if month > 12 or month == 0:
            print("Mes no válido")
        elif day > 31 or day == 0:
            print("Día no válido")
        else:
            print(f"{year:04d} - {month:02d} - {day:02d}, {hour:02d}:{minute:02d}:{second:02d}")

Datetime()

#Version función:
#def Datetime(year = 0, month = 0, day = 0, hour = 0, minute = 0, second = 0):
#   if month > 12 or month == 0:
#       print("Mes no valido")
#   if day > 31 or day == 0:
#       print("Dia no valido")
#   else:
#       f"{year:04d} - {month:02d} - {day:02d}, {hour:02d}:{minute:02d}:{second:02d}"

#fecha = datetime()
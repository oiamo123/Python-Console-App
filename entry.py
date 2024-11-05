from datetime import date

class Entry:
    def __init__(self, entryDate, entryHours, hourlyRate):
        self._entryDate: date = entryDate
        self._entryHours: float = entryHours
        self._hourlyRate: float = hourlyRate
        self._entryPay: float = 0.0
        self.calcPay() # Calculate pay on initialization

    #Calculate pay
    def calcPay(self):
        #If hours are less than 44 hours
        if self._entryHours <= 44:
            self._entryPay: float = self._hourlyRate * self._entryHours
        
        #If it's a holiday
        elif Holidays.isHoliday(self._entryDate):
            self._entryPay: float = self._hourlyRate * self._entryHours * 1.5

        #If hours are greater than 44 hours
        else:
            #Calculate overtime pay
            overtime: float = (self._entryHours - 44) * 1.5 * self._hourlyRate
            self._entryPay = 44 * self._hourlyRate + overtime
    
    def __str__(self) -> str:
        return f"{self._entryDate}: {self._entryPay}"
    
class Holidays:
    _holidays: set[date] = {
        date(2024, 1, 1), # New Year's Day
        date(2024, 3, 29), # Good Friday
        date(2024, 7, 1), # Canada day 
        date(2024, 8, 5), # Civic Holiday
        date(2024, 9, 2), # Labour Day
        date(2024, 9, 30), # Reconciliation Day
        date(2024, 10, 14), # Thanksgiving Day
        date(2024, 11, 11), # Remembrance Day
        date(2024, 12, 25) # Christmas
    }

    @staticmethod
    def isHoliday(check_date: date) -> bool:
        return check_date in Holidays._holidays
from datetime import date
from entry import Entry

class User:
    def __init__(self, name, pay):
        self.name: str = name
        self._pay: float = pay
        self._entries: dict = dict()
    
    #Adds entry, returns true or false depending on if entry is valid
    def add_entry(self, entryDate: date, entryHours: float) -> bool:
        #Date is in the future, hours is less than 12 and there isn't already an entry on that date
        if entryDate >= date.today() and entryHours > 0 and entryHours <= 12 and not self._entries.contains(entryDate):
            entry: Entry = Entry(entryDate, entryHours, self._pay)
            self._entries.add(entryDate, entry)
            return True
        else:
            return False
        
    def remove_entry(self, entryDate: date) -> bool:
        if (self._entries.contains(entryDate)):
            self._entries.remove(entryDate)
            return True
        else:
            return False


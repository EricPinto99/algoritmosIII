from DateStruct import DateStruct

class Controller:
    def __init__(self, date):
        self.date = date
    
    def readDate(self):
        self.day = int(input("Day: "))
        self.month = int(input("Month: "))
        self.year = int(input("Year: "))
        
    def validateDate(self):
        self.validate = False
        # Meses com 31 dias
        if (self.monthsEnding31()):
            if (self.day <= 31):
                self.validate = True
        # Meses com 30 dias
        elif (self.monthsEnding30()):
            if (self.day <= 30):
                self.validate = True

        elif(self.month == 2):
            self.validate = True

            if(self.day == 29):
                self.validate = False
                if (self.checkLeapYear()):
                    self.validate = True

        return  self. validate

    def initializeDate(self):
        print("Date: " + str(self.day) + "/" + str(self.month) + "/" + str(self.year))

    def informDays(self):
        self.days = int(input("Enter the days you want to add: "))

    def addDay(self, increment = 1):
        self.day += increment

    def addMonth(self, increment = 1):
        self.month += increment

        if(self.month > 12):
            self.month = 1
            self.addYear()

    def addYear(self, increment = 1):
        self.year += increment

    def manipulateDates(self, lastDay):

        self.counter = 0

        while(self.counter < self.days):
            self.addDay()

            if(self.month == 2):
                lastDay = 28

                if (self.checkLeapYear()):
                    lastDay = 29

            elif (self.monthsEnding30()):
                lastDay = 30

            elif(self.monthsEnding31()):
                lastDay = 31

            if(self.day == lastDay):
                self.day = 0
                self.addMonth()

            self.counter += 1

    def monthsEnding30(self):
        return self.month == 4 or self.month == 6 or self.month == 9 or \
               self.month == 11

    def monthsEnding31(self):
        return self.month == 1 or self.month == 3 or self.month == 5 or \
            self.month == 7 or self.month == 8 or self.month == 10 \
            or self.month == 12

    def checkLeapYear(self):
        self.check = False
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            self.check = True

        return self.check
    
    def dateInFull(self):
        months = ['January','February','March','April','May','Jun','July','August','September','October','November', 'December']
        
        print("Date in Full: " + str(self.day) + "th " + months[self.month-1] + " " + str(self.year))
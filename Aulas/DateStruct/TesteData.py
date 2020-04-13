from DateStruct import DateStruct
from Controller import Controller

d = DateStruct(0,0,0)
dateOperations = Controller(d)

dateOperations.readDate()

if(dateOperations.validateDate()):
    dateOperations.initializeDate()
    if(dateOperations.checkLeapYear()):
        print("The year reported is leap year. ")
    else:
        print("The year reported is not a leap year. ")
    dateOperations.dateInFull()
    print("-----------------------------")
    dateOperations.informDays()
    dateOperations.manipulateDates(dateOperations.days)
    dateOperations.initializeDate()
    print("-----------------------------")

else:
    print("Plase, enter with a correct date. ")

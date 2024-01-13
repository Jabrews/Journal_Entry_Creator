import datetime
from datetime import timedelta
import os
import shutil

class Usercontroller:
    def __init__(self):
        self.date = datetime.date.today()
        self.create = createDirectory(self.date)
        self.delete = deleteDirectory(self.date)
        self.view = viewDirectory(self.date)

    ################MENUS#################
    def mainMenu(self):
        menuLoop = True
        while menuLoop:
            userChoice = str(input("""
            1. Create Directory
            2. Delete Directory
            3. View Directory
            User Option: """))
            if userChoice == "1":
                self.creationMenu()
            elif userChoice == "2":
                self.deletionMenu()
            elif userChoice == "3":
                self.viewMenu()

    def creationMenu(self):
        ##Changes in CURRENT DATA: ##
        displayDate = self.date
        menuLoop = True
        while menuLoop:
            userChoice = str(input(f"""
            CURRENT DATE: {displayDate}
            1. Change Date
            2. Confirm 
            3. Back
            User Option: """))
            if userChoice == "3":
                break
            elif userChoice == "1":
                displayDate = self.create.changeDate()
            elif userChoice == "2":
                self.create.createDirectory(str(displayDate)) ##CHANGE to string for paths

    def deletionMenu(self):
        displayDate = self.date
        menuLoop = True
        while menuLoop:
            userChoice = str(input(f"""
                    CURRENT DATE: {displayDate}
                    1. Change Date
                    2. Confirm 
                    3. Back
                    User Option: """))
            if userChoice == "3":
                break
            elif userChoice == "1":
                displayDate = self.create.changeDate() ##Using same function as creation!
            elif userChoice == "2":
                self.delete.deleteDate(displayDate)

    def viewMenu(self):
        displayDate1 = None
        displayDate2 = self.date
        menuLoop = True
        while menuLoop:
            userChoice = str(input(f"""
                            WARNING: DO NOT TRY DIFFERENT MILLENNIUMS
                            DATE 1 (lowest): {displayDate1}
                            DATE 2 (highest): {displayDate2}
                            1. Change Date 1
                            2. Change Date 2
                            3. Confirm 
                            4. Back
                            User Option: """))
            if userChoice == "4":
                break
            elif userChoice == "1":
                displayDate1 = self.create.changeDate() ##using from create class
            elif userChoice == "2":
                displayDate2 = self.create.changeDate() ##using from create class
            elif userChoice == "3":
                self.view.displayDates(displayDate1, displayDate2)
    #####################################



class createDirectory:
    def __init__(self, date):
        self.date = date
        self.parent_directory = "Data/" #Parent for making directory

    ###########Change Dates############
    def changeDate(self):
        print("Format : yyyy-mm-dd")
        try:
            test_date = self.dateInput()
            return test_date
        except:
            print("Returning To Menu")


    def dateInput(self):
        try:
            userYear = int(input("Year: "))
            userMonth = int(input("Month: "))
            userDay = int(input("Day: "))
            print(f"{userYear} - {userMonth} - {userDay}")
            ##Make date variable##
            newDate = datetime.date(userYear, userMonth, userDay)
        except:
            print("Try Formatting Correctly")
            newDate = self.date
        finally:
            return newDate
        ###Will return the date given by controller class if not valid####

    #########Create Directory##############

    def createDirectory(self, display_date):
        print(display_date)
        userAuthentication = self.Confirm()
        if userAuthentication == True:
            self.makeDirectory(display_date)



    def Confirm(self):
        userChoice = str(input("Are you sure you wish to proceed?: "))
        if userChoice == "yes":
            return True
        else:
            return False

    def makeDirectory(self, display_date):
        datePath = os.path.join(self.parent_directory, display_date)
        print(f"TEST | {datePath}")
        try:
            os.mkdir(datePath)
            print("Sucsefully created directory!")
        except:
            print("Issue Encountered")
    #######################################

class deleteDirectory:
    def __init__(self, date):
        self.date = date
        self.create = createDirectory(self.date)
        self.parent_directory = "Data/"


    def deleteDate(self, display_date):
        userAuthentication = self.create.Confirm()
        if userAuthentication == True:
            datePath = os.path.join(self.parent_directory, str(display_date))
            print(f"TEST | {datePath} ")
            try:
                shutil.rmtree(datePath)
                print("Sucsefully Removed Directory!")
            except:
                print("Issue Encountered")

class viewDirectory:
    def __init__(self, date):
        self.parent_directory = "Data/"

    def viewRange(self, start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)
        # displaying the dates using the functions

    def displayDates(self, start_date, end_date):
        for dt in self.viewRange(start_date, end_date):
            possibleDates = dt.strftime("%Y-%m-%d") #format data
            if possibleDates in os.listdir(self.parent_directory):
                print(possibleDates)





controller = Usercontroller()
programLoop = True
while programLoop:
    controller.mainMenu()

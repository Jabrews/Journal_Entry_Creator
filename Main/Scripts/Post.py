import json
import os
import datetime as dt
from OSFunc import osFunctions

class postManipulation:
    def __init__(self):
        self.os = osFunctions()
        self.title = None
        self.body = None
        self.tags = None
        self.date = dt.date.today()
        self.selectedPost = None
        self.selectedDate = None

    def enterTitle(self):
        userString = str(input("Post Title: "))
        if len(userString) > 0:
            self.title = userString
            print("Updated Title!")
        else:
            print("Invalid Characters")

    def enterBody(self):
        userString = str(input("Post Body: "))
        if len(userString) > 0:
            self.body = userString
            print("Updated Body!")
        else:
            print("Invalid Characters")

    def addTags(self, userTags):
        print(f"Type DONE Once Finished")
        addLoop = True
        while addLoop:
            userTag = str(input("Tag:"))
            if userTag == "DONE":
                return userTags
            elif len(userTag) > 0:
                userTags.append(userTag)
                print(f"Added {userTag}")
            else:
                print("Error has happened")

    def deleteTag(self, userTags):
        print(f"Type DONE Once Finished")
        deleteLoop = True
        while deleteLoop:
            userTag = str(input("Tag: "))
            if userTag in userTags:
                print(f"Sucsefully Deleted {userTag}")
                userTags.remove(userTag)
                print(f"Remaining Tags: | {userTags}")
            elif userTag == "DONE":
                break
            else:
                print("Tag not found!")

    def changeDate(self):
        print("Format: yyyy-mm-dd")
        dateLoop = True
        while dateLoop:
            year = input("Enter year (yyyy): ")
            if len(year) != 4 or not year.isdigit():
                print("Year must be 4 digits.")
                continue
            month = input("Enter month (mm): ")
            if len(month) != 2 or not month.isdigit():
                print("Month must be 2 digits.")
                continue
            day = input("Enter day (dd): ")
            if len(day) != 2 or not day.isdigit():
                print("Day must be 2 digits.")
                continue
            try:
                userDate = dt.date(int(year), int(month), int(day))
                self.date = userDate
                break
            except:
                print("Error has occurred changing date")
                break

    ############Creating File##############

    def checkData(self):
        if self.title == None:
            print("No Title Found")
        elif self.body == None:
            print("No Body Found")
        elif self.tags == None:
            print("No Tags Found")
        else:
            return True

    def formatJson(self):
        jsonFile = {
            "Title": self.title,
            "Body": self.body,
            "Tags": self.tags
        }
        return jsonFile
    def createFile(self):
        dateGood = self.checkData()
        if dateGood == True:
            fileExist = self.os.directoryCheck(str(self.date))
            if fileExist == True:
                print(f"Adding to existing entry")
                data = self.formatJson()
                self.os.addToExisting(self.date, self.title, data)
                print("Sucsefully created entry!")
            elif fileExist == False:
                print("Creating new entry and adding to it")
                data = self.formatJson()
                self.os.addToNew(self.date, self.title, data)
                print("Sucsefully created entry!")
        else:
            print("Make sure all data is entered")

    ############Deleting File###########

    def inputDate(self):
        print("Format: yyyy-mm-dd")
        dateLoop = True
        while dateLoop:
            try:
                year = input("Enter year (yyyy): ")
                if len(year) != 4 or not year.isdigit():
                    print("Year must be 4 digits.")
                    continue
                month = input("Enter month (mm): ")
                if len(month) != 2 or not month.isdigit():
                    print("Month must be 2 digits.")
                    continue
                day = input("Enter day (dd): ")
                if len(day) != 2 or not day.isdigit():
                    print("Day must be 2 digits.")
                    continue
                userDate = dt.date(int(year), int(month), int(day))
                return str(userDate)
            except:
                print("Date not properly formatted")
                break


    def selectDate(self):
        print(os.listdir(self.os.parent_directory))
        userDate = self.inputDate()
        self.selectedDate = userDate

    def selectTitle(self):
        if self.selectedDate == None:
            print("select a date first!")
        else:
            directoryPath = os.path.join(self.os.parent_directory, self.selectedDate)
            try:
                directoryItems = os.listdir(directoryPath)
                userFile = str(input(f"""
                {directoryItems}
                Select File: """))
                self.selectedPost = userFile
            except:
                print("Date not found")

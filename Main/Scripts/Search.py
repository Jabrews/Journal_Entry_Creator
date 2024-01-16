import os.path

from OSFunc import osFunctions
import datetime as dt
from datetime import date, timedelta
import json


class Search:
    def __init__(self):
        self.os = osFunctions()
        self.lowest = None
        self.highest = None
        self.dates_list = []
        self.chosen_dates = []

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
                return userDate
            except:
                print("Date not properly formatted")
                break

    def dateSearch(self, lowest, highest):
        if lowest == None:
            print("Make sure date is chosen")
        elif highest == None:
            print("Make sure date is chosen")
        else:
            self.dates_list = []
            # Generate dates and add to the list
            while lowest <= highest:
                lowest += timedelta(days=1)
                self.dates_list.append(lowest.strftime("%Y-%m-%d"))
            return self.dates_list

    def search(self, lowest, highest):
        self.dates_list = self.dateSearch(lowest, highest)
        self.chosen_dates = self.os.returnDirectory(self.dates_list)
        if len(self.chosen_dates) == 0:
            print("No entries found")
        else:
            for dates in self.chosen_dates:
                dateFile = os.path.join(self.os.parent_directory, dates)
                for files in os.listdir(dateFile):
                    full_file_path = os.path.join(dateFile, files)  # Get the full file path
                    with open(full_file_path, "r") as file:  # Open file with the full path
                        data = json.load(file)
                        self.print_json_data(data)

    def print_json_data(self, data):
        print(f"Title: {data['Title']}")
        print(f"Body: {data['Body']}")
        print(f"Tags: {', '.join(data['Tags'])}\n")



    ##get chosen tags##
    ##open data directory##
    ##check all json files {"tags "}to see if they have any in common with chose
    ##if they do then print that files data##


    def search_addTags(self, userTags):
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

    def search_deleteTags(self, userTags):
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

    def getTags(self, userTags):
        for dateFile in os.listdir(self.os.parent_directory):
            datePaths = os.path.join(self.os.parent_directory, dateFile)
            for dataFile in os.listdir(datePaths):
                dataFilePath = os.path.join(datePaths, dataFile)  # Corrected file path
                try:
                    with open(dataFilePath, "r") as jsonFile:
                        blogEntry = json.load(jsonFile)
                        if any(tag in blogEntry.get("Tags", []) for tag in userTags):
                            print(f"Title: {blogEntry['Title']}")
                            print(f"Body: {blogEntry['Body']}")
                            print(f"Tags: {blogEntry['Tags']}")
                except Exception as e:
                    print(f"Error opening file {dataFilePath}: {e}")

    def getTitle(self):
        userTitle = str(input("Title: "))
        if len(userTitle) == 0:
            print("No characters found")
        else:
            return userTitle

    def search_byTitle(self, userTitle):
        fileName = userTitle + ".json"
        for dateFile in os.listdir(self.os.parent_directory):
            datePaths = os.path.join(self.os.parent_directory, dateFile)
            for dataFile in os.listdir(datePaths):
                if dataFile == fileName:
                    filePath = os.path.join(datePaths, dataFile)
                    try:
                        with open(filePath, "r") as jsonFile:
                            blogEntry = json.load(jsonFile)
                            print(f"Title: {blogEntry['Title']}")
                            print(f"Body: {blogEntry['Body']}")
                            print(f"Tags: {blogEntry['Tags']}")
                    except:
                        print(f"Error opening file {filePath}")
                    break


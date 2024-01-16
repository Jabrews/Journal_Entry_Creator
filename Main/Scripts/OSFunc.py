import json
import os


class osFunctions:
    def __init__(self):
        self.parent_directory = "../Data"

    #def use date to check if directory exist
    #if not then create one and add json to it
    #if so then just add json to it

    def directoryCheck(self, date):
        entryFiles = os.listdir(self.parent_directory)
        if str(date) in entryFiles:
            return True
        else:
            return False

    def addToExisting(self, date, title, json_info):
        filePath_root = os.path.join(self.parent_directory, str(date))
        ##getting file name##
        fileName = title + ".json"
        filePath = os.path.join(filePath_root, fileName)
        with open(filePath, "w") as dataFile:
            json.dump(json_info, dataFile)

    def addToNew(self, date, title, json_info):
        filePath_root = os.path.join(self.parent_directory, str(date))
        os.makedirs(filePath_root)
        ##getting file name##
        fileName = title + ".json"
        filePath = os.path.join(filePath_root, fileName)
        with open(filePath, "w") as dataFile:
            json.dump(json_info, dataFile)

    def deleteFile(self, date, post):
        try:
            directory_rootPath = os.path.join(self.parent_directory, date)
            directoryPath = os.path.join(directory_rootPath, post)
            try:
                os.remove(directoryPath)
                print("Sucsefully Removed File")
            except:
                print("File Not Found")
        except:
            pass


    def returnDirectory(self, datelist):
        chosenDates = []
        for dates in datelist:
            if dates in os.listdir(self.parent_directory):
                chosenDates.append(dates)
        return chosenDates

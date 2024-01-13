import os
import json


###ISSSUES###
#1 not making json file correctly
#2 Unable to open file and get {"tags": [shit]}


class tagManipulation:
    def __init__(self):
        self.parent_directory = "../Data"
        self.chosenTags = []
        self.blockedTags = []


    def addTag_chosen(self):
        tagLoop = True
        while tagLoop:
            print("type DONE once finished")
            userTag = str(input("Add Tag: "))
            if userTag == "DONE":
                break
            elif len(userTag) > 0:
                self.chosenTags.append(userTag)
                print(f"Added: {userTag}")

    def addTag_blocked(self):
        tagLoop = True
        while tagLoop:
            print("type DONE once finished")
            userTag = str(input("Add Tag: "))
            if userTag == "DONE":
                break
            elif len(userTag) > 0:
                self.blockedTags.append(userTag)
                print(f"Added: {userTag}")

    def deleteTag(self):
        deleteLoop = True
        while deleteLoop:
            print("Type DONE once finished")
            userTag = str(input("Delete Tag: "))
            if userTag == "DONE":
                break
            elif userTag in self.chosenTags:
                self.chosenTags.remove(userTag)
            elif userTag in self.blockedTags:
                self.blockedTags.remove(userTag)
            else:
                print("Could not find tag")

    ###################################
    def searchMenu(self):
        searchLoop = True
        while searchLoop:
            userChoice = str(input(f"""
            1. View Post
            2. Back
            User Choice: """))
            if userChoice == "1":
                self.taggedPost()
            elif userChoice == "2":
                break

    def taggedPost(self):
        self.foundTags = 0  # Reset the counter each time the function is called
        for file in os.listdir(self.parent_directory):
            if file.endswith(".json"):  # Check if it's a JSON file
                file_path = os.path.join(self.parent_directory, file)
                with open(file_path, 'r') as selectedJson:
                    blogEntry = json.load(selectedJson)
                    if any(tag in blogEntry.get("Tags", []) for tag in self.chosenTags):
                        print(f"Title: {blogEntry['Title']}")
                        print(f"Body: {blogEntry['Body']}")
                        print(f"Tags: {blogEntry['Tags']}")

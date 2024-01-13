import os.path
import json

class postEntry:
    def __init__(self, title, body, tags):
        self.title = title
        self.body = body
        self.tags = tags

class postManipulation:
    def __init__(self):
        self.title = None
        self.body = None
        self.tags = None
        self.display_post = postEntry(self.title, self.body, self.tags)
        self.parent_directory = "../Data"
        self.deleteTitle = None

    def enterTitle(self):
        userString = str(input("Post Title: "))
        if len(userString) > 0:
            self.display_post.title = userString
            print("Updated Title!")
        else:
            print("Invalid Characters")

    def enterBody(self):
        userString = str(input("Post Body: "))
        if len(userString) > 0:
            self.display_post.body = userString
            print("Updated Body!")
        else:
            print("Invalid Characters")

    ######################TAGS########################
    def enterTags(self):
        userTags = []
        tagLoop = True
        while tagLoop:
            userChoice = str(input(f"""
            Current Tags: {userTags}
            1. Add Tag
            2. Delete Tag
            3. Confirm 
            4. Back
            """))
            if userChoice == "1":
                userTags = self.addTags(userTags)
            elif userChoice == "2":
                userTags = self.deleteTag(userTags)
            elif userChoice == "3":
                self.display_post.tags = userTags
            elif userChoice == "4":
                break

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
                print(f"Remaing Tags: | {userTags}")
            elif userTag == "DONE":
                break
            else:
                print("Tag not found!")

    ######################//TAGS########################
    def createJSON(self):
        blogTitle = self.display_post.title
        blogBody = self.display_post.body
        blogTags = self.display_post.tags
        blogEntry = {
            "Title": blogTitle,
            "Body": blogBody,
            "Tags": blogTags
        }
        fileName = str(blogTitle) + ".json"
        filePath = os.path.join(self.parent_directory, fileName)
        with open(filePath, "w") as jsonFile:
            json.dump(blogEntry, jsonFile)
            print("Sucsefully Created JSON File")

##############Delete Post#################################

    def selectedPost(self):
        directory_listing = os.listdir(self.parent_directory)
        postTitle = str(input("Post Title: ") + ".json")
        for post in directory_listing:
            if postTitle == post:
                print(f"Sucsefully Found {post}")
                self.deleteTitle = postTitle
            else:
                print("Post Not Found")

    def deletePost(self):
        try:
            deletion_path = os.path.join(self.parent_directory, self.deleteTitle)
            os.remove(deletion_path)
            print("Sucsefully Removed Post")
        except:
            print("Issue Encountered")

from Search import Search
from Post import postManipulation
from OSFunc import osFunctions

class userController:
    def __init__(self):
        self.search = Search()
        self.post = postManipulation()
        self.os = osFunctions()

    def mainMenu(self):
        menuLoop = True
        while menuLoop:
            userChoice = str(input("""
            1. Create New Post
            2. Delete Post
            3. View Post(s)
            User Choice: """))
            if userChoice == "1":
                self.createPost()
            elif userChoice == "2":
                self.deleteMenu()
            elif userChoice == "3":
                self.viewPost()

    def createPost(self):
        menuLoop = True
        while menuLoop:
            userChoice = str(input(f"""
            ####Current Post####
            Title: {self.post.title}
            Body: {self.post.body}
            Tags: {self.post.tags}
            *Date: {self.post.date}
            ####################
            1. Enter Title
            2. Enter Body
            3. Enter Tags
            4. Enter Date
            5. Confirm
            6. Back 
            User Choice """))
            if userChoice == "1":
                self.post.enterTitle()
            elif userChoice == "2":
                self.post.enterBody()
            elif userChoice == "3":
                self.tagMenu()
            elif userChoice == "4":
                self.post.changeDate()
            elif userChoice == "5":
                self.post.createFile()
            elif userChoice == "6":
                break
    def tagMenu(self):
        userTags = []
        tagLoop = True
        while tagLoop:
            userChoice = str(input(f"""
                    Current Tags: {userTags}
                    1. Add Tag
                    2. Delete Tag
                    3. Confirm 
                    4. Back
                    User Choice: """))
            if userChoice == "1":
                userTags = self.post.addTags(userTags)
            elif userChoice == "2":
                userTags = self.post.deleteTag(userTags)
            elif userChoice == "3":
                self.post.tags = userTags
                print("Updated Tags")
            elif userChoice == "4":
                break

    def deleteMenu(self):
        menuLoop = True
        while menuLoop:
            userChoice = str(input(f"""
            Selected Date: {self.post.selectedDate}
            Selected Title: {self.post.selectedPost}
            1. Select Date
            2. Select Title
            3. Delete
            4. Back
            User Choice: """))
            if userChoice == "1":
                self.post.selectDate()
            elif userChoice == "2":
                self.post.selectTitle()
            elif userChoice == "3":
                self.os.deleteFile(self.post.selectedDate, self.post.selectedPost)
            elif userChoice == "4":
                break

    def viewPost(self):
        menuLoop = True
        while menuLoop:
            userChoice = str(input("""
            Search Types:
            1. Date Range
            2. Tag Search
            3. Title Search
            4. Back
            User Choice: """))
            if userChoice == "1":
                self.search_dateMenu()
            elif userChoice == "2":
                self.search_tagMenu()
            elif userChoice == "3":
                self.search_titleMenu()
            elif userChoice == "4":
                break

    def search_dateMenu(self):
        menuLoop = True
        while menuLoop:
            userChoice = str(input(f"""
            Date Lowest: {self.search.lowest}
            Date Highest: {self.search.highest}
            1. Enter Date (low)
            2. Enter Date (high)
            3. Initiate Search
            4. Back
            """))
            if userChoice == "1":
                self.search.lowest = self.search.inputDate()
            elif userChoice == "2":
                self.search.highest = self.search.inputDate()
            elif userChoice == "3":
                self.search.search(self.search.lowest, self.search.highest)
            elif userChoice == "4":
                break

    def search_tagMenu(self):
        userTags = []
        tagLoop = True
        while tagLoop:
            userChoice = str(input(f"""
                    Current Tags: {userTags}
                    1. Add Tag
                    2. Delete Tag
                    3. Confirm 
                    4. Back
                    User Choice: """))
            if userChoice == "1":
                userTags = self.search.search_addTags(userTags)
            elif userChoice == "2":
                userTags = self.search.search_deleteTags(userTags)
            elif userChoice == "3":
                self.search.getTags(userTags)
            elif userChoice == "4":
                break

    def search_titleMenu(self):
        userTitle = None
        menuLoop = True
        while menuLoop:
            userChoice = str(input(f"""
            Chosen Title: {userTitle}
            1. Change Title
            2. Confirm
            3. Back
            User Choice: """))
            if userChoice == '1':
                userTitle = self.search.getTitle()
            elif userChoice == "2":
                self.search.search_byTitle(userTitle)
            elif userChoice == "3":
                break

controller = userController()
programLoop = True
while programLoop:
    controller.mainMenu()
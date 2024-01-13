from PostManipulation import postManipulation
from TagManipulation import tagManipulation

class MainController:
    def __init__(self):
        self.post = postManipulation()
        self.tag =  tagManipulation()

    def mainMenu(self):
        menuLoop = True
        while menuLoop:
            userChoice = str(input("""
            1. Create Post
            2. Delete Post
            3. Tag Search
            User Choice: """))
            if userChoice == "1":
                self.createMenu()
            elif userChoice == "2":
                self.deleteMenu()
            elif userChoice == "3":
                self.tagMenu()

    def createMenu(self):
        menuLoop = True
        while menuLoop:
            userChoice = str(input(f"""
            #####################
            Title : {self.post.display_post.title}
            Body : {self.post.display_post.body}
            Tags : {self.post.display_post.tags}
            #####################
            1. Enter Title
            2. Enter Body
            3. Enter Tags
            4. Create Post
            5. Back
            User Choice: """))
            if userChoice == "1":
                self.post.enterTitle()
            elif userChoice == "2":
                self.post.enterBody()
            elif userChoice == "3":
                self.post.enterTags()
            elif userChoice == "4":
                self.post.createJSON()
            elif userChoice == "5":
                break

    def deleteMenu(self):
        deleteLoop = True
        while deleteLoop:
            userChoice = str(input(f"""
            Selected Post: {self.post.deleteTitle}
            1. Post Title
            2. Delete
            3. Back
            User Choice: """))
            if userChoice == "1":
                self.post.selectedPost()
            elif userChoice == "2":
                self.post.deletePost()
            elif userChoice == "3":
                break

    def tagMenu(self):
        tagLoop = True
        while tagLoop:
            userChoice = str(input(f"""
            Chosen Tags: {self.tag.chosenTags}
            Blocked Tags: {self.tag.blockedTags}
            1. Add Chosen Tag 
            2. Add Blocked Tag
            3. Delete Tag
            4. Initiate Search Menu*
            5. Back
            User Choice: """))
            if userChoice == "1":
                self.tag.addTag_chosen()
            elif userChoice == "2":
                self.tag.addTag_blocked()
            elif userChoice == "3":
                self.tag.deleteTag()
            elif userChoice == "4":
                self.tag.searchMenu()
            elif userChoice == "5":
                break


controller = MainController()
programLoop = True
while programLoop:
    controller.mainMenu()

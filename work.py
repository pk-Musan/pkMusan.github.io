class Work:
    def __init__(self, id, name, image="", description="", date="", github="", url=""):
        self.id = id
        self.name = name
        self.image = "images/" + image
        self.description = description
        self.date = date
        self.github = github
        self.url = url
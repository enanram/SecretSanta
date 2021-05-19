class Participant:
    
    def __init__(self, name, email = "", exclude = []):
        self.name = name
        if email == "":
            self.email = email
        else:
            self.email = "{}@email.com".format(self.name)
        self.exclude = exclude
    

    def __str__(self):
        returnString = "Name: {}\nemail: {}\nExclude:\n".format(self.name, self.email)
        if len(self.exclude) == 0:
            returnString += "\tNone"
        else:
            for item in self.exclude:
                returnString += "\t" + item
        return returnString

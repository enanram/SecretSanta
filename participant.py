class Participant:
    
    def __init__(self, name, email, exclude):
        self.name = name
        self.email = email
        
        if exclude:
            self.exclude = exclude
        else:
            self.exclude = []
        
        self.match = None
    

    @property
    def nameWithMatch(self):
        stringOut = self.name
        if self.match:
            stringOut += " buys for {}".format(self.match.name)
        else:
            stringOut += " (no match)"
        return stringOut



    def __str__(self):
        returnString = "Name: {}\nemail: {}\nExclude:\n".format(self.name, self.email)
        if len(self.exclude) == 0:
            returnString += "\tNone"
        elif self.exclude:
            for item in self.exclude:
                returnString += "\t" + item + "\n"
        else:
            returnString += "None\n"
        return returnString

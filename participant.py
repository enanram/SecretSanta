import functools


class Participant:
    
    def __init__(self, name, email, exclude):
        self.name = name
        self.email = email
        
        if exclude:
            self.exclude = exclude
        else:
            self.exclude = []
        
        self.giftee = None
    

    @property
    def nameWithMatch(self):
        stringOut = self.name
        if self.giftee:
            stringOut += " buys for {}".format(self.giftee.name)
        else:
            stringOut += " (no match)"
        return stringOut


    '''
    Converts the list of names in self.exclude to a list of Participant objects
    '''
    def convertExcludeToObjects(self, participants):
        if not self.exclude:
            pass
        else:
            for i in range(len(self.exclude)):
                nameString = self.exclude[i].strip().lower()
                
                for part in participants:
                    objectName = part.name.strip().lower()
                    if objectName == nameString:
                        self.exclude[i] = part
                        break

                


    def __str__(self):
        returnString = "Name: {}\nemail: {}\nExclude:\n".format(self.name, self.email)
        if len(self.exclude) == 0:
            returnString += "\tNone"
        elif self.exclude:
            for item in self.exclude:
                if isinstance(item, str):
                    returnString += "\t" + item + "\n"
                else:
                    returnString += "\t" + item.name + "\n"
        else:
            returnString += "None\n"
        return returnString


    '''
    The following methods allow objects to be sorted by the number of exceptions.
    '''
    def __lt__(self, other):
        return len(self.exclude) < len(other.exclude)

    def __gt__(self, other):
        return len(self.exclude) > len(other.exclude)
    
    def __eq__(self, other):
        return len(self.exclude) == len(other.exclude)

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)
    
    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

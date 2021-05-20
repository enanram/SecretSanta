################################################################
######################### SECRET SANTA #########################
################################################################
# A script that matches members of a group to each other while #
# avoiding matching pairs who have matched in the past.        #
################################################################
###################### by Donagh Marnane #######################



from participant import Participant
import random
import csv

'''
A new session is initiated when a .csv file is opened. This will check
for users who have exceptions. If no exceptions are found the simple
matcher can be run.
'''
class Session:
    def __init__(self):
        self.exclusions = False

'''
This method opens the .csv file and returns a list of Participant objects from the contents.
'''
def importCsvFile(session):
    with open("participants.csv", 'r') as csvFile:
        csvLines = csv.reader(csvFile)
        
        # Skip the first line, which contains titles
        next(csvLines)
        
        participants = []

        for line in csvLines:
            if len(line) > 2:
                session.exclusions = True
            # Create Participant object for each line in the csv and add to the list
            name = line[0]
            email = line[1]
            exclude = [line[i] for i in range(2, len(line))]
            participants.append(Participant(name, email, exclude))

        
        # for item in participants:
        #     print(item)
        
        # The returned list is sorted by how many exclusions it has
        participants.sort(reverse=True)
        return participants


def stripAndLower(inputString):
    return inputString.strip().lower()

'''
Matching algorithm that does not take exclusions into account.
Randomises the order of particpants by creating a separate list of
indices, randomising it, copying it, and shifting the copy over by 1.
'''
def simpleMatcher(participants):
    participantCount = len(participants)
    givers = list(range(participantCount))
    random.shuffle(givers)
    receivers = givers.copy()
    receivers.insert(0, receivers.pop())

    for i in range(participantCount):
        participants[givers[i]].match = participants[receivers[i]]
    
    for part in participants:
        print(part.nameWithMatch)




'''
Matching algorithm that takes exclusions into account.
'''
def complexMatcher(participants):
    pass




def main():
    session = Session()
    participants = importCsvFile(session)
    if session.exclusions:
        complexMatcher(participants)
    else:
        simpleMatcher(participants)



if __name__ == "__main__":
    main()
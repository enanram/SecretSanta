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
        
        participants = []

        for line in csvLines:
            if line[0] in {"name", "Name", "NAME"}:
                continue
            if len(line) > 2:
                session.exclusions = True
            # Create Participant object for each line in the csv and add to the list
            name = line[0]
            email = line[1]
            exclude = [line[i] for i in range(2, len(line))]
            participants.append(Participant(name, email, exclude))

        # initialise each participant's domain as all other participants
        for part in participants:
            part.domain = participants.copy()
            part.removeSelf()
        
        # for item in participants:
        #     print(item)
        
        # The returned list is sorted by how many exclusions it has
        participants.sort(reverse=True)
        return participants



def addAnyone(participants, giftees):
    numRemaining = len(participants)
            
    # add a unique participant to giftees
    while True:
        randomIndex = random.randrange(numRemaining)
        if participants[randomIndex] in giftees:
            continue
        else:
            giftees.append(participants[randomIndex])
            break



'''
Matching algorithm that does not take exclusions into account.
Randomises the order of particpants by randomising the list, 
copying it, and shifting the copy over by 1.
'''
def simpleMatcher(participants):
    participantCount = len(participants)
    givers = participants.copy()
    random.shuffle(givers)
    receivers = givers.copy()
    receivers.insert(0, receivers.pop())

    for i in range(participantCount):
        givers[i].giftee = receivers[i]
    
    for part in participants:
        print(part.nameWithMatch)




'''
Matching algorithm that takes exclusions into account. 
Not yet tested - may need tweaking.
'''
def complexMatcher(participants):
    giftees = []
    for index, part in enumerate(participants):
        part.cullDomain()
        if part.domain:            
            for participant in part.domain:
                if participant not in giftees:
                    giftees.append(participant)
                    break
        elif len(giftees) != index + 1 or not part.domain:
            numRemaining = len(participants)
            # add a unique participant to giftees
            while True:
                randomIndex = random.randrange(numRemaining)
                if participants[randomIndex] in giftees:
                    continue
                else:
                    giftees.append(participants[randomIndex])
                    break



def main():
    session = Session()
    participants = importCsvFile(session)
    if session.exclusions:
        complexMatcher(participants)
    else:
        simpleMatcher(participants)



if __name__ == "__main__":
    main()
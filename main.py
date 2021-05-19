from participant import Participant
import random
import csv

def importCsvFile():
    with open("participants.csv", 'r') as csvFile:
        csvLines = csv.reader(csvFile)
        
        next(csvLines)
        
        participants = []

        for line in csvLines:
            name = line[0]
            email = line[1]
            exclude = [line[i] for i in range(2, len(line))]
            participants.append(Participant(name, email, exclude))
            
            # for item in line:
            #     print(item)   
        
        for item in participants:
            print(item)




def main():
    importCsvFile()





if __name__ == "__main__":
    main()
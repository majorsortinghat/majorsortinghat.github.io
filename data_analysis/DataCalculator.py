import json
import math


with open("Major_Mapping_Survey_2.json", "r") as read_file:
    data = json.load(read_file)

counter = 0

majors ={}
correctionVar = -3 #Used to normalize from a scale of 1:5 to -2:2. Why -2:2 and not -1:1? Because




def checkTrait(trait):
    if trait != 'NumberOfPeople' and trait != "Clubs" and trait != "Major_2" and trait != "Major_1" and trait != 'Graduation' and trait != 'Satisfaction':  # Ignore what's not useful/easy
        return True
    else:
        return False


def weightCalc(person):
    return (float(
        person['Satisfaction']) - 4) / 2;  # Weight each answer in accordance to how much they like the major.


def addTraitToMajor():
    return

def addCountToMajor(person, major):
    if (person[major] == ""):
        return
    if(str(person[major]) not in majors):
        majors[str(person[major])] = {}
        majors[str(person[major])]['NumberOfPeople'] = 1
    else:
        majors[str(person[major])]['NumberOfPeople'] += 1















def iterateThroughData():
    for person in data:
        continue


def checkifEmptyString(person):
    return person[trait] == "" or person[trait] == "N/A"

for person in data:

    if str(person['Major_1']) not in majors and person['Major_1'] != 'Undeclared': #If the major isn't already in the dict.


        #weight = (float(person['Satisfaction']) - 4) / 2; #Weight each answer in accordance to how much they like the major.
        weight = weightCalc(person)
        #print (weight)

        print()
        print(person['Major_1'])
        print(person['Major_2'])
        print(person['Satisfaction'])
        print(person['Like_Parties'])


        majors[str(person['Major_1'])] = {}
        majors[str(person['Major_1'])]['NumberOfPeople'] = 1

        addCountToMajor(person, 'Major_2')

        """if str(person['Major_2']) not in majors and str(person['Major_2']) != "":
            majors[str(person['Major_2'])] = {}
            majors[str(person['Major_2'])]['NumberOfPeople'] = 1
        elif str(person['Major_2']) != "":
            majors[str(person['Major_2'])]['NumberOfPeople'] += 1"""

        for trait in person:
            if checkTrait(trait):
                if checkifEmptyString(person):
                    majors[str(person['Major_1'])][trait] = 0
                    if str(person['Major_2']) != "":
                        majors[str(person['Major_2'])][trait] = 0
                else:
                    majors[str(person['Major_1'])][trait] = (float(person[trait])+correctionVar)*weight
                    if str(person['Major_2']) != "":
                        majors[str(person['Major_2'])][trait] = (float(person[trait]) + correctionVar) * weight

        #print(majors[str(person['Major_1'])])

    elif person['Major_1'] != 'Undeclared': #The major is in the dict, so this is where the data is updated

        #weight = (float(person['Satisfaction']) - 4) / 2;
        weight = weightCalc(person)
        majors[str(person['Major_1'])]['NumberOfPeople'] += 1

        if str(person['Major_2']) not in majors and str(person['Major_2']) != "":
            majors[str(person['Major_2'])] = {}
            majors[str(person['Major_2'])]['NumberOfPeople'] = 1
            for trait in person:
                if checkTrait(trait):
                    if checkifEmptyString(person):
                        majors[str(person['Major_2'])][trait] = 0
                    else:
                        majors[str(person['Major_2'])][trait] = (float(person[trait]) + correctionVar) * weight

        elif str(person['Major_2']) != "":
            majors[str(person['Major_2'])]['NumberOfPeople'] += 1

        for trait in majors[str(person['Major_1'])].keys():
            if checkTrait(trait):
                if not checkifEmptyString(person):
                    majors[str(person['Major_1'])][trait] += (person[trait]+correctionVar)*weight
                    if str(person['Major_2']) != "":
                        majors[str(person['Major_2'])][trait] += (person[trait] + correctionVar) * weight

        #print('Number of people in '+ str(person['Major_1'])+': ' + str(majors[str(person['Major_1'])]['NumberOfPeople']))
        #majors[person['Major_1']]['Satisfaction'] += float(person['Major_1']['Satisfaction'])


for major in majors.keys():

    print()
    print('Major: ' + major)

    for trait in majors[major].keys():
        if trait != 'NumberOfPeople':
            tempVariance = 0
            majors[major][trait] = majors[major][trait]/majors[major]['NumberOfPeople'] #Convert from sum of traits to avarage of traits
            for person in data:

                if (str(person['Major_1']) == major or str(person['Major_2']) == major) and person['Major_1'] != 'Undeclared' and person[trait] != "" and person[trait] != "N/A": #important to convert Major to string, as some are numbers
                    weight = (float(person[
                                        'Satisfaction']) - 4) / 2;  # Weight each answer in accordance to how much they like the major.
                    #print("Person trait. "+str(((person[trait])+correctionVar)*weight)+ " Majors Major trait: "+str(majors[major][trait]))
                    tempVariance += (((person[trait]+correctionVar)*weight-majors[major][trait])**2)
                    #print(tempVariance)
            tempVariance = tempVariance/majors[major]['NumberOfPeople'] #Calculate actual variance from the sum of individual deltas
            majors[major][trait] = {"Mean": majors[major][trait], "SD": math.sqrt(tempVariance)}

        print(trait + ': ' + str(majors[major][trait]))

    #print('The scales go from -3 to 3, with -3 being "hate it" and 3 being "love it".')

with open('outdata.json', 'w') as outfile:
    json.dump(majors, outfile, indent=4, sort_keys=True)
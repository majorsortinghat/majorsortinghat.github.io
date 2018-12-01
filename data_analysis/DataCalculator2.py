import json
import copy
import statistics
import math


with open("Major_Mapping_Survey_2.json", "r") as read_file:
    data = json.load(read_file)

majors = {}

meanSDMajors = {}

def addMajorsAndCount():
    for person in data:
        major1 = str(person['Major_1'])
        major2 = str(person['Major_2'])
        addMajor(major1)
        addMajor(major2)
        countMajor(major1)
        countMajor(major2)
    traitdict = {}
    for trait in data[0]:
        if checkTrait(trait):
            traitdict[trait] = []
    for major in majors:
        majors[major] = copy.deepcopy(traitdict)

def addMajor(major):
    if major not in majors and major != "" and major != "Undeclared":
        majors[major] = {'count': 0}


def countMajor(major):
    if major != "" and major != "Undeclared":
        majors[major]['count'] += 1

def checkTrait(trait):
    if trait != 'NumberOfPeople' and trait != "Clubs" and trait != "Major_2" and trait != "Major_1" and trait != 'Graduation' and trait != 'Satisfaction':  # Ignore what's not useful/easy
        return True
    else:
        return False

def checkValue(value):
    return value != "" and value != "N/A"


def addSingleTrait():
    return

def weightCalc(person):
    return (float(
        person['Satisfaction']) - 4) / 2;  # Weight each answer in accordance to how much they like the major.

def addTraits():
    for major in majors:
        #major_people = [person for person in data if major == str(person['Major_1']) or major == str(person['Major_2'])]
        for person in data:
            if major == str(person['Major_1']) or major == str(person['Major_2']):
                weight = weightCalc(person)
                for trait in person:
                    if checkTrait(trait) and checkValue(person[trait]):

                        majors[major][trait].append((float(person[trait])-3)*weight)
                        #majors[major][trait][1] += 1


addMajorsAndCount()
addTraits()
print(majors)


def calculateSD():
    for major in majors:
        meanSDMajors[major] = {}
        for trait in majors[major]:
            sd = 0.00001
            if (len(majors[major][trait]) > 1):
                sd = statistics.stdev(majors[major][trait])
            print(len(majors[major][trait]))
            if(len(majors[major][trait]) > 0):
                if (sd == 0):
                    sd = 0.0001
                meanSDMajors[major][trait] = {'Mean': sum(majors[major][trait])/len(majors[major][trait]), 'SD': sd}


calculateSD()

print(meanSDMajors)

with open('outdata.json', 'w') as outfile:
    json.dump(meanSDMajors, outfile, indent=4, sort_keys=True)

def addCountToMajor(person, major):
    if (person[major] == ""):
        return
    if(str(person[major]) not in majors):
        majors[str(person[major])] = {}
        majors[str(person[major])]['NumberOfPeople'] = 1
    else:
        majors[str(person[major])]['NumberOfPeople'] += 1
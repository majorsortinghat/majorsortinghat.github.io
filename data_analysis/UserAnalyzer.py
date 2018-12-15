import json
import math
import sklearn.tree
import sklearn.ensemble
import sklearn.linear_model
import numpy as np
import pickle
import matplotlib.pyplot as plt

keys = ["Satisfaction",
    "Like_Parties",
    "Like_HangingOut",
    "Like_Hiking",
    "Like_BoardGames",
    "Like_VideoGames",
    "Like_WatchingTV",
    "Like_WatchingMovies",
    "Like_IndividualSports",
    "Like_TeamSports",
    "Like_ReadingBook",
    "PowerOfVulnerability",
    "FakeVideosOfRealPeople",
    "PharmacyOfTheFuture",
    "HowGreatLeadersInspireGreatAction",
    "LetMyDatasetChangeYourMindset",
    "MagicIngredientBringsLifeToPixar",
    "PowerOfIntroverts",
    "WhatGardeningToldMeAboutLife",
    "WhatIfGentrificationWasAboutHealing",
    "HighSchool_Math",
    "HighSchool_Physics",
    "HighSchool_Chemistry",
    "HighSchool_Bio",
    "HighSchool_English",
    "HighSchool_History",
    "HighSchool_Music",
    "HighSchool_Art",
    "HighSchool_Leader",
    "HighSchool_Engineering",
    "Rank_Understand",
    "Rank_FullOfIdeas",
    "Rank_Imagination",
    "Rank_DifficultyUnderstandingAbstract",
    "Rank_AlwaysPrepared",
    "Rank_AttentionToDetails",
    "Rank_GetChoresDoneRightAway",
    "Rank_ForgetToPutThingsBack",
    "Rank_StartConversations",
    "Rank_TalkToDifferentPeopleAtParties",
    "Rank_ThinkALotBeforeSpeaking",
    "Rank_DislikeGettingAttention",
    "Rank_QuietAroundStrangers",
    "Rank_SoftHeart",
    "Rank_TakeTimeOutForOthers",
    "Rank_MakePeopleFeelAtEase",
    "Rank_NotInterestedInOthersProblems",
    "Rank_FeelLittleConcernForOthers",
    "Rank_GetIrritatedEasily",
    "Rank_HaveFrequentMoodSwings",
    "Rank_WorryAboutThings",
    "Rank_RelaxedMostOfTheTime",
    "Rank_SeldomFeelBlue"]

with open("outdata.json", "r") as read_file:
    data = json.load(read_file)

def loadRaw(rawDataFile):
    with open(rawDataFile, "r") as read_file:
        rawData = json.load(read_file)

        alldataarr = []
        alllabelsarr = []

        for person in rawData:
            if person["Major_1"] != "Undeclared":
                alllabelsarr.append(person["Major_1"])
                add_data = {}
                for key in keys:
                    if key in person:
                        if person[key] != 'N/A' and person[key] != "":
                            add_data[key] = (int(person[key]))
                        else:
                            add_data[key] = -1
                    else:
                        add_data[key] = -1
                alldataarr.append(add_data)

                if person["Major_2"] != "":
                    alllabelsarr.append(person["Major_2"])
                    alldataarr.append(add_data)

        alldata = np.array(alldataarr)
        alllabels = np.array(alllabelsarr)
    return alldata, alllabels
        #traindata=np.array(alldataarr[:int(len(alldataarr)*.9)])
        #trainlabels=np.array(alllabelsarr[:int(len(alllabelsarr)*.9)])
        #testdata=np.array(alldataarr[int(len(alldataarr)*.9):])
        #testlabels=np.array(alllabelsarr[int(len(alllabelsarr)*.9):])

def compareValues(userInput):
    #print("userInput: "+str(userInput))
    resultScores = {}
    length = len(userInput)
    for major in data:
        tempScore = 0;
        i = 0
        #print(major)
        for trait in userInput:
            if trait in data[str(major)]:
                #print(trait)
                #print(userInput[trait])
                #print(str(major))
                #print(data[str(major)])
                #print(data[str(major)][trait]['Mean'])
                i += 1
                tempScore += ((float(userInput[trait])-3-data[str(major)][trait]['Mean'])**2/(data[str(major)][trait]['SD']))**2
        #print(tempScore)
        resultScores[major] = math.sqrt(tempScore)/i * length;

    #print()
    invDict = invertDict(resultScores)
    #print(invDict)
    #print(dictToSortedList(invDict))

    #for i in dictToSortedList(invDict):
        #print(str(invDict[i]) +": "+ str(i))

    return invDict


def invertDict(d):
    newDict = {}
    for i in d.keys():
        newDict[d[i]] = i;
    return newDict

def dictToSortedList(d):
    mylist = list(d.keys())
    return (sorted(mylist))



def getInput():
    unprocessedInput = {}

    unprocessedInput["Like_Parties"] = input("Rate on a scale from 1-5 how much you like parties: ")

    unprocessedInput["Like_HangingOut"] = input("Rate on a scale from 1-5 how much you like Hanging out with friends: ")
    unprocessedInput["Like_Hiking"] = input("Rate on a scale from 1-5 how much you like Hiking: ")
    unprocessedInput["Like_BoardGames"] = input("Rate on a scale from 1-5 how much you like Board Games: ")
    unprocessedInput["Like_VideoGames"] = input("Rate on a scale from 1-5 how much you like Video Games: ")
    unprocessedInput["Like_WatchingTV"] = input("Rate on a scale from 1-5 how much you like watching TV: ")
    unprocessedInput["Like_WatchingMovies"] = input("Rate on a scale from 1-5 how much you like watching movies: ")
    unprocessedInput["Like_IndividualSports"] = input("Rate on a scale from 1-5 how much you like individual sports: ")
    unprocessedInput["Like_TeamSports"] = input("Rate on a scale from 1-5 how much you like team sports: ")
    unprocessedInput["Like_ReadingBook"] = input("Rate on a scale from 1-5 how much you like Reading a book: ")

    unprocessedInput["PowerOfVulnerability"] = input("Rank on a scale from 1-5 how much you would like to watch the talk PowerOfVulnerability: ")
    unprocessedInput["FakeVideosOfRealPeople"] = input(
        "Rank on a scale from 1-5 how much you would like to watch the talk FakeVideosOfRealPeople: ")
    unprocessedInput["PharmacyOfTheFuture"] = input(
        "Rank on a scale from 1-5 how much you would like to watch the talk PharmacyOfTheFuture: ")
    unprocessedInput["HowGreatLeadersInspireGreatAction"] = input(
        "Rank on a scale from 1-5 how much you would like to watch the talk HowGreatLeadersInspireGreatAction: ")
    unprocessedInput["LetMyDatasetChangeYourMindset"] = input(
        "Rank on a scale from 1-5 how much you would like to watch the talk LetMyDatasetChangeYourMindset: ")
    unprocessedInput["MagicIngredientBringsLifeToPixar"] = input(
        "Rank on a scale from 1-5 how much you would like to watch the talk MagicIngredientBringsLifeToPixar: ")
    unprocessedInput["PowerOfIntroverts"] = input(
        "Rank on a scale from 1-5 how much you would like to watch the talk PowerOfIntroverts: ")
    unprocessedInput["WhatGardeningToldMeAboutLife"] = input(
        "Rank on a scale from 1-5 how much you would like to watch the talk WhatGardeningToldMeAboutLife: ")
    unprocessedInput["WhatIfGentrificationWasAboutHealing"] = input(
        "Rank on a scale from 1-5 how much you would like to watch the talk WhatIfGentrificationWasAboutHealing: ")

    return unprocessedInput


def fake6_2Input():
    data = {
    "Like_Parties": 1,
    "Like_HangingOut": 5,
    "Like_Hiking": 1,
    "Like_BoardGames": 2,
    "Like_VideoGames": 1,
    "Like_WatchingTV": 5,
    "Like_WatchingMovies": 5,
    "Like_IndividualSports": 1,
    "Like_TeamSports": 1,
    "Like_ReadingBook": 4,
    "PowerOfVulnerability": 4,
    "FakeVideosOfRealPeople": 1,
    "PharmacyOfTheFuture": 2,
    "HowGreatLeadersInspireGreatAction": 1,
    "LetMyDatasetChangeYourMindset": 2,
    "MagicIngredientBringsLifeToPixar": 5,
    "PowerOfIntroverts": 5,
    "WhatGardeningToldMeAboutLife": 1,
    "WhatIfGentrificationWasAboutHealing": 1,
    "HighSchool_Math": 4,
    "HighSchool_Physics": 3,
    "HighSchool_Chemistry": 4,
    "HighSchool_Bio": 1,
    "HighSchool_English": 2,
    "HighSchool_History": 1,
    "HighSchool_Music": 5,
    "HighSchool_Art": 5,
    "HighSchool_Leader": 3,
    "HighSchool_Engineering": 3,
    """
    "Now_Math": 1,
    "Now_Physics": 1,
    "Now_Chemistry": 4,
    "Now_Bio": 2,
    "Now_English": 4,
    "Now_History": 1,
    "Now_Music": 5,
    "Now_Art": 5,
    "Now_Leader": 3,
    "Now_Engineering": 3,
    """
    "Rank_Understand": 4,
    "Rank_FullOfIdeas": 5,
    "Rank_Imagination": 5,
    "Rank_DifficultyUnderstandingAbstract": 1,
    "Rank_AlwaysPrepared": 4,
    "Rank_AttentionToDetails": 4,
    "Rank_GetChoresDoneRightAway": 1,
    "Rank_ForgetToPutThingsBack": 4,
    "Rank_StartConversations": 1,
    "Rank_TalkToDifferentPeopleAtParties": 1,
    "Rank_ThinkALotBeforeSpeaking": 4,
    "Rank_DislikeGettingAttention": 5,
    "Rank_QuietAroundStrangers": 5,
    "Rank_SoftHeart": 5,
    "Rank_TakeTimeOutForOthers": 2,
    "Rank_MakePeopleFeelAtEase": 4,
    "Rank_NotInterestedInOthersProblems": 2,
    "Rank_FeelLittleConcernForOthers": 2,
    "Rank_GetIrritatedEasily": 2,
    "Rank_HaveFrequentMoodSwings": 2,
    "Rank_WorryAboutThings": 5,
    "Rank_RelaxedMostOfTheTime": 2,
    "Rank_SeldomFeelBlue": 2
  }
    return data


def fake12Input():
    data = {
        "Like_Parties": 4,
        "Like_HangingOut": 5,
        "Like_Hiking": 5,
        "Like_BoardGames": 3,
        "Like_VideoGames": 1,
        "Like_WatchingTV": 2,
        "Like_WatchingMovies": 3,
        "Like_IndividualSports": 2,
        "Like_TeamSports": 3,
        "Like_ReadingBook": 4,
        "PowerOfVulnerability": 2,
        "FakeVideosOfRealPeople": 3,
        "PharmacyOfTheFuture": 3,
        "HowGreatLeadersInspireGreatAction": 2,
        "LetMyDatasetChangeYourMindset": 3,
        "MagicIngredientBringsLifeToPixar": 3,
        "PowerOfIntroverts": 3,
        "WhatGardeningToldMeAboutLife": 4,
        "WhatIfGentrificationWasAboutHealing": 4,
        "HighSchool_Math": 4,
        "HighSchool_Physics": 4,
        "HighSchool_Chemistry": 5,
        "HighSchool_Bio": 5,
        "HighSchool_English": 3,
        "HighSchool_History": 2,
        "HighSchool_Music": 5,
        "HighSchool_Art": 4,
        """
        "Now_Math": 4,
        "Now_Physics": 4,
        "Now_Chemistry": 4,
        "Now_Bio": 4,
        "Now_English": 4,
        "Now_History": 3,
        "Now_Music": 5,
        "Now_Art": 4,
        """
        "Rank_Understand": 4,
        "Rank_FullOfIdeas": 3,
        "Rank_Imagination": 4,
        "Rank_DifficultyUnderstandingAbstract": 3,
        "Rank_AlwaysPrepared": 2,
        "Rank_AttentionToDetails": 5,
        "Rank_GetChoresDoneRightAway": 3,
        "Rank_ForgetToPutThingsBack": 3,
        "Rank_StartConversations": 2,
        "Rank_TalkToDifferentPeopleAtParties": 3,
        "Rank_ThinkALotBeforeSpeaking": 5,
        "Rank_DislikeGettingAttention": 4,
        "Rank_QuietAroundStrangers": 5,
        "Rank_SoftHeart": 4,
        "Rank_TakeTimeOutForOthers": 4,
        "Rank_MakePeopleFeelAtEase": 4,
        "Rank_NotInterestedInOthersProblems": 1,
        "Rank_FeelLittleConcernForOthers": 1,
        "Rank_GetIrritatedEasily": 1,
        "Rank_HaveFrequentMoodSwings": 2,
        "Rank_WorryAboutThings": 5,
        "Rank_RelaxedMostOfTheTime": 3,
        "Rank_SeldomFeelBlue": 3
    }
    return data


def fake2AInput():
    data = {
        "Like_Parties": 5,
        "Like_HangingOut": 5,
        "Like_Hiking": 3,
        "Like_BoardGames": 2,
        "Like_VideoGames": 3,
        "Like_WatchingTV": 2,
        "Like_WatchingMovies": 4,
        "Like_IndividualSports": 4,
        "Like_TeamSports": 5,
        "Like_ReadingBook": 3,
        "PowerOfVulnerability": 2,
        "FakeVideosOfRealPeople": 2,
        "PharmacyOfTheFuture": 3,
        "HowGreatLeadersInspireGreatAction": 5,
        "LetMyDatasetChangeYourMindset": 3,
        "MagicIngredientBringsLifeToPixar": 5,
        "PowerOfIntroverts": 3,
        "WhatGardeningToldMeAboutLife": 1,
        "WhatIfGentrificationWasAboutHealing": 1,
        "HighSchool_Math": 4,
        "HighSchool_Physics": 4,
        "HighSchool_Chemistry": 2,
        "HighSchool_Bio": 3,
        "HighSchool_English": 3,
        "HighSchool_History": 3,
        "HighSchool_Music": 5,
        "HighSchool_Art": 5,
        """
        "Now_Math": 4,
        "Now_Physics": 4,
        "Now_Chemistry": 1,
        "Now_Bio": 3,
        "Now_English": 3,
        "Now_History": 3,
        "Now_Music": 5,
        "Now_Art": 5,
        "Now_Engineering": 4,
        """
        "Rank_Understand": 3,
        "Rank_FullOfIdeas": 4,
        "Rank_Imagination": 4,
        "Rank_DifficultyUnderstandingAbstract": 3,
        "Rank_AlwaysPrepared": 4,
        "Rank_AttentionToDetails": 4,
        "Rank_GetChoresDoneRightAway": 2,
        "Rank_ForgetToPutThingsBack": 4,
        "Rank_StartConversations": 4,
        "Rank_TalkToDifferentPeopleAtParties": 4,
        "Rank_ThinkALotBeforeSpeaking": 4,
        "Rank_DislikeGettingAttention": 3,
        "Rank_QuietAroundStrangers": 4,
        "Rank_SoftHeart": 3,
        "Rank_TakeTimeOutForOthers": 4,
        "Rank_MakePeopleFeelAtEase": 5,
        "Rank_NotInterestedInOthersProblems": 2,
        "Rank_FeelLittleConcernForOthers": 2,
        "Rank_GetIrritatedEasily": 4,
        "Rank_HaveFrequentMoodSwings": 5,
        "Rank_WorryAboutThings": 5,
        "Rank_RelaxedMostOfTheTime": 1,
        "Rank_SeldomFeelBlue": 1
    }
    return data

def processInput(unprocessedInput):
    processedOutput = {}
    for i in unprocessedInput.keys():
        processedOutput[i] = float(unprocessedInput[i])-3
    return processedOutput

dt6_2Input = np.array([7, 1, 5, 1, 2, 1, 5, 5, 1, 1, 4, 4, 1, 2, 1, 2, 5, 5, 1, 1, 4, 3, 4, 1, 2, 1, 5, 5, 3, 3,
    4, 5, 5, 1, 4, 4, 1, 4, 1, 1, 4, 5, 5, 5, 2, 4, 2, 2, 2, 2, 5, 2, 2])


values, labels = loadRaw('Major_Mapping_Survey_2.json')
#print(values)
#dtree = sklearn.tree.DecisionTreeClassifier()
#dtree = dtree.fit(values, labels)

total = 0
correct = 0
for i in range(len(values)):
    
    total += 1
    results = compareValues(processInput(values[i]))
    if labels[i] == results[min(results.keys())]:
        correct += 1

print(correct/total)
        

'''
forest = sklearn.ensemble.RandomForestClassifier(n_estimators = 50)
forest = forest.fit(values, labels)

linear = sklearn.linear_model.SGDClassifier(loss = 'modified_huber', alpha = .1, max_iter=100, tol=1e-3)
linear = linear.fit(values, labels)
'''
filename = 'linear.sav'
pickling_on = open(filename, "rb")
linear = pickle.load(pickling_on)
pickling_on.close()
'''
#print("DTREE 6-2: ", dtree.predict(dt6_2Input.reshape(1,-1)))
#print("DTREE score: ", dtree.score(values, labels))
print("FOREST 6-2: ", forest.predict(dt6_2Input.reshape(1,-1)))
print("FOREST 6-2 prob: ", forest.predict_proba(dt6_2Input.reshape(1,-1)))
print("FOREST score: ", forest.score(values, labels))
i_62 = list(forest.classes_).index('6-2')
i_63 = list(forest.classes_).index('6-3')
i_2 = list(forest.classes_).index('2')
print("LINEAR 6-2: ", linear.predict(dt6_2Input.reshape(1,-1)))
print("LINEAR 6-2 prob: ", linear.predict_proba(dt6_2Input.reshape(1,-1)))
print("LINEAR 6-2 dfn: ", linear.decision_function(dt6_2Input.reshape(1,-1)))
print("LINEAR score: ", linear.score(values, labels))
'''
col = keys

#modelname.feature_importance_
y = linear.feature_importances_
#plot
fig, ax = plt.subplots() 
width = 0.4 # the width of the bars 
ind = np.arange(len(y)) # the x locations for the groups
ax.barh(ind, y, width, color="green")
ax.set_yticks(ind+width/10)
ax.set_yticklabels(col, minor=False)
plt.title('Feature importance in RandomForest Classifier')
plt.xlabel('Relative importance')
plt.ylabel('feature') 
plt.figure(figsize=(5,5))
fig.set_size_inches(6.5, 4.5, forward=True)
#plt.show()
'''
from treeinterpreter import treeinterpreter as ti
prediction, bias, contributions = ti.predict(forest, dt6_2Input.reshape(1,-1))
N = 54 # no of entries in plot , 4 ---> features & 1 ---- class label
major62 = []
major63 = []
major2 = []
indexes = [i_62, i_63, i_2]
for j in range(3):
    list_ =  [major62 , major63, major2]
    for i in range(53):
       val = contributions[0,i,indexes[j]]
       list_[j].append(val)
major62.append(prediction[0,i_62]/5)
major63.append(prediction[0,i_63]/5)
major2.append(prediction[0,i_2]/5)
print(major62)
print(major63)
print(major2)
fig, ax = plt.subplots()
ind = np.arange(N)
width = 0.15
p1 = ax.bar(ind, major62, width, color='red', bottom=0)
p2 = ax.bar(ind+width, major63, width, color='green', bottom=0)
p3 = ax.bar(ind+ (2*width), major2, width, color='yellow', bottom=0)
ax.set_title('Contribution of all features for a major ')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(col, rotation = 90)
ax.legend((p1[0], p2[0] ,p3[0]), ('62', '63', '2' ) , bbox_to_anchor=(1.04,1), loc="upper left")
ax.autoscale_view()
plt.show()
'''


print('2A Returns...')
compareValues(processInput(fake2AInput()))
print('12 Returns...')
compareValues(processInput(fake12Input()))
print('6-2 Returns...')
compareValues(processInput(fake6_2Input()))
'''
#userInput = {}
'''

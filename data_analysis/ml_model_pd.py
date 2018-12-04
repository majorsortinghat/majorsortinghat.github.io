# tensorflow code modified by grace gu, then pp


import numpy as np
import random
 
import tensorflow as tf
import json
import math


import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
 
#FLAGS = None
 
#NUM_LOOPS = 10000
#BATCH_SIZE = 100


traits = ["Satisfaction",
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

def arrtotens_input(input_arr):
    pretensors = np.array(input_arr).transpose()
    tensors = [tf.constant(pretensor) for pretensor in pretensors]
    return dict(zip(traits, tensors))

def main():

    
    with open("outdata.json", "r") as read_file:
        major_data = json.load(read_file)
        majors = major_data.keys()
    
    with open("Major_Mapping_Survey_2.json", "r") as read_file:
        data = json.load(read_file)
    
    alldataarr =[]
    alllabelsarr = []

    for person in data:
        if person["Major_1"] != "Undeclared":
            alllabelsarr.append(str(person["Major_1"]))
            add_data = []
            for trait in traits:
                if trait in person:
                    if person[trait] != 'N/A' and person[trait] != "":
                        add_data.append(int(person[trait]))
                    else:
                        add_data.append(0)
                else:
                    add_data.append(0)
            alldataarr.append(add_data)

            if person["Major_2"] != "":
                alllabelsarr.append(str(person["Major_2"]))
                alldataarr.append(add_data)

    g = tf.Graph()
    with g.as_default():
        input_cols = []
        for trait in traits:
            max_score = 6
            if trait == "Satisfaction":
                max_score = 8
            trait_column = tf.feature_column.categorical_column_with_identity(
                key=trait,
                num_buckets=max_score)
            input_cols.append(trait_column)

        output_column = tf.feature_column.categorical_column_with_vocabulary_list(
            'Major',
            majors
        )
        estimator = tf.estimator.LinearClassifier(feature_columns=input_cols)

        alldata=arrtotens_input(alldataarr)
        alllabels=tf.constant(alllabelsarr)
        traindata=arrtotens_input(alldataarr[:int(len(alldataarr)*.9)])
        print(traindata)
        trainlabels=tf.constant(alllabelsarr[:int(len(alllabelsarr)*.9)])
        print(trainlabels)
        testdata=arrtotens_input(alldataarr[int(len(alldataarr)*.9):])
        testlabels=tf.constant(alllabelsarr[int(len(alllabelsarr)*.9):])
        
        def input_data(features, labels):
            ds = tf.data.Dataset.from_tensor_slices((features, labels))
            ds = ds.shuffle(100).repeat().batch(50)
            return ds

        estimator.train(input_fn = lambda:input_data(traindata, trainlabels))
    '''
    # Create the model
    x = tf.placeholder(tf.float32, [None, 53])
    W = tf.Variable(tf.zeros([53, 2]))
    b = tf.Variable(tf.zeros([2]))
    #y = tf.matmul(x, W) + b
    y = tf.nn.softmax(tf.matmul(x, W) + b)
 
    # Define loss and optimizer
    y_ = tf.placeholder(tf.float32, [None, 2])
 
    # The raw formulation of cross-entropy,
    #
    #   tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.nn.softmax(y)),
    #                                 reduction_indices=[1]))
    #
    # can be numerically unstable.
    #
    # So here we use tf.nn.softmax_cross_entropy_with_logits on the raw
    # outputs of 'y', and then average across the batch.
     
    cross_entropy = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
 
    sess = tf.InteractiveSession()
    tf.global_variables_initializer().run()
    # Train
    for _ in range(NUM_LOOPS):
        idx = random.sample(range(len(traindata)), BATCH_SIZE)
        batch_xs = traindata[idx]
        batch_ys = trainlabels[idx]
 
        #batch_xs, batch_ys = diatom.train.next_batch(100)
        
        try:
            sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
        except ValueError:
            print(batch_xs, batch_ys)
            raise ValueError
 
    # Test trained model
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    #print(sess.run(accuracy, feed_dict={x: diatom.test.images,
    #                                    y_: diatom.test.labels}))
 
    acc = sess.run(accuracy, feed_dict={x: testdata, y_: testlabels})
    print(acc)
    prediction=tf.argmax(y,1)
    #print("predictions", prediction.eval(feed_dict={x: testdata}))
    probability=sess.run(y, feed_dict={x: alldata})
    # print(probability)
 
    np.savetxt('probability', probability)
    np.savetxt('accuracy', np.array([acc]))
    '''
if __name__ == '__main__':

    main()
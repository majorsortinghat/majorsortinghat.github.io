# tensorflow code modified by grace gu, then pp

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
 
import argparse
import sys
import numpy as np
import random
 
import tensorflow as tf
import json
import math


import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
 
FLAGS = None
 
NUM_LOOPS = 10000
BATCH_SIZE = 100
 
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
 
def main(_):
 
  with open("Major_Mapping_Survey_2.json", "r") as read_file:
    data = json.load(read_file)
  
  alldataarr = []
  alllabelsarr = []

  for person in data:
    if person["Major_1"] != "Undeclared":
      alllabelsarr.append(person["Major_1"])
      add_data = []
      for key in keys:
        if key in person:
          if person[key] != 'N/A' and person[key] != "":
            add_data.append(int(person[key]))
          else:
            add_data.append(None)
        else:
          add_data.append(None)
      alldataarr.append(add_data)

      if person["Major_2"] != "":
        alllabelsarr.append(person["Major_2"])
        alldataarr.append(add_data)

  # Import data TODO
  alldata=np.array(alldataarr)
  alllabels=np.array(alllabelsarr)
  traindata=np.array(alldataarr[:int(len(alldataarr)*.9)])
  trainlabels=np.array(alllabelsarr[:int(len(alllabelsarr)*.9)])
  testdata=np.array(alldataarr[int(len(alldataarr)*.9):])
  testlabels=np.array(alllabelsarr[int(len(alllabelsarr)*.9):])
  
 
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
 
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--data_dir', type=str, default='C:\\Users\\Priya Pillai\\Documents\\GitHub\\majorsortinghat\\data_analysis',
                      help='Directory for storing input data')
  FLAGS, unparsed = parser.parse_known_args()
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
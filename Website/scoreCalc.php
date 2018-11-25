<?php
    ini_set("display_errors", 1);
    $jsondata = file_get_contents("outdata.json");
    $data = json_decode($jsondata, true);
    //echo $data['1']['HighSchool_Bio']['Mean'];

    $replies = array();
    echo $_POST['reply']['Like_Parties'];
/*
    foreach($_POST['reply'] as $index => $value) {
        echo $value;
    }

/*
    $FakeVideosOfRealPeople
    $HighSchool_Art
    $HighSchool_Bio
    $HighSchool_Chemistry
    $HighSchool_Engineering
    $HighSchool_English
    $HighSchool_History
    $HighSchool_Leader
    $HighSchool_Math
    $HighSchool_Music
    $HighSchool_Physics
    $HowGreatLeadersInspireGreatAction
    $LetMyDatasetChangeYourMindset
    $Like_BoardGames
    $Like_HangingOut
    $Like_Hiking
    $Like_IndividualSports
    $Like_Parties
    $Like_ReadingBook
    $Like_TeamSports
    $Like_VideoGames



    "Like_ReadingBook": {
        "Mean": 1.5,
        "SD": 0.7071067811865476
    },
    "Like_TeamSports": {
        "Mean": 2.0,
        "SD": 0.0001
    },
    "Like_VideoGames": {
        "Mean": 1.0,
        "SD": 0.0001
    },
    "Like_WatchingMovies": {
        "Mean": 2.0,
        "SD": 0.0001
    },
    "Like_WatchingTV": {
        "Mean": 1.5,
        "SD": 0.7071067811865476
    },
    "MagicIngredientBringsLifeToPixar": {
        "Mean": 0.0,
        "SD": 1.4142135623730951
    },
    "Now_Art": {
        "Mean": -1.0,
        "SD": 1e-05
    },
    "Now_Bio": {
        "Mean": 1.0,
        "SD": 0.0001
    },
    "Now_Chemistry": {
        "Mean": 0.5,
        "SD": 0.7071067811865476
    },
    "Now_Engineering": {
        "Mean": 1.5,
        "SD": 0.7071067811865476
    },
    "Now_English": {
        "Mean": 0.0,
        "SD": 1.4142135623730951
    },
    "Now_History": {
        "Mean": 1.5,
        "SD": 0.7071067811865476
    },
    "Now_Leader": {
        "Mean": 0.0,
        "SD": 1e-05
    },
    "Now_Math": {
        "Mean": 1.0,
        "SD": 0.0001
    },
    "Now_Music": {
        "Mean": -1.0,
        "SD": 1e-05
    },
    "Now_Physics": {
        "Mean": 0.0,
        "SD": 1.4142135623730951
    },
    "PharmacyOfTheFuture": {
        "Mean": -1.5,
        "SD": 0.7071067811865476
    },
    "PowerOfIntroverts": {
        "Mean": 0.0,
        "SD": 1.4142135623730951
    },
    "PowerOfVulnerability": {
        "Mean": -0.5,
        "SD": 0.7071067811865476
    },
    "Rank_AlwaysPrepared": {
        "Mean": 0.5,
        "SD": 2.1213203435596424
    },
    "Rank_AttentionToDetails": {
        "Mean": 1.5,
        "SD": 0.7071067811865476
    },
    "Rank_DifficultyUnderstandingAbstract": {
        "Mean": 0.0,
        "SD": 0.0001
    },
    "Rank_DislikeGettingAttention": {
        "Mean": 0.0,
        "SD": 0.0001
    },
    "Rank_FeelLittleConcernForOthers": {
        "Mean": -1.5,
        "SD": 0.7071067811865476
    },
    "Rank_ForgetToPutThingsBack": {
        "Mean": 0.5,
        "SD": 2.1213203435596424
    },
    "Rank_FullOfIdeas": {
        "Mean": 0.5,
        "SD": 0.7071067811865476
    },
    "Rank_GetChoresDoneRightAway": {
        "Mean": 0.0,
        "SD": 1.4142135623730951
    },
    "Rank_GetIrritatedEasily": {
        "Mean": 0.5,
        "SD": 0.7071067811865476
    },
    "Rank_HaveFrequentMoodSwings": {
        "Mean": 0.5,
        "SD": 2.1213203435596424
    },
    "Rank_Imagination": {
        "Mean": 0.5,
        "SD": 0.7071067811865476
    },
    "Rank_MakePeopleFeelAtEase": {
        "Mean": 1.0,
        "SD": 1.4142135623730951
    },
    "Rank_NotInterestedInOthersProblems": {
        "Mean": -1.0,
        "SD": 0.0001
    },
    "Rank_QuietAroundStrangers": {
        "Mean": 1.5,
        "SD": 0.7071067811865476
    },
    "Rank_RelaxedMostOfTheTime": {
        "Mean": -0.5,
        "SD": 0.7071067811865476
    },
    "Rank_SeldomFeelBlue": {
        "Mean": -1.0,
        "SD": 0.0001
    },
    "Rank_SoftHeart": {
        "Mean": 0.5,
        "SD": 0.7071067811865476
    },
    "Rank_StartConversations": {
        "Mean": 0.0,
        "SD": 1.4142135623730951
    },
    "Rank_TakeTimeOutForOthers": {
        "Mean": 1.0,
        "SD": 0.0001
    },
    "Rank_TalkToDifferentPeopleAtParties": {
        "Mean": -0.5,
        "SD": 0.7071067811865476
    },
    "Rank_ThinkALotBeforeSpeaking": {
        "Mean": 1.0,
        "SD": 0.0001
    },
    "Rank_Understand": {
        "Mean": 1.0,
        "SD": 0.0001
    },
    "Rank_WorryAboutThings": {
        "Mean": 1.0,
        "SD": 0.0001
    },
    "WhatGardeningToldMeAboutLife": {
        "Mean": 0.5,
        "SD": 2.1213203435596424
    },
    "WhatIfGentrificationWasAboutHealing": {
        "Mean": 1.5,
        "SD": 0.7071067811865476
    }*/



?>
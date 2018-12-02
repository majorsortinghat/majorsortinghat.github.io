<?php
    ini_set("display_errors", 1);
    $jsondata = file_get_contents("majorsortinghat/outdata.json");
    $data = json_decode($jsondata, true);
    echo $data['1']['HighSchool_Bio']['Mean'];

    $replies = array();
    //echo $replies;
    //echo $_POST['reply']['Like_Parties'];

    foreach($_POST['reply'] as $index => $value) {
        //echo $value;
        //echo $index;
        $replies[$index] = $value;
    }
    unset($index);
    unset($value);

    
function compareValues($data, $replies) {
    $resultscores = array();
    foreach($data as $major => $value) {
        //echo "O";
        $tempScore = 0;
        $numberOfTriatsChecked = 0;


        
        foreach($replies as $trait => $val) {
            //echo $trait;
            if(in_array($trait, array_keys($value))) {
                

                $tempScore += pow($val-$value[$trait]['Mean'],2)/($value[$trait]['SD']);
                $numberOfTriatsChecked++;
                
            }
        }
        //echo $numberOfTriatsChecked . ": ". $major . " |||         \n";
        $resultscores[$major] = $tempScore/$numberOfTriatsChecked;
        
        //echo $tempScore;
    }
    asort($resultscores);
    

    return $resultscores;
}



function topThree($data, $replies) {
    $fullList = compareValues($data, $replies);
    $three = array_slice($fullList, 0, 3, true); 
    /*
    foreach($three as $key => $val) {
        echo $key . ": " . $val .  "\n";
    }*/
    return $three;
}




?>
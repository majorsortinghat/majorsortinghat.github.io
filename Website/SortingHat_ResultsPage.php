<!DOCTYPE html>
<html>

<head>
    <title>
        The MIT Sorting Hat Results Page

    </title>
    
    
</head>

<body>



    <?php include "scoreCalc.php";?>

    <div id="barViz">

    </div>
    <script type="text/javascript">

        var data = <?php
        echo json_encode(topThree($data, $replies), JSON_HEX_TAG); ?>; //Don't forget the extra semicolon!

        console.log(data);

        

        console.log("hey");
        
    </script>
</body>


</html>
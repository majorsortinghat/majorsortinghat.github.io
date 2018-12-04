<!DOCTYPE html>
<html>

<head>
    <title>
        The MIT Sorting Hat Results Page

    </title>


    <!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <link rel="shortcut icon" type="image/png" href="HatLogo_favicon.png"/>



    
</head>

<body>

    <header>
        <a href="index.php"> The MIT Sorting Hat </a>
    </header>



    <?php include "scoreCalc.php";?>

    <div id="visualization">
    </div>

    <div id="headline">

        </div>


    <script type="text/javascript">

        var userScores = <?php echo json_encode(compareValues($data, $replies), JSON_HEX_TAG); ?>; //Don't forget the extra semicolon!
        var replies = <?php echo json_encode($replies, JSON_HEX_TAG); ?>;
        console.log("Replies");
        console.log(replies);

        console.log("userScores");
        console.log(userScores);

        //console.log(data);
        console.log("hey");
        
    </script>

    <script src="https://d3js.org/d3.v4.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.2/p5.js"></script>
    <script src="SortingHat_ResultsPage.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</body>


</html>
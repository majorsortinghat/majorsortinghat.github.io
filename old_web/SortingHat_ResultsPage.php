<!DOCTYPE html>
<html>

<head>
    <title>
        The MIT Sorting Hat Results Page

    </title>



    <link rel="shortcut icon" type="image/png" href="HatLogo_favicon.png"/>
    <link rel="stylesheet" href="resultsPage.css">



    
</head>

<body>
    <header>

        <div id="HomeButton">
        
        <a href="index.php" class="homebutton"><img id="logoImg" src="HatLogo.png"> <span id="sorthat"> The MIT Sorting Hat</span></a>
    </div>
</header>



    <?php include "scoreCalc.php";?>
    <div id="headline">

        </div>
    <div id="visualization">
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


    <footer>
        <a class="footerLink" href="about.html">About the project</a> <a class="footerLink" href="ourDataset.html">Our dataset</a>
</footer>

    <script src="https://d3js.org/d3.v4.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.2/p5.js"></script>
    <script src="SortingHat_ResultsPage.js"></script>


</body>


</html>
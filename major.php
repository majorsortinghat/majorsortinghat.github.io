<!DOCTYPE html>
<html>

<head>
    <title><?php echo $_GET["id"]; ?></title>
    <link rel="stylesheet" href="major.css">
    <link rel="shortcut icon" type="image/png" href="HatLogo_favicon.png"/>
</head>

<body>
    <header>
        <div id="HomeButton">
        
            <a href="index.php" class="homebutton"><img id="logoImg" src="HatLogo.png"> <span id="sorthat"> The MIT Sorting Hat</span></a>
        </div>

    </header>
    


    
    <?php 
    $jsondata = file_get_contents("major_Descriptions_quote.json");
    $data = json_decode($jsondata, true);
    $thisMajorNum = $_GET["id"];
    $thisMajor = $data[$thisMajorNum];
    ?>



    <div id= "linecontainer">
<div id="linegraph">
    <div id="graphHeadline" style="display: none">Explore how close your match is with course <?php 
echo $thisMajorNum;  ?>: </div>
</div>
<div id="numOfPeople"></div>
<div id="graphExplanation">
<svg >
  <rect id="userDot" />
</svg>You <svg ><rect id="majorDot" /></svg><?php echo $thisMajorNum;  ?>
</div>
</div>
    <div>
         
    
    </div>
   
<h1>
<a href="<?php echo $thisMajor["CourseSite"]; ?>">
    <?php echo $thisMajorNum;  ?>:
    <?php echo $thisMajor["Name"]; ?>
</a>


</h1>

<h3 id="matchScore">
</h3>




<div id ="paragraph">
    <p>
        <?php echo $thisMajor["Description"]; ?>
        
</p>
</div>

<div id="personas">
    <div id="persona0" class ="subpersona">
        <img id="personaImg1"  style="height: 150px; width: 150px; border-radius: 75px;">
        <div>
        <q id="personaQuote1"></q>
        </div>
    </div>

    <div id="persona1"class ="subpersona">
        <img id="personaImg1"  style="height: 150px; width: 150px; border-radius: 75px;">
        <div>
        <q id="personaQuote1"></q>
        </div>
    </div>
´
    <div id="persona2"class ="subpersona">
        <img id="personaImg1"  style="height: 150px; width: 150px; border-radius: 75px;">
        <div>
        <q id="personaQuote1"></q>
</div>

    </div>

</div>




    <footer>
        <a class="footerLink" href="about.html">About the project</a> <a class="footerLink" href="ourDataset.html">Our dataset</a><a class="footerLink" href="<?php echo $thisMajor["TextCitation"]; ?>">Text adapted from this site</a>
</footer>

<script src="major.js"></script>
<script src="https://d3js.org/d3.v4.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.2/p5.js"></script>
</body>

</html>
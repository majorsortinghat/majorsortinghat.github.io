<!DOCTYPE html>
<html>

<head>
    <title><?php echo $_GET["id"]; ?></title>
    <link rel="stylesheet" href="major.css">
    <link rel="shortcut icon" type="image/png" href="HatLogo_favicon.png"/>
    <script src="major.js"></script>
    <script src="https://d3js.org/d3.v4.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.2/p5.js"></script>

</head>

<body>
    <header>
        <div id="HomeButton">
        
            <a href="index.php" class="homebutton"><img id="logoImg" src="HatLogo.png"> <span id="sorthat"> The MIT Sorting Hat</span></a>
        </div>
    </header>
    
    
    <?php 
    $jsondata = file_get_contents("major_Descriptions.json");
    $data = json_decode($jsondata, true);
    $thisMajorNum = $_GET["id"];
    $thisMajor = $data[$thisMajorNum];
    ?>
    <div>
         
    
    </div>
   
<h1>
<a href="<?php echo $thisMajor["CourseSite"]; ?>">
    <?php echo $thisMajorNum;  ?>:
    <?php echo $thisMajor["Name"]; ?>
</a>


</h1>




<div id ="paragraph">
    <p>
        <?php echo $thisMajor["Description"]; ?>
        <a href="<?php echo $thisMajor["TextCitation"]; ?>">Text adapted from this site</a>
</p>
</div>

<div id="linegraph">
    <div id="graphHeadline">Explore how close your match is with course <?php 
echo $thisMajorNum;  ?>: </div>
</div>
<div id="graphExplanation">
<svg >
  <rect id="userDot" />
</svg>You <svg ><rect id="majorDot" /></svg><?php echo $thisMajorNum;  ?>
</div>

    <footer>
        <a class="footerLink" href="about.html">About the project</a> <a class="footerLink" href="ourDataset.html">Our dataset</a>
</footer>

</body>

</html>
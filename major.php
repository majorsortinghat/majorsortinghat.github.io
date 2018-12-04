<!DOCTYPE html>
<html>

<head>
    <title><?php echo $_GET["id"]; ?></title>
    <link rel="stylesheet" href="major.css">
</head>

<body>
    <header>
    <a href="index.php">The MIT Sorting Hat</a>
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

<?php 
echo $thisMajorNum;  ?>: 
<?php echo $thisMajor["Name"]; ?>



</h1>




<div id ="paragraph">
    <p>
        <?php echo $thisMajor["Description"]; ?>
        <a href="<?php echo $thisMajor["TextCitation"]; ?>">link</a>
</p>
</div>

<div id="linegraph">
</div>

<script src="major.js"></script>
<script src="https://d3js.org/d3.v4.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.2/p5.js"></script>
</body>

</html>
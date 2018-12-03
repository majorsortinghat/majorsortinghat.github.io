<!DOCTYPE html>
<html>

<head>
    <title><?php echo $_GET["id"]; ?></title>
</head>

<body>
    <a href="index.php">The MIT Sorting Hat</a>
    <div>
         Welcome
    
</div>
   
<h1>
<?php echo $_GET["id"]; ?><br>

</h1>

<?php echo $_SESSION['data']; ?><br>


<div id ="paragraph">
    <p>
    Drinking vinegar helvetica lo-fi yr bicycle rights prism health goth YOLO. 
    Aesthetic four dollar toast selfies food truck, poutine hexagon street art 
    vexillologist man braid gluten-free blog hashtag next level shabby chic. 
    Vexillologist knausgaard lumbersexual kitsch celiac kale chips edison bulb. 
    Tbh iPhone listicle hella gastropub. Cold-pressed +1 wayfarers deep v kombucha 
    microdosing. 3 wolf moon pitchfork sustainable bicycle rights, shabby chic coloring 
    book truffaut irony gluten-free.
</p>
</div>


<script type="text/javascript">
    console.log("hey");
    var data = <?php echo json_encode($_SESSION['data'], JSON_HEX_TAG); ?>; //Don't forget the extra semicolon!

    console.log(data);

    //console.log(data);
    console.log("hey");

</script>
</body>

</html>
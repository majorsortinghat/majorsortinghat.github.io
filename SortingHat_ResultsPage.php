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

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    
<script src="vis/dist/vis.js"></script>
  <link href="vis/dist/vis.css" rel="stylesheet" type="text/css" />

  <script src="https://d3js.org/d3-path.v1.min.js"></script>
<script src="https://d3js.org/d3-shape.v1.min.js"></script>

    
</head>

<body>



    <?php include "scoreCalc.php";?>

    <div id="visualization">



    </div>

    <script>

        var line = d3.line();

    </script>
    <script type="text/javascript">

        var data = <?php
        echo json_encode(topThree($data, $replies), JSON_HEX_TAG); ?>; //Don't forget the extra semicolon!

        console.log(data);



    var container = document.getElementById('visualization');
    var items = [
        {x: '2014-06-11', y: 10},
        {x: '2014-06-12', y: 25},
        {x: '2014-06-13', y: 30},
        {x: '2014-06-14', y: 10},
        {x: '2014-06-15', y: 15},
        {x: '2014-06-16', y: 30}
    ];

    var dataset = new vis.DataSet(items);
    var options = {
        style:'bar',
        barChart: {width:50, align:'center'}, // align: left, center, right
        drawPoints: false,
        dataAxis: {
            icons:true
        },
        orientation:'top',
        start: '2014-06-10',
        end: '2014-06-18'
    };
    //var graph2d = new vis.Graph2d(container, items, options);



        

        console.log("hey");
        
    </script>
</body>


</html>
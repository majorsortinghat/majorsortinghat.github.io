<!DOCTYPE html>
<html>

<head>
    <title>
        The MIT Sorting Hat Results Page

    </title>
    <script src="vis/dist/vis.js"></script>
    <link href="vis/dist/vis.css" rel="stylesheet" type="text/css" />
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
        var container = document.getElementById('barViz');
        var items = [{
            x: '2014-06-11',
            y: 10
        }, {
            x: '2014-06-12',
            y: 25
        }, {
            x: '2014-06-13',
            y: 30
        }, {
            x: '2014-06-14',
            y: 10
        }, {
            x: '2014-06-15',
            y: 15
        }, {
            x: '2014-06-16',
            y: 30
        }];



        var dataset = new vis.DataSet(items);
        var options = {
            start: '2014-06-10',
            end: '2014-06-18'
        };
        var graph2d = new vis.Graph2d(container, dataset, options);
    </script>
</body>


</html>
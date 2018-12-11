var w = window.innerWidth;
var h = window.innerHeight * 0.95;
//console.log(majors_len);
var minScreensDimension = Math.min.apply(null, [w, h]);
//console.log(minScreensDimension);
var center = [w / 2, h / 2];
var highlightKey = null;

//document.getElementById("headline").innerHTML = "Your closest major is " + findBestMajor(majors, 1);
//console.log(data);
var avg = function ( p ) {
    var avgUserScores = null;
    var avgMajors = null;
    var avgSortedMajorScores = null;
    var avgMajors_len = null;
    p.setup = function() {
        var myCanvas = p.createCanvas(w, h);
        avgUserScores = avgScores;
        avgMajors = sortMajors(cleanData(avgUserScores))[0];
        avgSortedMajorScores = sortMajors(cleanData(avgUserScores))[1];
        avgMajors_len = Object.keys(avgMajors).length;
        //myCanvas.parent("visualization_1");
    };

    p.draw = function() {
        draw_dist(avgUserScores, avgSortedMajorScores, avgMajors, avgMajors_len, p);
    };
};

var myp5 = new p5(avg, "visualization_1")

var forest = function ( p ) {
    var forestUserScores = null;
    var forestMajors = null;
    var forestSortedMajorScores = null;
    var forestMajors_len = null;
    p.setup = function() {
        var myCanvas = p.createCanvas(w, h);
        forestUserScores = forestScores;
        forestMajors = sortMajors(cleanData(forestUserScores))[0];
        forestSortedMajorScores = sortMajors(cleanData(forestUserScores))[1];
        forestMajors_len = Object.keys(forestMajors).length;
        //myCanvas.parent("visualization_1");
    };

    p.draw = function() {
        draw_dist(forestUserScores, forestSortedMajorScores, forestMajors, forestMajors_len, p);
    };
};

var myp5 = new p5(forest, "visualization_2")

var linear = function ( p ) {
    var linUserScores = null;
    var linMajors = null;
    var linSortedMajorScores = null;
    var linMajors_len = null;
    p.setup = function() {
        var myCanvas = p.createCanvas(w, h);
        linUserScores = linearScores;
        linMajors = sortMajors(cleanData(linUserScores))[0];
        linSortedMajorScores = sortMajors(cleanData(linUserScores))[1];
        linMajors_len = Object.keys(linMajors).length;
        //myCanvas.parent("visualization_1");
    };

    p.draw = function() {
        draw_dist(linUserScores, linSortedMajorScores, linMajors, linMajors_len, p);
    };
};

var myp5 = new p5(linear, "visualization_3")

function cleanData(dirtyData) {
    //console.log(dirtyData);
    var cleanDict = {};
    var values = Object.keys(dirtyData).map(function(key) {
        return dirtyData[key];
    });
    var min_value = Math.min.apply(null, values);

    //console.log(min_value);
    for (var key in dirtyData) {
        //console.log(key);
        // check if the property/key is defined in the object itself, not in parent
        if (dirtyData.hasOwnProperty(key)) {
            if (dirtyData[key] <= min_value * 3) {
                //console.log(dirtyData[key]);
                cleanDict[key] = dirtyData[key] / min_value;
            }
            //console.log(key, dictionary[key]);
        }
    }
    //findBestMajor(cleanDict, min_value);

    return cleanDict;
}

function sortMajors(majors) {
    tempDict = {};
    tempArr = [];
    for (var major in majors) {
        tempDict[majors[major]] = major;
        tempArr.push(majors[major]);
    }

    tempArr.sort();
    //console.log("tempArr: " + tempArr);
    return [tempDict, tempArr];

}

function draw_dist(userScores, sortedMajorScores, majors, majors_len, p) {
    p.background(0, 30, 50);
    //var majors = cleanData(data);
    var textcolor = [255, 255, 255];
    var n = 0.6;
    p.fill(textcolor);

    p.textAlign(p.CENTER, p.CENTER);
    p.ellipseMode(p.CENTER); // Set ellipseMode to p.CENTER

    var x = p.mouseX,
        y = p.mouseY;
    for (var i = 0; i < sortedMajorScores.length; i++) {
        var key = sortedMajorScores[i];
        //console.log(key);

        p.textSize(14);
        p.colorMode(p.HSL);

        p.stroke(100, 255, 40 + n * 2.5);
        var dx = (minScreensDimension / 6) * Math.cos(2 * Math.PI * n / majors_len) * key;
        var dy = (minScreensDimension / 6) * Math.sin(2 * Math.PI * n / majors_len) * key;

        var corrY = 1 * (dx);
        var corrX = 1;

        p.line(center[0], center[1], center[0] + dx, center[1] + dy);
        p.noStroke();
        var horizAlign = p.CENTER;

        if (dx + center[0] < center[0]) {
            corrX = -1;
            horizAlign = p.CENTER;
        }
        if (dy + center[1] < center[1]) {
            corrY = -1;
            p.textAlign(horizAlign, p.CENTER);
        } else {
            p.textAlign(horizAlign, p.CENTER);
        }

        p.colorMode(p.RGB);
        var posX = center[0] + dx + 1.5 * p.sqrt(p.abs(dx * 1.5)) * dx / p.abs(dx),
            posY = center[1] + dy + 1.5 * p.sqrt(p.abs(dy * 1.5)) * dy / p.abs(dy);

        if ((highlightKey == majors[key] && (x > posX - 40 && x < posX + 40 && y > posY - 40 && y < posY + 40)) || (x > posX - 20 && x < posX + 20 && y > posY - 10 && y < posY + 10)) {
            //console.log(key);
            highlightKey = majors[key];
            p.colorMode(p.HSL);
            p.fill(15 * p.sq(p.sq(key)), 100, 45);
            //posX += dx * 1.01;
            //posY += dy * 1.01;
            p.ellipse(posX, posY, 90);
            p.colorMode(p.RGB);
            p.textSize(12);
            p.fill(textcolor);
            p.text("Distance: " + userScores[majors[key]].toFixed(2) + "\nlearn more", posX, posY + 15);
            if (majors[key].length < 5) {
                p.textSize(30);
            } else {
                p.textSize(21);
            }

            p.text(majors[key], posX, posY - 15);
            if (p.mouseIsPressed) {
                //console.log("Pressed");
                var urlEnd = "";
                //sessionStorage.setItem(key, )

                //console.log(urlEnd);

                //console.log(sessionStorage);
                var url = "http://" + window.location.host + "/" + "major/" + majors[key];
                //console.log(url);
                window.location = url;
            }


        } else {
            p.text(majors[key], posX, posY);
        }

        n++;

        //console.log(key, key);
    }

    p.fill(180, 200, 255); // Set fill
    /*
        if (x < center[0] + 20 && x > center[0] - 20 && y < center[1] + 20 && y > center[1] - 20) {
            ellipse(center[0], center[1], 60); // Draw gray ellipse using p.CENTER mode
            fill(textcolor);
            textSize(14);
            text("ABOUT\nYOU", center[0], center[1]);
            if (mouseIsPressed) {
                //console.log("Pressed");
                var url = "http://" + window.location.host + "/" + "about_you.html";
                window.location = url;
            }
        } else {*/
    p.ellipse(center[0], center[1], 30); // Draw gray ellipse using p.CENTER mode
    //}
};
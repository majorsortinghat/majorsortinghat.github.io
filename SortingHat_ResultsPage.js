console.log("hey");

var w = window.innerWidth;
var h = window.innerHeight * 0.95;
var majors = cleanData(userScores);
var majors_len = Object.keys(majors).length;
//console.log(majors_len);
var minScreensDimension = Math.min.apply(null, [w, h]);
//console.log(minScreensDimension);
var center = [w / 2, h / 2];


var highlightKey = null;


document.getElementById("headline").innerHTML = "Your closest major is " + findBestMajor(majors, 1);
//console.log(data);

function findBestMajor(majors, value) {

    for (var key in majors) {

        if (majors[key] == value) {
            return key;
        }
    }

    return null;

}






function setup() {
    var myCanvas = createCanvas(w, h);
    myCanvas.parent('visualization');

}



function draw() {
    background(0, 30, 50);
    //var majors = cleanData(data);
    var textcolor = [255, 255, 255];
    var n = 0.6;
    fill(textcolor);

    textAlign(CENTER, CENTER);
    ellipseMode(CENTER); // Set ellipseMode to CENTER



    var x = mouseX,
        y = mouseY;
    for (var key in majors) {

        textSize(14);
        colorMode(HSL);

        stroke(100, 255, 40 + n * 2.5);
        var dx = (minScreensDimension / 6) * Math.cos(2 * Math.PI * n / majors_len) * majors[key];
        var dy = (minScreensDimension / 6) * Math.sin(2 * Math.PI * n / majors_len) * majors[key];

        var corrY = 1 * (dx);
        var corrX = 1;

        line(center[0], center[1], center[0] + dx, center[1] + dy);
        noStroke();
        var horizAlign = CENTER;

        if (dx + center[0] < center[0]) {
            corrX = -1;
            horizAlign = CENTER;
        }
        if (dy + center[1] < center[1]) {
            corrY = -1;
            textAlign(horizAlign, CENTER);
        } else {
            textAlign(horizAlign, CENTER);
        }

        colorMode(RGB);
        var posX = center[0] + dx + 1.5 * sqrt(abs(dx * 1.5)) * dx / abs(dx),
            posY = center[1] + dy + 1.5 * sqrt(abs(dy * 1.5)) * dy / abs(dy);



        if ((highlightKey == key && (x > posX - 40 && x < posX + 40 && y > posY - 40 && y < posY + 40)) || (x > posX - 20 && x < posX + 20 && y > posY - 10 && y < posY + 10)) {
            //console.log(key);
            highlightKey = key;
            colorMode(HSL);
            fill(15 * sq(sq(majors[key])), 100, 45);
            //posX += dx * 1.01;
            //posY += dy * 1.01;
            ellipse(posX, posY, 90);
            colorMode(RGB);
            textSize(12);
            fill(textcolor);
            text("Distance: " + userScores[key].toFixed(2) + "\nlearn more", posX, posY + 15);
            textSize(30);
            text(key, posX, posY - 15);
            if (mouseIsPressed) {
                //console.log("Pressed");
                var urlEnd = "";
                //sessionStorage.setItem(key, )

                for (var reply in replies) {
                    sessionStorage.setItem("reply", [reply, parseInt(replies[reply])]);

                    //urlEnd = urlEnd.concat("&" + reply + "=t[" + replies[reply] + "]");
                }
                //console.log(urlEnd);

                //console.log(sessionStorage);
                var url = "http://" + window.location.host + "/" + "major.php?id=" + key;
                //console.log(url);
                window.location = url;
            }


        } else {
            text(key, posX, posY);
        }


        n++;

        //console.log(key, majors[key]);
    }






    fill(180, 200, 255); // Set fill
    /*
        if (x < center[0] + 20 && x > center[0] - 20 && y < center[1] + 20 && y > center[1] - 20) {
            ellipse(center[0], center[1], 60); // Draw gray ellipse using CENTER mode
            fill(textcolor);
            textSize(14);
            text("ABOUT\nYOU", center[0], center[1]);
            if (mouseIsPressed) {
                //console.log("Pressed");
                var url = "http://" + window.location.host + "/" + "about_you.html";
                window.location = url;
            }
        } else {*/
    ellipse(center[0], center[1], 30); // Draw gray ellipse using CENTER mode
    //}




}


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
    findBestMajor(cleanDict, min_value);

    return cleanDict;
}
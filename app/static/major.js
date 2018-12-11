var currentSearch = majorNum;
var thisMajorProfile = outData[currentSearch];
var w = window.innerWidth * 0.9;
var h = window.innerHeight / 4.5;
var thisperson = sessionStorage;
var vertMid = h / 2;
var thesaurus = majorTranslator;
var personas = {};
var descriptions;

setNumOfPeople()

fillPersonas(majorDescriptionsQuote)

function setup() {

    var myCanvas = createCanvas(w, h);
    myCanvas.parent("linegraph");

}

var notPrinted = true;

function draw() {
    background(0, 30, 50);

    var x = mouseX,
        y = mouseY;

    var length = vals.length;
    var count = 1;
    strokeWeight(0.5);
    for (var i = 0; i < 5; i++) {
        stroke(255, 255, 255, 100);
        line(0, (0.5 + i) * h / 5, w, (0.5 + i) * h / 5);
    }
    var major = "";
    strokeWeight(0.5);
    for (var key in keys) {
        if (key in vals) {

            var posX = count * w / length;
            var posY = vertMid;

            //console.log(thisMajorProfile[item]['Mean']);
            //var colorPerson = [255, 0, 0];
            //var colorPerson = [0, 255, 0];
            var diameter = 10;
            //var drawInfo = false;
            noStroke();

            if ((x > posX - 0.5 * w / length && x < posX + 0.5 * w / length && y > posY - vertMid && y < posY + vertMid)) {
                diameter = 18;
                //drawInfo = true;
                major = key;
            }
            rectMode(CENTER);
            fill(180, 200, 255, 200);
            rect((count-.5) * w / length, vertMid - thisMajorProfile[keys[key]]['Mean'] * h / 5, 5, thisMajorProfile[keys[key]]['SD'] * h / 5);
            fill(80, 120, 255);
            ellipse((count-.5) * w / length, vertMid - thisMajorProfile[keys[key]]['Mean'] * h / 5, diameter);
            //console.log(thisMajorProfile[item]['Mean']);
            fill(160, 255, 140);
            ellipse((count-.5) * w / length, vertMid - vals[key] * h / 5, diameter);

            count++;
        }

    }
    if (major != "") {
        fill(120, 120, 120, 220);

            var width = "You: ".concat(vals[major]).concat(".  .").concat("Avg of ").concat(currentSearch).concat(": ").concat(thisMajorProfile[keys[major]]['Mean']).length * 7 + 25;
        if (width < thesaurus[keys[major]].length * 8.1 + 20) {
            width = thesaurus[keys[major]].length * 8.1 + 20;
        }
        var startX = mouseX;
        //var correction = 1;
        if (mouseX + width > w) {

            startX = mouseX - width;
            //correction = -1;
        }
        rectMode(CORNER);
        rect(startX + 5, mouseY + 5, width, 55, 5);
        fill(255);
        textSize(17);
        text(thesaurus[keys[major]], startX + 20, mouseY + 28);
        textSize(14);
        text("You: " + vals[major], startX + 35, mouseY + 45)
        text("Avg of " + currentSearch + ": " + thisMajorProfile[keys[major]]['Mean'].toFixed(2), startX + 90, mouseY + 45)
            //console.log(thisMajorProfile[major]['Mean']);
    }
    //for (var entry in vals) {
        //console.log(thisMajorProfile)
        //if (null != null) {
            //console.log(thisMajorProfile[entry]['Mean']);
        //}
        //console.log(entry);
    //}
}

function fillPersonas(desc) {
    for (var i = 0; i < 3; i++) {
        var tempString = "persona".concat(i.toString());
        personas[tempString] = document.getElementById(tempString);
        var dim = (Math.ceil(Math.random() * 100) * 10 + 50).toString();
        personas[tempString].children[0].src = "https://www.placecage.com/" + dim + "/" + dim;
        personas[tempString].children[1].innerHTML = desc[currentSearch]["Quote"][i];
    }

}

function setNumOfPeople() {
    if (thisMajorProfile["numOfPeople"] > 5) {
        document.getElementById("numOfPeople").innerHTML = "Based on the answers from " + thisMajorProfile["numOfPeople"] + " people in this major";
    } else {
        document.getElementById("numOfPeople").innerHTML = "Based on the answers from fewer than 5 people in this major";
    }

}
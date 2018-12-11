var thisMajorProfile;
var currentSearch = window.location.search.replace('?id=', '');
var w = window.innerWidth * 0.9;
var h = window.innerHeight / 4.5;
var thisperson = sessionStorage;
var vertMid = h / 2;
var thesaurus;
var personas = {};
var descriptions;





function setMajor(data) {
    thisMajorProfile = data[currentSearch];
    console.log(thisMajorProfile);
    setNumOfPeople();
}

function loadJSON(path, success, error) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                if (success)
                    return success(JSON.parse(xhr.responseText));
            } else {
                if (error)
                    error(xhr);
            }
        }
    };
    xhr.open("GET", path, true);
    xhr.send();
}

thisMajorProfile = loadJSON('majorsortinghat/outdata.json',
    setMajor,
    function(xhr) { console.error(xhr); }
);
thesaurus = loadJSON('majorsortinghat/majorTranslator.json',
    function(data) {
        var innerThesaurus = data;
        console.log(innerThesaurus);
        return innerThesaurus;
    },
    function(xhr) { console.error(xhr); }
);
loadJSON('major_Descriptions_quote.json',
    fillPersonas,
    function(xhr) { console.error(xhr); }
);

console.log(thisperson);
console.log(thesaurus);
console.log(thisMajorProfile);
console.log(thisperson)
console.log("connected!");
//console.log(currentSearch);


function setup() {

    var myCanvas = createCanvas(w, h);
    myCanvas.parent("linegraph");

}

var notPrinted = true;

function draw() {
    background(0, 30, 50);

    var x = mouseX,
        y = mouseY;

    var length = thisperson.length;
    var count = 1;
    strokeWeight(0.5);
    for (var i = 0; i < 5; i++) {
        stroke(255, 255, 255, 100);
        line(0, (0.5 + i) * h / 5, w, (0.5 + i) * h / 5);
    }
    var major = "";
    strokeWeight(0.5);
    for (var item in thisMajorProfile) {
        //console.log(item);

        //console.log("Hey");
        if (thisperson[item] != null) {

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
                major = item;
            }

            rectMode(CENTER);
            fill(180, 200, 255, 200);
            rect(count * w / length, vertMid - thisMajorProfile[item]['Mean'] * h / 5, 5, thisMajorProfile[item]['SD'] * h / 5);
            fill(80, 120, 255);
            ellipse(count * w / length, vertMid - thisMajorProfile[item]['Mean'] * h / 5, diameter);
            //console.log(thisMajorProfile[item]['Mean']);
            fill(160, 255, 140);
            ellipse(count * w / length, vertMid - thisperson[item] * h / 5, diameter);

            count++;
        }

    }
    if (major != "") {
        fill(120, 120, 120, 220);

        var width = "You: ".concat(thisperson[item]).concat(".  .").concat("Avg of ").concat(currentSearch).concat(": ").concat(thisMajorProfile[item]['Mean']).length * 7 + 25;
        if (width < thesaurus[major].length * 8.1 + 20) {
            width = thesaurus[major].length * 8.1 + 20;
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
        text(thesaurus[major], startX + 20, mouseY + 28);
        textSize(14);
        text("You: " + thisperson[major], startX + 35, mouseY + 45)
        text("Avg of " + currentSearch + ": " + thisMajorProfile[major]['Mean'].toFixed(2), startX + 90, mouseY + 45)
            //console.log(thisMajorProfile[major]['Mean']);
    }
    for (var entry in thisperson) {
        //console.log(thisMajorProfile)
        if (null != null) {
            console.log(thisMajorProfile[entry]['Mean']);
        }
        //console.log(entry);
    }
}

function fillPersonas(desc) {
    console.log(desc);
    for (var i = 0; i < 3; i++) {
        var tempString = "persona".concat(i.toString());
        console.log(tempString);
        personas[tempString] = document.getElementById(tempString);
        console.log(personas[tempString].children[1]);
        var dim = (Math.ceil(Math.random() * 100) * 10 + 50).toString();
        personas[tempString].children[0].src = "https://www.placecage.com/" + dim + "/" + dim;
        personas[tempString].children[1].children[0].innerHTML = desc[currentSearch]["Quote"][i];
    }

}

function setNumOfPeople() {
    if (thisMajorProfile["numOfPeople"] > 5) {
        document.getElementById("numOfPeople").innerHTML = "Based on the answers from " + thisMajorProfile["numOfPeople"] + " people in this major";
    } else {
        document.getElementById("numOfPeople").innerHTML = "Based on the answers from fewer than 5 people in this major";
    }

}
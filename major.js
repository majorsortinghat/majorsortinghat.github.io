var thisMajorProfile;
var currentSearch = window.location.search.replace('?id=', '');
var w = window.innerWidth * 0.9;
var h = window.innerHeight / 6;
var thisperson = sessionStorage;
var vertMid = h / 2;
var thesaurus;


function setMajor(data) {
    var innerThisMajorProfile = data[currentSearch];
    console.log(innerThisMajorProfile);
    return innerThisMajorProfile;
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


console.log(thesaurus);
console.log(thisMajorProfile);
console.log("connected!");
//console.log(currentSearch);


function setup() {

    var myCanvas = createCanvas(w, h);
    myCanvas.parent("linegraph");

}


function draw() {
    background(255);



    var x = mouseX,
        y = mouseY;


    var length = thisperson.length;
    var count = 1;

    for (var i = 0; i < 5; i++) {
        stroke(220);
        line(0, (0.5 + i) * h / 5, w, (0.5 + i) * h / 5);
    }
    var major = "";

    for (var item in thisMajorProfile) {
        //console.log(item);

        //console.log("Hey");
        if (thisperson[item] != null) {

            var posX = count * w / length;
            var posY = vertMid;

            //console.log(thisMajorProfile[item]['Mean']);
            var colorPerson = [255, 0, 0];
            var colorPerson = [0, 255, 0];
            var diameter = 9;
            var drawInfo = false;
            noStroke();

            if ((x > posX - 0.5 * w / length && x < posX + 0.5 * w / length && y > posY - vertMid && y < posY + vertMid)) {
                diameter = 15;
                drawInfo = true;
                major = item;
            }


            rectMode(CENTER);
            fill(180, 200, 255);
            rect(count * w / length, vertMid - thisMajorProfile[item]['Mean'] * h / 5, 5, thisMajorProfile[item]['Mean'] * h / 5);
            fill(100, 150, 255);
            ellipse(count * w / length, vertMid - thisMajorProfile[item]['Mean'] * h / 5, diameter);
            //console.log(thisMajorProfile[item]['Mean']);
            fill(150, 250, 200);
            ellipse(count * w / length, vertMid - thisperson[item] * h / 5, diameter);




            count++;
        }

    }
    if (major != "") {
        fill(200);

        var width = "You: ".concat(thisperson[item]).concat(".  .").concat("Avg of ").concat(currentSearch).concat(": ").concat(thisMajorProfile[item]['Mean']).length * 7 + 25;
        if (width < thesaurus[major].length * 8.1 + 20) {
            width = thesaurus[major].length * 8.1 + 20;
        }
        var startX = mouseX;
        var correction = 1;
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
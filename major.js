var thisMajorProfile;
var currentSearch = window.location.search.replace('?id=', '');
var w = window.innerWidth;
var h = window.innerHeight / 8;
var thisperson = sessionStorage;
var vertMid = h / 2;
var thesaurus;


function setMajor(data) {
    thisMajorProfile = data[currentSearch];
    console.log(thisMajorProfile);
}

function loadJSON(path, success, error) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                if (success)
                    success(JSON.parse(xhr.responseText));
            } else {
                if (error)
                    error(xhr);
            }
        }
    };
    xhr.open("GET", path, true);
    xhr.send();
}

loadJSON('majorsortinghat/outdata.json',
    setMajor,
    function(xhr) { console.error(xhr); }
);
loadJSON('majorsortinghat/majorTranslator.json',
    function(data) {
        thesaurus = data;
        console.log(thesaurus);
    },
    function(xhr) { console.error(xhr); }
);



console.log(thesaurus);
console.log(thisMajorProfile);
console.log("connected!");
//console.log(currentSearch);


function setup() {

    var myCanvas = createCanvas(w, h);
    myCanvas.parent('linegraph');

}


function draw() {
    background(255);



    var x = mouseX,
        y = mouseY;


    var length = thisperson.length;
    var count = 1;

    for (var i = 0; i < 5; i++) {
        stroke(200);
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
            var diameter = 5;
            var drawInfo = false;
            noStroke();

            if ((x > posX - 10 && x < posX + 10 && y > posY - vertMid && y < posY + vertMid)) {
                diameter = 10;
                drawInfo = true;
                major = item;
            }
            fill(255, 0, 0);
            ellipse(count * w / length, vertMid + thisperson[item] * h / 5, diameter);
            fill(0, 255, 0);
            ellipse(count * w / length, vertMid + thisMajorProfile[item]['Mean'] * h / 5, diameter);





            count++;
        }

    }
    if (major != "") {
        fill(200);

        var width = "You: ".concat(thisperson[item]).concat(".    .").concat("Avg of ").concat(currentSearch).concat(": ").concat(thisMajorProfile[item]['Mean']).length * 7 + 20;
        if (width < thesaurus[major].length * 7 + 20) {
            width = thesaurus[major].length * 7 + 20;
        }
        var startX = mouseX;
        var correction = 1;
        if (mouseX + width > w) {
            console.log("Too big");
            startX = mouseX - width;
            //correction = -1;
        }
        rect(startX + 5 * correction, mouseY + 5, width, 55, 5);
        fill(255);
        textSize(14);
        text(thesaurus[major], startX + 20 * correction, mouseY + 25);
        textSize(12);
        text("You: " + thisperson[item], startX + 20 * correction, mouseY + 45)
        text("Avg of " + currentSearch + ": " + thisMajorProfile[item]['Mean'], startX + 70 * correction, mouseY + 45)


    }
    for (var entry in thisperson) {
        //console.log(thisMajorProfile)
        if (null != null) {
            console.log(thisMajorProfile[entry]['Mean']);
        }
        //console.log(entry);
    }

}
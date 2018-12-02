console.log("hey");

var w = window.innerWidth;
var h = window.innerHeight * 0.8;
var majors = cleanData(data);
var majors_len = Object.keys(majors).length;
console.log(majors_len);
var minScreensDimension = Math.min.apply(null, [w, h]);
console.log(minScreensDimension);
var center = [w / 2, h / 2];

//console.log(data);





function setup() {
    var myCanvas = createCanvas(w, h);
    myCanvas.parent('visualization');

}



function draw() {

    //var majors = cleanData(data);
    var n = 1;
    fill(0);
    textSize(14);
    textAlign(CENTER, CENTER);
    for (var key in majors) {
        stroke(150);
        var dx = (minScreensDimension / 7) * Math.cos(2 * Math.PI * n / majors_len) * majors[key];
        var dy = (minScreensDimension / 7) * Math.sin(2 * Math.PI * n / majors_len) * majors[key];

        var corrY = 1;
        var corrX = 1;

        line(center[0], center[1], center[0] + dx, center[1] + dy);
        noStroke();
        if (dx + center[0] < center[0]) {
            corrX = -1;
        }
        if (dy + center[1] < center[1]) {
            corrY = -1;
        }
        text(key, center[0] + dx + 10 * corrX, center[1] + dy + 10 * corrY);
        n++;
        //console.log(key, majors[key]);
    }

    ellipseMode(CENTER); // Set ellipseMode to CENTER
    fill(255, 0, 50); // Set fill

    ellipse(center[0], center[1], 50); // Draw gray ellipse using CENTER mode

}


function cleanData(dirtyData) {
    //console.log(dirtyData);
    var cleanDict = {};


    var values = Object.keys(dirtyData).map(function(key) {
        return dirtyData[key];
    });
    var min_value = Math.min.apply(null, values);
    //console.log(min_value);
    for (var key in data) {
        //console.log(key);
        // check if the property/key is defined in the object itself, not in parent
        if (dirtyData.hasOwnProperty(key)) {
            if (dirtyData[key] <= min_value * 5) {
                //console.log(dirtyData[key]);
                cleanDict[key] = dirtyData[key] / min_value;
            }
            //console.log(key, dictionary[key]);
        }
    }
    return cleanDict;
}
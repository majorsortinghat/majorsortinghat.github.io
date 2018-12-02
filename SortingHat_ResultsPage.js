console.log("hey");

var w = window.innerWidth;
var h = window.innerHeight;
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

    ellipseMode(CENTER); // Set ellipseMode to CENTER
    fill(255, 0, 50); // Set fill
    noStroke();
    ellipse(center[0], center[1], 50); // Draw gray ellipse using CENTER mode


    stroke(150);
    //var majors = cleanData(data);
    var n = 1;
    for (var key in majors) {

        var x = center[0] + (minScreensDimension / 7) * Math.cos(2 * Math.PI * n / majors_len) * majors[key];
        var y = center[1] + (minScreensDimension / 7) * Math.sin(2 * Math.PI * n / majors_len) * majors[key];

        line(center[0], center[1], x, y);
        text(key, x, y);
        n++;
        //console.log(key, majors[key]);
    }

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
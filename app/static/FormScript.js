function show(shown, hidden) {
    document.getElementById(shown).style.display = 'block';
    document.getElementById(hidden).style.display = 'none';
    return false;
}

function validate(thisform, nextform) {
    console.log("Validating!");
    show(nextform, thisform);
    return false;
    //do stuff
}

function init() {
    console.log("Alright alright alright");
    //document.getElementById('page1').onsubmit = validate('FormPage1', 'FormPage2');
}
window.onload = init;
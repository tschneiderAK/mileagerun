function helloWorld(){
    console.log('Hello, world')
}

function checkCreditAirlines(){
    var partnersJSON = document.getElementById("partnersJSON");
    var partners = JSON.parse(partnersJSON);
    console.log('Air France:');
    console.log(partners.AF);

}
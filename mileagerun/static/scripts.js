async function updateFlown() {
    getFlownToCredited();
    getFareCodes();
    getFlightTypes();
}

async function updateCredit() {
    getFlightTypes();
}

async function getFlownToCredited() {
    let flown = document.getElementById('flown-airline-select');
    let credit = document.getElementById('credit-airline-select');
    
    let response = await fetch('data/flown-to-credited/' + flown.value);
    let flownToCreditJSON = await response.json();
    
    options = '';
    for (let result of flownToCreditJSON['credit airlines']) {
        options += '<option value="' + result[0] + '">' + result[1] + '</option>';

    credit.innerHTML = options;
    }
}

async function getCreditedToFlown() {
    let flown = document.getElementById('flown-airline-select');
    let credit = document.getElementById('credit-airline-select');
    
    let response = await fetch('data/credited-to-flown/' + credit.value);
    let creditToFlownJSON = await response.json();
    
    options = '';
    for (let result of creditToFlownJSON['operating airlines']) {
        options += '<option value="' + result + '">' + result + '</option>';

    flown.innerHTML = options;
    }
}

async function getFareCodes() {
    let flown = document.getElementById('flown-airline-select');

    if (flown.value) {
        let fareCode = document.getElementById('fare-code-select');
        let response = await fetch('data/fare-codes/' + flown.value);
        let fareCodesJSON = await response.json();
    
        options = '';
        for (let result of fareCodesJSON['codes']) {
            options += '<option value="' + result[0] + '">' + result[0] + '</option>';
    
        fareCode.innerHTML = options;
        }
    }
}

async function getFlightTypes() {
    let flown = document.getElementById('flown-airline-select');
    let credit = document.getElementById('credit-airline-select');

    if (flown.value && credit.value) {
        let flightType = document.getElementById('flight-type-select');
        let response = await fetch('data/flight-types/' + flown.value + '/' + credit.value);
        let flightTypeJSON = await response.json();
        
        options = '';
        for (let result of flightTypeJSON['flight types']) {
            options += '<option value="' + result[0] + '">' + result[1] + '</option>'; // Using result[0] and result[1] to allow for code descriptors in the future.
    
        flightType.innerHTML = options;
        }
    }
}

// Call bootstrap-autocomplete for the specified fields.

  $(document).ready(function(){
    $('.js-select2').select2();
      });

    $(document).ready(function(){
    $('#destination-select, #origin-select').select2();
        });
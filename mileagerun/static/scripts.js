async function updateFlown() {
    getFlownToCredited();
    getFareCodes();
}

async function getFlownToCredited() {
    let flown = document.getElementById('flown-airline-select');
    let credit = document.getElementById('credit-airline-select');
    
    let response = await fetch('data/flown-to-credited/' + flown.value);
    let flownToCreditJSON = await response.json();
    
    console.table(flownToCreditJSON)
    
    options = '';
    for (let result of flownToCreditJSON['credit airlines']) {
        options += '<option value="' + result + '">' + result + '</option>';

    credit.innerHTML = options;
    }
}

async function getCreditedToFlown() {
    let flown = document.getElementById('flown-airline-select');
    let credit = document.getElementById('credit-airline-select');
    
    let response = await fetch('data/credited-to-flown/' + credit.value);
    let creditToFlownJSON = await response.json();
    
    console.table(creditToFlownJSON)
    
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
    
        console.table(fareCodesJSON)
        
        options = '';
        for (let result of fareCodesJSON['codes']) {
            options += '<option value="' + result + '">' + result + '</option>';
    
        fareCode.innerHTML = options;
        }
    }
}

// Call bootstrap-autocomplete for the specified fields.

  $(document).ready(function(){
    $('.js-select2').select2();
      });
async function updateFlown() {
    getFlownToCredited();
    getFareCodes();
}

async function getFlownToCredited() {
    let flown = document.getElementById('flown-airline-select');
    let credit = document.getElementById('credit-airline-select');
    
    let response = await fetch('/flown-to-credited/' + flown.value);
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
    
    let response = await fetch('/credited-to-flown/' + credit.value);
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
        let response = await fetch('/fare-codes/' + flown.value);
        let fareCodesJSON = await response.json();
    
        console.table(fareCodesJSON)
        
        options = '';
        for (let result of fareCodesJSON['codes']) {
            options += '<option value="' + result + '">' + result + '</option>';
    
        fareCode.innerHTML = options;
        }
    }
}

// WTForms does not support passing the data-url property to form fields.
// This function will add this property once loaded.
// function addDataURL() {}
//     let url = 'aiports.json';
//     let field = document.getElementById('origin-select')
//     field.


  $(document).ready(function(){

    $('#origin-select').autoComplete({
        resolverSettings: {
            url: 'airports.json'
        }
    });
  });
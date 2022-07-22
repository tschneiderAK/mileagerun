async function updateFlown() {
    getFareCodes();
    getFlightTypes();
}

async function updateCredit() {
    getFlightTypes();
    getFlownOptions();
}

async function updateCreditOptions() {
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

async function getFlownOptions() {
    let flown = document.getElementById('flown-airline-select');
    let credit = document.getElementById('credit-airline-select');
    creditVal = credit.value;
    creditLabel = credit.label;

    if (flown.value) {
        tmp = flown.value
    }
    
    let response = await fetch('data/credited-to-flown/' + creditVal);
    let creditToFlownJSON = await response.json();
    
    options = "<optgroup label='" + creditVal + " Partner Airlines'>";
    for (let result of creditToFlownJSON['partner airlines']) {
        options += '<option value="' + result[0] + '">' + result[1] + '</option>';
    }
    options += "<optgroup label='Other Airlines (requires change in FF program)'>"
    for (let result of creditToFlownJSON['other airlines']) {
        options += '<option value="' + result[0] + '">' + result[1] + '</option>';
    }
    flown.innerHTML = options;
    flown.value = tmp
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
    
    $(document).on('select2:open', () => {
        document.querySelector('.select2-search__field').focus();
        });
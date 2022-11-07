// Calls various functions when the flown airline is changed.
async function updateFlown() {
    setFareCodes();
    setFlightTypes();
}

// Calls various functions when the credit airline is changed.
async function updateCredit() {
    setFlightTypes();
    setFlownOptions();
}

// When we change the flown airline, check if it can partner with the credit airline.
// Reset the credit airline if not.
async function checkPartnership() {
    let credit = document.getElementById('credit-airline-select');
    let flown = document.getElementById('flown-airline-select');
    console.log(credit.value)
    console.log(flown.value)
    if (credit.value) {
        let response = await fetch('data/credited-to-flown/' + credit.value);
        let creditToFlownJSON = await response.json();
        if (!(flown.value in creditToFlownJSON['partner airlines'][0])) {
            console.log('No partner match');
            $(document).ready(function(){
                $('#credit-airline-select').val(null).trigger('change')
            })
            console.log(document.getElementById('credit-airline-select').value);
        }
    }
}

async function setCreditOptions() {
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

async function setFlownOptions() {
    let flown = document.getElementById('flown-airline-select');
    let credit = document.getElementById('credit-airline-select');
    let tmp = null
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
    flown.innerHTML = options;
    if (tmp) {
        flown.value = tmp
    }
}


async function setFareCodes() {
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

async function setFlightTypes() {
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

// Sends a POST request to /calculate/ to get miles earned.

document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('basicSearchForm');
    form.addEventListener('submit', async function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        const data = await fetch('/calculate', {
                method: 'POST',
                body: formData,})
            .then(response => response.json())
        console.log(data)
        document.getElementById('distance_result').innerHTML = data['distance'];
        document.getElementById('eqm_result').innerHTML = data['eqm'];
        document.getElementById('eqd_result').innerHTML = data['eqd'];
        document.getElementById('rdm_result').innerHTML = data['rdm'];
        document.getElementById('calculation-results').hidden = false;
        })
    })

// Call select2 for the specified fields.

  $(document).ready(function(){
    $('.js-select2').select2();
      });

    $(document).ready(function(){
    $('#destination-select, #origin-select').select2();
        });
    
    $(document).on('select2:open', () => {
        document.querySelector('.select2-search__field').focus();
        });
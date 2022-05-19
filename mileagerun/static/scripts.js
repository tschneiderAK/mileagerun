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


$('.basicAutoComplete').autoComplete({
    resolverSettings: {
        url: '/airports.json'
    }
});
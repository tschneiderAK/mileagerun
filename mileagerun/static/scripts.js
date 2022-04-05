async function getPartners() {
    let flown = document.getElementById('flown-airline-select');
    let credit = document.getElementById('credit-airline-select');
    
    let response = await fetch('/partners/' + flown.value);
    let partnerJSON = await response.json();
    
    console.table(partnerJSON)
    
    options = '';
    for (let result of partnerJSON['credit airlines']) {
        options += '<option value="' + result + '">' + result + '</option>';

    credit.innerHTML = options;
    }
}
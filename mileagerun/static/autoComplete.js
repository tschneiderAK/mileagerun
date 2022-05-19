
			$(function () {
				// Basic
				$('.basicAutoComplete').autoComplete({
					resolverSettings: {
						url: 'https://raw.githack.com/xcash/bootstrap-autocomplete/master/dist/latest/testdata/test-list.json'
					}
				});

				$('.basicAutoComplete').on('change', function (e) {
					console.log('change');
				});

				$('.basicAutoComplete').on('autocomplete.select', function (evt, item) {
					$('.basicAutoCompleteSelected').html(JSON.stringify(item));
					$('.basicAutoCompleteCustom').html('');
				});

				$('.basicAutoComplete').on('autocomplete.freevalue', function (evt, value) {
					$('.basicAutoCompleteCustom').html(JSON.stringify(value));
					$('.basicAutoCompleteSelected').html('');
				});

				$('.basicAutoCompleteShowDropdown').autoComplete({
					minLength: 0,
				});

				$('.basicAutoCompleteShowBtn').on('click', function () {
					console.log('click');
					$('.basicAutoCompleteShowDropdown').autoComplete('show');
				});

				$('.basicAutoCompleteQParameter').autoComplete({
					resolverSettings: {
						url: 'testdata/test-list.json',
						queryKey: 'search'
					}
				});


				// Advanced 1
				$('.advancedAutoComplete').autoComplete({
					resolver: 'custom',
					events: {
						search: function (qry, callback) {
							// let's do a custom ajax call
							$.ajax(
								'testdata/test-dict.json',
								{
									data: { 'qry': qry}
								}
							).done(function (res) {
								callback(res.results)
							});
						}
					}
				});

				// Advanced 2
				$('.advanced2AutoComplete').autoComplete({
					resolver: 'custom',
					formatResult: function (item) {
						return {
							value: item.id,
							text: "[" + item.id + "] " + item.text,
							html: [ 
									$('<img>').attr('src', item.icon).css("height", 18), ' ',
									item.text 
								] 
						};
					},
					events: {
						search: function (qry, callback) {
							// let's do a custom ajax call
							$.ajax(
								'testdata/test-dict.json',
								{
									data: { 'qry': qry}
								}
							).done(function (res) {
								callback(res.results)
							});
						}
					}
				});

				// Basic Select
				$('.basicAutoSelect').autoComplete();
				$('.basicAutoSelect').on('autocomplete.select', function (evt, item) {
					console.log('select', item);
					$('.basicAutoSelectSelected').html(item?JSON.stringify(item):'null');

				});
				
				// Default Select
				$('.defaultAutoSelect').autoComplete();
				$('#dAS').on('autocomplete.select', function (e, i) {
					console.log('selected');
				});

				// Empty Select
				$('.emptyAutoSelect').autoComplete();
				
				// Modal
				$('.basicModalAutoSelect').autoComplete();
				$('.basicModalAutoSelect').on('autocomplete.select', function (evt, item) {
					console.log('select');
					$('.basicModalAutoSelectSelected').html(JSON.stringify(item));
				});

				// Change default value programmatically.
				// Let's simulate a real world example.
				// Some point in time we initialize the autocomplete with a default value (defined by markup)
				$('.changeAutoSelect').autoComplete();
				// user then clicks on some button and we need to change that default value
				$('.btnChangeAutoSelect').on('click', function () {
					var e = $(this);
					$('.changeAutoSelect').autoComplete('set', { value: e.data('value'), text: e.data('text')});
				});
				// clear current value
				$('.btnClearAutoSelect').on('click', function () {
					var e = $(this);
					// $('.changeAutoSelect').autoComplete('set', null);
					$('.changeAutoSelect').autoComplete('clear');

				});

				// Events
				var eventsCodeContainer = $('#eventsCodeContainer');
				
				$('.eventsAutoComplete').autoComplete({
					resolverSettings: {
						url: 'testdata/test-list.json'
					}
				});
				$('.eventsAutoComplete').on('change', function() {
					console.log('eventsAutoComplete change');
					eventsCodeContainer.text(eventsCodeContainer.text() + 'fired change. value: ' + $(this).val() + '\n');
				});
				$('.eventsAutoComplete').on('autocomplete.select', function(evt, item) {
					console.log('eventsAutoComplete autocomplete.select');
					eventsCodeContainer.text(eventsCodeContainer.text() + 'fired autocomplete.select. item: ' + item + ' value: ' + $(this).val() + '\n');
				});
				$('.eventsAutoComplete').on('autocomplete.freevalue', function(evt, item) {
					console.log('eventsAutoComplete autocomplete.freevalue');
					eventsCodeContainer.text(eventsCodeContainer.text() + 'fired autocomplete.freevalue. item: ' + item + ' value: ' + $(this).val() + '\n');
				});
			});
		
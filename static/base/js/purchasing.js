let a = 0;
function addAChild() {
	var div_col = document.createElement('div');
	var div_ig = document.createElement('div');
	var div_igp = document.createElement('div');
	var label_desc = document.createElement('label');
	var myText = document.createTextNode('Betrag');
	var input_desc = document.createElement('input');

	div_col.appendChild(div_ig);
	div_ig.appendChild(div_igp);
	div_igp.appendChild(label_desc);
	label_desc.appendChild(myText);
	div_ig.appendChild(input_desc);

	div_col.classList.add('col-4')
	div_ig.className = 'input-group my-4'
	div_igp.classList.add('input-group-prepend')
	label_desc.classList.add('input-group-text')
	input_desc.classList.add('form-control')
	input_desc.name = 'value_' + a

	var Ausgabebereich = document.getElementById('formGroup');
	Ausgabebereich.appendChild(div_col);
	a = a + 1
}

function init() {
	var element = document.getElementById('addPurchasing');
	element.addEventListener('click', addAChild);
}
document.addEventListener('DOMContentLoaded', init);
//onload = hint_create;
var th,tw,MaxUsageRead=0;
function hint_create(){
	var hint = document.createElement('div');
	hint.setAttribute('id','hint');
	var el1 = document.createElement('p');
	var el2 = document.createElement('b');
	el2.innerHTML = title;
	var el3 = document.createElement('a');
	el3.setAttribute('id','hint_close');
	el3.title = 'Close';
	el3.onclick = hint_hide;
	var el4 = document.createElement('p');
	el4.innerHTML = text;
	el1.appendChild(el2);
	el1.appendChild(el3);
	hint.appendChild(el1);
	hint.appendChild(el4);
	document.body.appendChild(hint);
	gag = document.createElement('div');
	gag.setAttribute('id','gag');
	document.body.appendChild(gag);
}
function hint_hide(){
	document.getElementById('gag').style.display = 'none';
	document.getElementById('hint').style.display = 'none';
}
function hint_show(){
	if(!document.getElementById('gag')) hint_create();
	document.getElementById('gag').style.display = 'block';
	document.getElementById('hint').style.display = 'block';
}
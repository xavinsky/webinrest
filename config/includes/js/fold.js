function fold(obj){
    obj.parentNode.childNodes[0].style.display='none';
    obj.parentNode.childNodes[1].style.display='block';
    obj.parentNode.childNodes[3].style.display='none';
    return false;
}

function unfold(obj){
    obj.parentNode.childNodes[0].style.display='block';
    obj.parentNode.childNodes[1].style.display='none';
    obj.parentNode.childNodes[3].style.display='block';
    return false;
}


fold_menu_state = 0;

function fold_menu(obj){
    base = obj.parentNode.parentNode.parentNode;
    div1 = base.childNodes[0].childNodes[0];
    img1 = div1.childNodes[0];
    lines = base.childNodes[1];
    if (fold_menu_state == 0) {
	lines.style.cssFloat='none';
	lines.style.position='absolute';
 	div1.style.left='0px';
 	div1.right='auto';
 	img1.src='/includes/images/unfold_menu.png';
 	lines.style.visibility='hidden';
	fold_menu_state = 1;
    } else {
	lines.style.cssFloat='left';
	lines.style.position='static';
 	div1.style.left='auto';
 	div1.right='0px';
 	img1.src='/includes/images/fold_menu.png';
 	lines.style.visibility='visible';
	fold_menu_state = 0;
    }
    return false;

}

function swap_lang(over_lang){
    obj = document.getElementById('lang__'+over_lang);
    tab = document.getElementById('tab_'+over_lang);
    divs = obj.parentNode.getElementsByTagName('div');
    for(var i= 0; i < divs.length; i++) {
	di = divs[i];
	if (di.id.substr(0,6) == 'lang__'){
	    di.style.display='none';
	}
	if (di.id.substr(0,4) == 'tab_'){
	    di.className= "tabinactive"; 
	}
    }
    tab.className= "tabactive"; 
    obj.style.display='block';
}

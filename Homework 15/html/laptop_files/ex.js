function msgbox(txt){
alert(txt);
}
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

function dmlPickEx(curex){
  var lb=document.frmN.N;
  var idx=lb.selectedIndex;
  var t=lb[idx].text;
  var page;
  var qpos=document.location.href.indexOf('?');
  var dpos=document.location.href.indexOf('#');

  var parpos=t.indexOf('(');
  var exNom=t.substr(0,parpos);
  if(dpos!=-1)
   page=document.location.href.substr(0,dpos);
  else if(qpos!=-1)
   page=document.location.href.substr(0,qpos);
  else page=document.location.href;

  document.location.href=page+"?N="+exNom;
}

function selPickEx(curex,second_stage,nneg)
{

  var lb=document.frmN.N;
  var idx=lb.selectedIndex;
  var t=lb[idx].text;
  var exn=idx-nneg+1;
  var page;
  var qpos=document.location.href.indexOf('?');
  var dpos=document.location.href.indexOf('#');
//
  var parpos=t.indexOf('(');
  var exNom=t.substr(0,parpos);
//
  if(dpos!=-1)
   page=document.location.href.substr(0,dpos);
  else if(qpos!=-1)
   page=document.location.href.substr(0,qpos);
  else page=document.location.href;
  if(t.indexOf('Ok')==-1 && t.indexOf('->')==-1)
  {
        if(exn==second_stage)
        {
          if(window.confirm(str_2stage))
          {
//                lb.selectedIndex=curex-1;
                document.location.href="/faq.php#ref_rating";
                return;
          }
        }
        if(exn>=second_stage)
        {
          if(!window.confirm(str_start1+exNom+str_start2))
          {
                lb.selectedIndex=curex-1;
                return;
          }
        }
  }
  document.location.href=page+"?N="+exNom+"&X=1"; //exn;
}
function learnSelPickEx(curex)
{
  var lb=document.frmN.LN;
  var idx=lb.selectedIndex;
  var t=lb[idx].text;
  var exn=idx+1;
  var page;
  var qpos=document.location.href.indexOf('?');
  var dpos=document.location.href.indexOf('#');
  var parpos=t.indexOf('(');
  var exNom=t.substr(0,parpos);
  if(dpos!=-1)
   page=document.location.href.substr(0,dpos);
  else if(qpos!=-1)
   page=document.location.href.substr(0,qpos);
  else page=document.location.href;

  if(t.indexOf('Ok')==-1 && t.indexOf('->')==-1)
  {

  }
  //document.location.href=page+"?N="+exn;
  document.location.href=page+"?LN="+exNom;
}

function ShowTrueRes()
{
   document.frmRes.txtsql.value = document.frmAnswer.txtsql.value;
   if (document.frmAnswer.CHB.checked) document.frmRes.CHB.value='1';
   else  document.frmRes.CHB.value='';

}

function Cls()
{
   if(window.confirm(str_clear))
    document.frmAnswer.txtsql.value="";
    document.frmAnswer.txtsql.focus();
}

function ResizeTextarea(mod)
{
  var otxt=document.getElementById("txtsql");
  var osel=document.getElementById("N");
  var yael=document.getElementById("yandex_rtb_R-A-184442-7");
  var yael1=document.getElementById("yandex_rtb_R-A-184442-1");
  

  if(otxt.style.position!="absolute" && mod==1) // to fullscreen
  {
    if(MaxUsageRead==0)
    {
      alert(str_maxhowto);
      MaxUsageRead=1;
    }
    th=otxt.style.height;
    tw=otxt.style.width;
    var h=document.body.clientHeight-55;
    var w=document.body.clientWidth-20;

    otxt.style.position="absolute";
    otxt.style.top="45px";
    otxt.style.left="10px";
    otxt.style.height=h+"px";
    otxt.style.width=w+"px";
//	otxt.style.zIndex="0";
    if(osel!=undefined)
    {
    osel.style.visibility="hidden";
    }
    if(yael!=undefined)
    {
    yael.style.visibility="hidden";
	yael1.style.visibility="hidden";
    }

  }else if(otxt.style.position=="absolute" && mod==0)
  { // to window mode
    otxt.style.position="";
    otxt.style.height=th;
    otxt.style.width=tw;
    if(osel!=undefined)
    {
    osel.style.visibility="visible";
    }
	if(yael!=undefined)
    {
    yael.style.visibility="visible";
	yael1.style.visibility="visible";
    }
  }
}

function CheckSelSyntax(s)
{
 var c1 = 0, c2 = 0;
 var pos;
 str=s;
 if (str.length>=8000)
 {
         alert(str_8000);
        frmAnswer.txtsql.focus();
        if (frmAnswer.wo.checked)
                return true;
        else
                return false;
 }
 var i=0;
 while(str.substr(i,1)==" " || str.charCodeAt(i)==9 || str.charCodeAt(i)==13 || str.charCodeAt(i)==10)
  i++;

 //if (frmAnswer.wo.checked)
//         {
         if(str.substr(i,6).toUpperCase()!='SELECT' && str.substr(i,4).toUpperCase()!='WITH'  && str.substr(i,5).toUpperCase()!=';WITH') // это не select и не with
         {
     alert(str_select+'.');
     document.frmAnswer.txtsql.focus();
     return false;
         }
//    }
/*
 else if(str.substr(i,6).toUpperCase()!='SELECT') // это не select
 {
     alert(str_select+'.');
     document.frmAnswer.txtsql.focus();
     return false;
 }
*/

 if(!(str.toUpperCase().indexOf('FROM')>0)){
     alert(str_from);
     frmAnswer.txtsql.focus();
     return false;
 }

 pos = str.indexOf('(');
 while(pos != -1){
       c1++;
       pos = str.indexOf('(',pos+1);
 }
 pos = str.indexOf(')');
 while(pos != -1){
       c2++;
       pos = str.indexOf(')',pos+1);
 }
 if (c1!=c2){ // Несоответствие скобок
        if(window.confirm(str_skobki))
          return true;
        document.frmAnswer.txtsql.focus();
        return false;
 }
 return true;
}// end CheckSelSyntax

function CheckSelSyntax3(s) //3 этап
{
 var c1 = 0, c2 = 0;
 var pos;
 str=s;
 if (str.length>=8000)
 {
         alert(str_8000);
        frmAnswer.txtsql.focus();
        if (frmAnswer.wo.checked)
                return true;
        else
                return false;
 }
 var i=0;
 while(str.substr(i,1)==" " || str.charCodeAt(i)==9 || str.charCodeAt(i)==13 || str.charCodeAt(i)==10)
  i++;
 if(str.substr(i,6).toUpperCase()!='SELECT' && str.substr(i,4).toUpperCase()!='WITH'  && str.substr(i,5).toUpperCase()!=';WITH') // это не select
 {
     alert(str_select+'.');
     document.frmAnswer.txtsql.focus();
     return false;
 }

 if(!(str.toUpperCase().indexOf('FROM')>0)){
     alert(str_from);
     frmAnswer.txtsql.focus();
     return false;
 }

 pos = str.indexOf('(');
 while(pos != -1){
       c1++;
       pos = str.indexOf('(',pos+1);
 }
 pos = str.indexOf(')');
 while(pos != -1){
       c2++;
       pos = str.indexOf(')',pos+1);
 }
 if (c1!=c2){ // Несоответствие скобок
        if(window.confirm(str_skobki))
          return true;
        document.frmAnswer.txtsql.focus();
        return false;
 }
 return true;
}// end CheckSelSyntax3

function CheckDmlSyntax(s)
{
 var c1 = 0, c2 = 0;
 var pos;
 str=s;
 if (str.length>=8000)
 {
         alert(str_8000);
        frmAnswer.txtsql.focus();
        if (frmAnswer.wo.checked)
                return true;
        else
                return false;
 }

 var i=0;
 while(str.substr(i,1)==" " || str.charCodeAt(i)==9 || str.charCodeAt(i)==13 || str.charCodeAt(i)==10)
  i++;
 var fw=str.substr(i,6).toUpperCase(), fw1=str.substr(i,4).toUpperCase() ; fw2=str.substr(i,5).toUpperCase() ;
 if (fw=='SELECT')
  document.frmAnswer.wo.checked=true;
 else if(  fw!='INSERT'        && fw!='UPDATE'        && fw!='DELETE'  && fw2!='MERGE'  && fw1!='WITH' && fw2!=';WITH' )
 {
        alert(str_select+',INSERT,UPDATE,DELETE,MERGE.');
        document.frmAnswer.txtsql.focus();
        return false;
 }
 pos = str.indexOf('(');
 while(pos != -1){
       c1++;
       pos = str.indexOf('(',pos+1);
 }
 pos = str.indexOf(')');
 while(pos != -1){
       c2++;
       pos = str.indexOf(')',pos+1);
 }
 if (c1!=c2){
        if(window.confirm(str_skobki))
          return true;
        document.frmAnswer.txtsql.focus();
        return false;
 }
 return true;
}// end CheckDmlSyntax

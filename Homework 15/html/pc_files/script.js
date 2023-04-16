// автодополнение
 onload = function(){if(document.getElementById('txtsql')!=null)document.getElementById('txtsql').focus();}
 var intelCode = ".DELETE.FROM.GROUP BY.HAVING.INSERT.ORDER BY.SELECT.UNION.UPDATE.WHERE.ASC.CASE.COALESCE.CONTAINS.CONVERT.CROSS JOIN.DESC.DISTINCT.END.FULL JOIN.INNER JOIN.INTO.JOIN.LEFT JOIN.OUTER.RIGHT JOIN.SET.TOP.VALUES.WITH.AND.BETWEEN.EXISTS.LIKE.NOT.NULL.NULLIF.PERCENT.SOME.THEN.WHEN.DATETIME.";
 var TableCode = ".Product.PC.Laptop.Printer.Income.Outcome.Income_o.Outcome_o.Classes.Ships.Outcomes.Battles.Trip.Pass_in_trip.Company.Passenger.utB.utQ.utV.";
 var colCode = ".maker.model.type.code.speed.ram.hd.price.screen.cd.color.class.country.numGuns.bore.displacement.launched.name.ship.battle.result.point.inc.out.B_Q_ID.B_V_ID.B_VOL.Q_ID.V_ID.V_COLOR.trip_no.ID_comp.plane.town_from.town_to.time_out.time_in.ID_psg.place.";

 var oPopup = window.createPopup;
 var position=0;
 var count_iter=0;

function onchanged()
{
 if (document.frmAnswer.CHB.checked){ //вернуть обратно, при выставлении на сайт
// if (document.all.CHB.checked){//убрать, при выставлении на сайт выставлять
 document.all.help_text.innerText = str_avto_yes;
 document.frmRes.CHB.value='1';//вернуть обратно, при выставлении на сайт
// document.frmAnswer.CHB.value='1';//убрать, при выставлении на сайт
          }
 else {document.all.help_text.innerText = str_avto;//'Автозамена (выключено)';
        document.frmRes.CHB.value='';////вернуть обратно, при выставлении на сайт
// document.frmAnswer.CHB.value='';//убрать, при выставлении на сайт
        }
}


function autorep()
{
  var key = window.event.keyCode;
  var Flag=0;

  if (window.event.ctrlKey && key == 32)
  {
    var rng = document.selection.createRange();
    rng.moveStart("word", -1);

    var str = rng.text.toUpperCase().replace(/\s*$/gi, "");

    var pind = intelCode.toUpperCase().indexOf("."+str);
    var pind1 = TableCode.toUpperCase().indexOf("."+str);
    var pind2 = colCode.toUpperCase().indexOf("."+str);
    var word;
    count_iter=count_iter+1;
    if (pind>=0 && str!="" && count_iter<=1)
    {
      word = intelCode.substring(pind+1, intelCode.indexOf(".", pind+1));
      rng.text = word + " ";
      Flag=1;
    }
    {
     if (pind1>=0 && str!="" && Flag==0 && count_iter<=1)
     {
       word = TableCode.substring(pind1+1, TableCode.indexOf(".", pind1+1));
       rng.text = word + " ";
       Flag=1;
     }
     if (pind2>=0 && str!="" && Flag==0 && count_iter<=1)
     {
       word = colCode.substring(pind2+1, colCode.indexOf(".", pind2+1));
       rng.text = word + " ";
     }
    }
    return true;
  }

  count_iter=0;
  oPopup.hide();

  //обрабатываем английские буквы
  if ((key >= 65 && key <= 90) || (key >= 97 && key <= 122))
  {
    var rng = document.selection.createRange();
    if (rng.text.length==0)
    {
      rng.moveStart("word", -1);
      var rect = rng.getBoundingClientRect();

      var lefter = rect.left+position;
      var topper = rect.bottom-30;

      var str = rng.text.toUpperCase();
      var pind = intelCode.toUpperCase().indexOf("."+str);
      var pind1 = TableCode.toUpperCase().indexOf("."+str);
      var pind2 = colCode.toUpperCase().indexOf("."+str);

      Flag=0;

      if (pind>=0 && str!="") //Всплывающая подсказка
      {
        oToolTip.all.oToolTipText.innerText = intelCode.substring(pind+1, intelCode.indexOf(".", pind+1));

        oPopup.document.body.style.backgroundColor = "#FF9";
        oPopup.document.body.innerHTML = oToolTip.innerHTML;
        oPopup.show(0, 0, 0, 0);
        var realHeight = oPopup.document.body.scrollHeight;
        var realWidth = oPopup.document.body.scrollWidth;
        oPopup.hide();
        position=position+4;
        oPopup.show(lefter, topper, realWidth, realHeight, document.body);

        Flag=1;
      }
      {
       if (pind1>=0 && str!="" && Flag==0) //Всплывающая подсказка
       {
         oToolTip.all.oToolTipText.innerText = TableCode.substring(pind1+1, TableCode.indexOf(".", pind1+1));

         oPopup.document.body.style.backgroundColor = "#0FA";
        oPopup.document.body.innerHTML = oToolTip.innerHTML;
        oPopup.show(0, 0, 0, 0);
        var realHeight = oPopup.document.body.scrollHeight;
        var realWidth = oPopup.document.body.scrollWidth;
        oPopup.hide();
        position=position+4;
        oPopup.show(lefter, topper, realWidth, realHeight, document.body);

         Flag=1;
       }

       if (pind2>=0 && str!="" && Flag==0) //Всплывающая подсказка
       {
         oToolTip.all.oToolTipText.innerText = colCode.substring(pind2+1, colCode.indexOf(".", pind2+1));

        oPopup.document.body.style.backgroundColor = "#CFF";
        oPopup.document.body.innerHTML = oToolTip.innerHTML;
        oPopup.show(0, 0, 0, 0);
        var realHeight = oPopup.document.body.scrollHeight;
        var realWidth = oPopup.document.body.scrollWidth;
        oPopup.hide();
        position=position+4;
        oPopup.show(lefter, topper, realWidth, realHeight, document.body);

       }
      }
    }
  }
  else
  {
   position=0;
  }
  return true;
}
		function TabFunc(ev,s,stg){
			key = ev.keyCode ? ev.keyCode : ev.which;
			if (ev.ctrlKey && ev.shiftKey && key == 32){
				if(document.selection){
					var fortab = document.selection.createRange();
					fortab.text = "\t";
				}
				else{
					obj = document.getElementById('txtsql');
					start = obj.selectionStart;
					end = obj.selectionEnd;
					p1 = obj.value.substr(0,start);
					p2 = obj.value.substr(end,obj.value.length);
					obj.value = p1 + "\t" + p2;
					obj.selectionStart = obj.selectionEnd = start+1;
				}
			}
			else if(ev.ctrlKey && key == 13){
             str=s;  //alert(stg);
			 if ((stg==3) ? !CheckSelSyntax3(str) : !CheckSelSyntax(str)) return false;
			 else    document.forms['frmAnswer'].submit()
            }
		}



		function TabFuncDML(ev){
			key = ev.keyCode ? ev.keyCode : ev.which;
			if (ev.ctrlKey && ev.shiftKey && key == 32){
				if(document.selection){
					var fortab = document.selection.createRange();
					fortab.text = "\t";
				}
				else{
					obj = document.getElementById('txtsql');
					start = obj.selectionStart;
					end = obj.selectionEnd;
					p1 = obj.value.substr(0,start);
					p2 = obj.value.substr(end,obj.value.length);
					obj.value = p1 + "\t" + p2;
					obj.selectionStart = obj.selectionEnd = start+1;
				}
			}
			else if(ev.ctrlKey && key == 13) document.forms['frmAnswer'].submit();
		}
        
/*
function TabFunc(){
  if (window.event.ctrlKey && window.event.shiftKey && window.event.keyCode == 84){
  var fortab = document.selection.createRange();
  fortab.text = "\t";
  }
  else if(window.event.ctrlKey && window.event.keyCode == 13){
  document.forms['frmAnswer'].submit();
  }
}

function TabFunc()
{
  var fortab = document.selection.createRange();

  if (window.event.ctrlKey && window.event.keyCode == 9)
  {
   fortab.text = "\t";
   fortab.collapse(false);
   return false;
  };
  return true;
}
*/
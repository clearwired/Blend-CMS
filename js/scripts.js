//clear input field onFocus
function clearDefault(el) {
  if (el.defaultValue==el.value) el.value = ""
}

//confirm delete object
function confirmSubmit()
{
var agree=confirm("Please confirm delete.");
if (agree)
	return true ;
else
	return false ;
}

function popUp(URL) {
day = new Date();
id = day.getTime();
eval("page" + id + " = window.open(URL, '" + id + "', 'toolbar=0,scrollbars=0,location=0,statusbar=0,menubar=0,resizable=0,width=350,height=250,left = 490,top = 412');");
}
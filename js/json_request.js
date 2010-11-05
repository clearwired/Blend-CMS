// create JSON request object
jsonRequestor = function (statusObject) {
	// assume this ain't gonna work until proven otherwise
	this.canDoRequests = false;
	
	// test whether the browser can handle XMLHttpRequest
	if (window.XMLHttpRequest) {	// Mozilla, Safari, et al.
		reqObj = new XMLHttpRequest();
	} else if (document.all) {		// IE
		reqObj = new ActiveXObject('Microsoft.XMLHTTP');
	}

	// if we have a request object to work with, set up the methods
	if (reqObj) {
		this.canDoRequests	= true;
		this.makeRequest	= makeRequest;
	} else {
		handleStatusMessage('error_bad_browser');
	}
	
	return this;
}

// send the request to the server
makeRequest = function (uri,content,async) {
	if (async == undefined) async = true;

	// set-up request object
	if (window.XMLHttpRequest) {	// Mozilla, Safari, et al.
		reqObj = new XMLHttpRequest();
	} else if (document.all) {		// IE
		reqObj = new ActiveXObject('Microsoft.XMLHTTP');
	}

	handleStatusMessage('working'); // external to this file
	
	reqObj.onreadystatechange = processRequestChange;
	reqObj.open('POST',uri,async);
	reqObj.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
	reqObj.send(content); // content = 'var1=data1&var2=data2'
}

// watch for OK state
processRequestChange = function () {
	if (null == reqObj.readyState) return;
	if (reqObj.readyState == 4) {
		if (reqObj.status == 200) {		
			processResult(); // external to this file
		} else {
			if (null == reqObj.status) return;
			handleStatusMessage('error_noconnection'); // external to this file
		}
	}
}

// show the status message
setStatusMessage = function (statusObject, statusCode) {
	statusObject.innerHTML = statusMessages[statusCode];
}

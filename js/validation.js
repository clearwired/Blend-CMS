/*

JavaScript Form Validation Library, 1.1
Andrew Hedges, andrew@clearwired.com
2006-07-23

*/

// test for an empty string
// s = subject str
isNotEmpty = function (s) {
	return (s.length > 0);
}

// test whether the string matches the pattern passed in
// s = subject str, p = pattern
containsMatch = function (s, p) {
	pattern = new RegExp(p);
	return pattern.test(s);
}

// test whether the first letter of the string is capitalized
// s = subject str
isCapped = function (s) {
	for (var l = 0; l < s.length; l++) {
		if (patterns['caps'].test(s.substring(l, l+1))) return true;
	}
	return false;
}

// test whether the first letter of the string is capitalized
// s = subject str
isCappedFirst = function (s) {
	var l = s.substring(0, 1);
	return patterns['caps'].test(l);
}

// test whether a string is a minimum length
// s = subject str, l = target length int
isLongEnough = function (s,l) {
	return (s.length >= l);
}

// test whether a string does not exceed a maximum length
// s = subject str, l = target length int
isNotTooLong = function (s,l) {
	return (s.length <= l);
}

// test whether a string is only letters (no numbers, spaces or punctuation)
// s = subject str
isAlpha = function(s) {
	return patterns['alpha'].test(s);
}

// test whether a string is a valid number (either integer or float, positive or negative)
// s = subject str
isNumeric = function(s) {
	return patterns['numeric'].test(s);
}

// test whether the string is only numbers (no letters, spaces or punctuation)
// s = subject str
isAllNumbers = function(s) {
	return patterns['numbers'].test(s);
}

// test whether the string is only numbers and letters (no spaces or punctuation)
// s = subject str
isAlphaNumeric = function(s) {
	return patterns['alphanumeric'].test(s);
}

// test whether the string is a valid date and/or time
// s = subject str
isDateTime = function(s) {
//	return ;
}

// test whether the string is a valid US ZIP code
// s = subject str
isUSZIP = function(s) {
	return patterns['uszip'].test(s);
}

// test whether a string is a valid Social Security Number
// s = subject str
isSSN = function(s) {
	s.replace(/(-|\s)g/,''); // strip any dashes or spaces
	if (!isAllNumbers(s))	return false; // make sure the string is all numbers
	if (s.length > 9)		return false; // if it's longer than 9 characters, it's not a SSN
	var p = s.substring(0,3) * 1; // get the first three numbers, convert to a number
	if (p == 0)		return false; // valid prefixes are: 001 - 665 and 667 - 772
	if (p == 666)	return false;
	if (p > 772)	return false;
	return true; // if none of the above triggered, it must be valid
}

// test whether the string is only numbers, letters, - (dash) and _ (underscore)
// s = subject str
isValidUsername = function(s) {
	return patterns['username'].test(s);
}

// test whether the string contains quote marks (either ' or ") (used for passwords)
// s = subject str
noQuotes = function(s) {
	return patterns['quotes'].test(s);
}

// test whether two strings are identical
// s = subject str
areIdentical = function(s1,s2) {
	return (s1 === s2);
}

// test whether two strings have the same value and type
// s = subject str
areTheSame = function(s1,s2) {
	return (s1 == s2);
}

// test whether two numeric arrays contain the same set of values
// a1 = first array, a2 = second array
areIdenticalArrays = function (a1, a2) {
	a1.sort();
	a2.sort();
	return a1.toString() == a2.toString();
}

// test whether the string is a valid URL (ignores file names, directories, and query strings)
// s = subject str
isURL = function(s) {
	// works for TLDs up to 6 characters (e.g., .museum)
	return patterns['url'].test(s);
}

// test whether the string is one valid email address
// s = subject str
isEmail = function(s) {
	return patterns['email'].test(s);
}

// test whether the string contains at least one valid email address
// s = subject str
areEmails = function(s) {
	s.replace(/\s/g,''); // remove any spaces
	var e = s.split(','); // split on commas in case we have multiple email addresses
	var is_email = true; // default to valid email
	for (var i = 0; i < e.length; i++) { // loop through the addresses
		if (!patterns['email'].test(e[i])) {
			is_email = false;
			break;
		}
	}
	return is_email;
}

// check whether a radio button is checked
// r = radio button collection obj
isChecked = function(r) {
	var chckd = false;
	if (r.length === undefined) {
		if (r.checked) chckd = false;
	} else {
		for (var i = r.length-1; i > -1; i--) {
			if (r[i].checked) {
				chckd = true;
				break;
			}
		}
	}
	return chckd;
}

/*

// test whether 
// s = subject str
funcName = function (s) {
	var pattern = //;
	return pattern.test(s);
}
*/

var patterns = new Array();
patterns['alpha']			= /^[a-zA-Z]*$/;
patterns['caps']			= /^[A-Z]*$/;
patterns['numeric']			= /^[0-9\.\-]*$/;
patterns['numbers']			= /^[0-9]*$/;
patterns["alphanumeric"]	= /^[a-zA-Z0-9]*$/;
patterns['uszip']			= /^[0-9]{5}(-[0-9]{4})?$/;
patterns['username']		= /^[a-zA-Z0-9\-_]*$/;
patterns['quotes']			= /(\"|\')?/;
patterns['url']				= /^(http:\/\/|https:\/\/|ftp:\/\/)[a-zA-Z0-9\-_]+(\.?[a-zA-Z0-9\-_]*)\.[a-zA-Z]{2,6}/;
patterns['email']			= /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,6}))$/;

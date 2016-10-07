var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

function get(){
	var xhr = new XMLHttpRequest();
	xhr.open("GET", 'http://jsonplaceholder.typicode.com/posts/100', true);
	xhr.responseType = "arraybuffer";
	xhr.onload = function(e) {
	  console.log(xhr);
	  console.log(xhr.responseText);
	}
	xhr.send();
}

function post(){
	var xhr = new XMLHttpRequest();
	xhr.open("POST", 'http://jsonplaceholder.typicode.com/posts', true);
	var data = {title: 'Foo', body:'Bar', userId:'1'};
	xhr.onload = function(e) {
	  console.log("\n\n"+JSON.stringify(xhr));
	  console.log(xhr.responseText);
	}
	xhr.send(JSON.stringify(data));
}

function put(){
	var xhr = new XMLHttpRequest();
	xhr.open("PUT", 'http://jsonplaceholder.typicode.com/posts/1', true);
	var data = {id: '1', title: 'Foo', body:'Bar', userId:'1'};
	xhr.onload = function(e) {
	  console.log("\n\n"+JSON.stringify(xhr));
	  console.log(xhr.responseText);
	}
	xhr.send(JSON.stringify(data));
}

function deleta(){
	var xhr = new XMLHttpRequest();
	xhr.open("DELETE", 'http://jsonplaceholder.typicode.com/posts/1', true);
	xhr.onload = function(e) {
	  console.log("\n\n"+JSON.stringify(xhr));
	  console.log(xhr.responseText);
	}
	xhr.send();
}

get();

post();

put();

deleta();

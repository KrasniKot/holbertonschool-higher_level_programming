async function disHello() {
	let request = await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr");
	let translello = await request.json();

	let nodep = document.createElement("p");
	nodep.appendChild(document.createTextNode(translello.hello));
	console.log(translello.hello);

	document.querySelector("#hello").appendChild(nodep);
};

disHello();

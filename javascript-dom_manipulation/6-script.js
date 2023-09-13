async function gC() {
	const response = await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json");
	const character = await response.json();

	let nodep = document.createElement("p");
	nodep.appendChild(document.createTextNode(character.name));
	window.alert(character.name);
	document.querySelector("#character").appendChild(nodep);
};

gC();

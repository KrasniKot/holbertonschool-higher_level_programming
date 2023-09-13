async function SWM() {
	let request = await fetch("https://swapi-api.hbtn.io/api/films/?format=json");
	let mvs = await request.json();

	for (let mv of mvs.results) {
		nodeli = document.createElement("li");
		nodeli.appendChild(document.createTextNode(mv.title));

		document.querySelector("#list_movies").appendChild(nodeli);
	};
};

SWM();

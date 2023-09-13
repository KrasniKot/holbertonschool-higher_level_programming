document.querySelector("#add_item").onclick = function() {
	let node = document.createElement("li");
	node.appendChild(document.createTextNode("item"));
	document.querySelector(".my_list").appendChild(node);
};

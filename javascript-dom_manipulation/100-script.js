document.addEventListener("DOMContentLoaded", function() {

	document.querySelector("#add_item").onclick = function() {
        	let node = document.createElement("li");
	        node.appendChild(document.createTextNode("item"));
        	document.querySelector(".my_list").appendChild(node);
	};

	document.querySelector("#remove_item").onclick = function() {
		let list = document.querySelector(".my_list");
		list.removeChild(list.lastChild);
	};

	document.querySelector("#clear_list").onclick = function() {
		let list = document.querySelector(".my_list");
		list.innerHTML = "";
	};
});


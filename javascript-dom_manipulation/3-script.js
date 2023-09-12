document.querySelector("#toggle_header").onclick = function (){
	para = document.querySelector("header");
	if (para.classList.contains("red")) {
	para.classList.replace("red", "green");
	} else {
	para.classList.replace("green", "red");
	}
};

function toggleClass() {
	header = document.querySelector("header");
	header.classList.toggle("green");
	header.classList.toggle("red");
}
let toggle_header = document.querySelector("#toggle_header");
toggle_header.addEventListener("click", toggleClass);

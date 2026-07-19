function update_header() {
	let header = document.querySelector("header");
	header.textContent = "New Header!!!";
}
let header = document.querySelector("#update_header");
header.addEventListener("click", update_header);

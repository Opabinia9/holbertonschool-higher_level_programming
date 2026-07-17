function addItem() {
	let ul = document.getElementsByClassName("my_list")[0];
	let li = document.createElement("li");
	let text = document.createTextNode("Item");
	li.appendChild(text);
	ul.appendChild(li);
}
let add_item = document.querySelector("#add_item");
add_item.addEventListener("click", addItem);

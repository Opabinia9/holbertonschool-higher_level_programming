async function setName() {
	let character = document.querySelector("#character");
	character.textContent = await fetch(
		"https://swapi-api.hbtn.io/api/people/5/?format=json",
	)
		.then((response) => response.json())
		.then((json) => json["name"])
		.catch((error) => console.log(error));
}
setName();

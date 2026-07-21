async function listMovies() {
	console.log(Date());
	const movieList = document.querySelector("#list_movies");
	try {
		const response = await fetch(
			"https://swapi-api.hbtn.io/api/films/?format=json",
		);
		const data = await response.json();
		const movies = data.results;
		console.log(movies);
		for (let movie of movies) {
			let movieitem = document.createElement("li");
			movieitem.textContent = movie.title;
			movieList?.appendChild(movieitem);
		}
	} catch {}
}
listMovies();

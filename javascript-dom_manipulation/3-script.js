function toggleClass() {
	let header = document.querySelector('header');
	header.classList.toggle('green');
	header.classList.toggle('red');
}
document.querySelector('#toggle_header').addEventListener('click', toggleClass);

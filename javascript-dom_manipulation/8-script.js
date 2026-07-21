async function sayHello() {
	console.log(Date());
	const hello = document.querySelector('#hello');
	try {
		const response = await fetch(
			'https://hellosalut.stefanbohacek.com/?lang=fr',
		);
		const data = await response.json();
		hello.textContent = data.hello;
	} catch {}
}
document.addEventListener('DOMContentLoaded', sayHello);

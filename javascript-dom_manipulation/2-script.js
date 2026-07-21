function addredclass() {}
document
	.querySelector('#red_header')
	.addEventListener(
		'click',
		() => (document.querySelector('header').classList += 'red'),
	);

document.addEventListener('DOMContentLoaded', function() {

	const btn = document.querySelector('#btn_translate');

	btn.onclick = function() {
		const lang = document.querySelector('#language_code').querySelector('option:checked');
		fetch(`https:\/\/hellosalut.stefanbohacek.dev/?lang=${lang.value}`)
		.then(function(response) {
			return response.json()
		})
		.then(function(data) {
			document.querySelector('#hello').textContent = data.hello
		});
	};
});

const addCat = async (data) => {
	const request = await fetch('localhost:5000/cats/add-cat', {
		method: 'POST',
		headers: { 'content-type': 'application/json' },
		body: data,
	});
	return request;
};

const el = document.getElementById('form')

el.addEventListener('submit', (e) => {
    e.preventDefault()
    console.log('POST')
    const formData = new FormData(el);
    const values = [...formData.entries()];
    console.log(values)
    addCat(values)
})
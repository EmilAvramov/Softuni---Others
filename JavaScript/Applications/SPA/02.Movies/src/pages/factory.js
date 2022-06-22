function createElement(
	tag,
	cls = '',
	txt = '',
	src = '',
	width = '',
	href = '',
	type = ''
) {
	const el = document.createElement(tag);
	if (cls) {
		el.classList.add(cls);
	}
	if (txt) {
		el.textContent = txt;
	}
	if (src) {
		el.src = src;
	}
	if (width) {
		el.width = width;
	}
	if (href) {
		el.href = href;
	}
	if (type) {
		el.type = type;
	}
	return el;
}

const movieParent = document.querySelector(
	'.card-deck d-flex justify-content-center'
);

export function movieCard(obj) {
	movieParent.innerHTML = '';
	const divContainer = createElement('div', 'container');
	const divSubC = createElement('div', 'row bg-light text-dark');

	const h1 = createElement('h1', '', `${obj.title}`);
	divSubC.appendChild(h1);

	const divSubCSub1 = createElement('div', 'col-md-8"');
	const img = createElement('img', 'img-thumbnail', '', `${obj.imageUrl}`);
	divSubCSub1.appendChild(img);
	divSubC.appendChild(divSubCSub1);

	const divSubCSub2 = createElement('div', 'col-md-4 text-center"');
	const h3 = createElement('h3', 'my-3', 'Movie Description');
	const p = createElement('p', '', `${obj.description}`);
	const l1 = createElement('a', 'btn btn-danger', 'Delete', '', '', '#');
	const l2 = createElement('a', 'btn btn-warning', 'Edit', '', '', '#');
	const l3 = createElement('a', 'btn btn-primary', 'Like', '', '', '#');
	const span = createElement('span', 'enrolled-span', 'Liked 1');
	divSubCSub2.appendChild(h3);
	divSubCSub2.appendChild(p);
	divSubCSub2.appendChild(l1);
	divSubCSub2.appendChild(l2);
	divSubCSub2.appendChild(l3);
	divSubCSub2.appendChild(span);
	divSubC.appendChild(divSubCSub2);

	divContainer.appendChild(divSubC);
	movieParent.appendChild(divContainer);
}

export function movieList() {}

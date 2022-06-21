async function getRecipes() {
	const response = await fetch(
		'http://localhost:3030/jsonstore/cookbook/recipes'
	);
	const recipes = await response.json();

	return Object.values(recipes);
}

async function getRecipeById(id) {
	const response = await fetch(
		`http://localhost:3030/jsonstore/cookbook/details/${id}`
	);
	const recipe = await response.json();

	return recipe;
}

function e(type, attributes, ...content) {
	const result = document.createElement(type);

	// eslint-disable-next-line no-restricted-syntax
	for (const [attr, value] of Object.entries(attributes || {})) {
		if (attr.substring(0, 2) === 'on') {
			result.addEventListener(
				attr.substring(2).toLocaleLowerCase(),
				value
			);
		} else {
			result[attr] = value;
		}
	}

	// eslint-disable-next-line no-param-reassign
	content = content.reduce(
		(a, c) => a.concat(Array.isArray(c) ? c : [c]),
		[]
	);

	content.forEach((ev) => {
		if (typeof ev === 'string' || typeof ev === 'number') {
			const node = document.createTextNode(ev);
			result.appendChild(node);
		} else {
			result.appendChild(ev);
		}
	});

	return result;
}

function createRecipeCard(recipe) {
	const result = e(
		'article',
		{},
		e('h2', {}, recipe.name),
		e(
			'div',
			{ className: 'band' },
			e('div', { className: 'thumb' }, e('img', { src: recipe.img })),
			e(
				'div',
				{ className: 'ingredients' },
				e('h3', {}, 'Ingredients:'),
				e(
					'ul',
					{},
					recipe.ingredients.map((i) => e('li', {}, i))
				)
			)
		),
		e(
			'div',
			{ className: 'description' },
			e('h3', {}, 'Preparation:'),
			recipe.steps.map((s) => e('p', {}, s))
		)
	);

	return result;
}

function createRecipePreview(recipe) {
	async function toggleCard() {
		// eslint-disable-next-line no-underscore-dangle
		const fullRecipe = await getRecipeById(recipe._id);

		// eslint-disable-next-line no-use-before-define
		result.replaceWith(createRecipeCard(fullRecipe));
	}
	const result = e(
		'article',
		{ className: 'preview', onClick: toggleCard },
		e('div', { className: 'title' }, e('h2', {}, recipe.name)),
		e('div', { className: 'small' }, e('img', { src: recipe.img }))
	);

	return result;
}

window.addEventListener('load', async () => {
	if (localStorage.email) {
		const logged = document.getElementById('user');
		logged.style.display = 'block';

		const logOut = document.getElementById('logoutBtn');
		logOut.addEventListener('click', () => {
			localStorage.clear();
			// eslint-disable-next-line no-restricted-globals
			location.reload();
		});
	} else {
		const guest = document.getElementById('guest');
		guest.style.display = 'block';
	}
	const main = document.querySelector('main');

	const recipes = await getRecipes();
	const cards = recipes.map(createRecipePreview);

	main.innerHTML = '';
	cards.forEach((c) => main.appendChild(c));
});

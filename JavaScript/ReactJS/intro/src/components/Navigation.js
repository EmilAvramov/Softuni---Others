export const Navigation = () => {
	return (
		<div id='header'>
			{' '}
			<a href='#' id='logo'>
				<img src='images/logo.gif' width='310' height='114' alt='' />
			</a>
			<ul className='navigation'>
				<li className='active'>
					<a href='index.html'>Home</a>
				</li>
				<li>
					<a href='petmart.html'>PetMart</a>
				</li>
				<li>
					<a href='about.html'>About us</a>
				</li>
				<li>
					<a href='blog.html'>Blog</a>
				</li>
				<li>
					<a href='petguide.html'>PetGuide</a>
				</li>
				<li>
					<a href='contact.html'>Contact us</a>
				</li>
			</ul>
		</div>
	);
};

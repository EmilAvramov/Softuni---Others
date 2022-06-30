import React from 'react';
import ReactDOM from 'react-dom/client';
import { Navigation } from './components/Navigation';
import { Main } from './components/Main';
import { Footer } from './components/Footer';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
	<React.StrictMode>
		<Navigation />
		<Main />
		<Footer />
	</React.StrictMode>
);

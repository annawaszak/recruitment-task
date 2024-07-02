import React from 'react';
import './App.css';
import Gallery from './components/Gallery';
import Modal from 'react-modal';


Modal.setAppElement('#root');  // Set the app element for accessibility

function App() {
	return (
		<div className="App">
			<Gallery />
		</div>
	);
}

export default App;

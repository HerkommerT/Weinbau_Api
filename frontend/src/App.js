// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import { Button } from 'primereact/button';
import 'primereact/resources/themes/saga-blue/theme.css';
import 'primereact/resources/primereact.min.css';

// Beispiel-Komponenten
const Home = () => (
    <div>
        <h1>Home Page</h1>
        <Link to="/menu">
            <Button label="Go to Menu" />
        </Link>
    </div>
);

const Menu = () => (
    <div>
        <h1>Menu Page</h1>
        <Link to="/">
            <Button label="Go to Home" />
        </Link>
    </div>
);

function App() {
    return (
        <Router>
            <div className="App">
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/menu" element={<Menu />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import 'primereact/resources/themes/saga-blue/theme.css';
import 'primereact/resources/primereact.min.css';
import 'primeicons/primeicons.css';
import Home from './components/Home';
import Wein from './components/Wein';
import Login from './components/PrivateLogin';

function App() {
    return (
        <Router>
            <div className="App">
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/wein" element={<Wein />} />
                    <Route path="/finanzen" element={<Login />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;

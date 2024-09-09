import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import { Button } from 'primereact/button';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
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

const Menu = () => {
    const [weingueter, setWeingueter] = useState([]);

    // useEffect wird verwendet, um die Daten beim Laden der Komponente zu holen
    useEffect(() => {
        // GET-Anfrage an die Flask-API mit fetch, um die Weingut-Daten zu erhalten
        fetch('http://127.0.0.1:5000/get_weingut')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Die erhaltenen Daten werden im Zustand gespeichert
                setWeingueter(data);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    }, []); // Der leere Array sorgt dafür, dass die Anfrage nur einmal bei der Montage ausgeführt wird

    return (
        <div>
            <h1>Menu Page</h1>
            {/* Anzeige der Daten in einer DataTable */}
            <DataTable value={weingueter}>
                <Column field="weingut_id" header="Weingut ID"></Column>
                <Column field="land" header="Land"></Column>
            </DataTable>
            <Link to="/">
                <Button label="Go to Home" />
            </Link>
        </div>
    );
};

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

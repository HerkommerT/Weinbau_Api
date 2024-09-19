import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import { Button } from 'primereact/button';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { Dialog } from 'primereact/dialog';
import { Toolbar } from 'primereact/toolbar';
import 'primereact/resources/themes/saga-blue/theme.css';
import 'primereact/resources/primereact.min.css';
import 'primeicons/primeicons.css';

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
    const [wein, setWeingueter] = useState([]);
    const [dialogVisible, setDialogVisible] = useState(false);
    const [newWein, setNewWein] = useState({
        name: '',
        beschr: '',
        preis: '',
        weingut_id: '',
        typ_id: '',
        art_id: ''
    });

    // Funktion zum Abrufen der Weine
    const fetchWeinList = () => {
        fetch('http://127.0.0.1:5000/wein')
            .then(response => response.json())
            .then(data => setWeingueter(data))
            .catch(error => console.error('Error fetching wine list:', error));
    };

    // useEffect wird verwendet, um die Daten beim Laden der Komponente zu holen
    useEffect(() => {
        fetchWeinList(); // Initiales Laden der Weine
    }, []);

    const handleDialogClose = () => {
        setDialogVisible(false);
    };

    const handleDialogOpen = () => {
        setDialogVisible(true);
    };

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setNewWein({
            ...newWein,
            [name]: value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch('http://127.0.0.1:5000/wein', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(newWein)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(() => {
            fetchWeinList();  // Nach dem POST, nochmal die Weine neu laden
            handleDialogClose();
        })
        .catch(error => console.error('There was a problem with the fetch operation:', error));
    };

    const startToolbarTemplate = () => {
        return (
            <Button label="Add Wein" icon="pi pi-plus" onClick={handleDialogOpen} className="p-button-success" />
        );
    };

    return (
        <div>
            <h1>Menu Page</h1>
            <Toolbar start={startToolbarTemplate} />

            <DataTable value={wein}>
                <Column field="wein_id" header="Wein ID" />
                <Column field="name" header="Name" />
                <Column field="beschr" header="Beschreibung" />
                <Column field="preis" header="Preis" />
                <Column field="weingut_id" header="Weingut ID" />
                <Column field="typ_id" header="Typ ID" />
                <Column field="art_id" header="Art ID" />
            </DataTable>

            <Dialog 
                header="Add New Wein" 
                visible={dialogVisible} 
                style={{ width: '50vw' }} 
                footer={
                    <div>
                        <Button type="submit" form="weinForm" label="Submit" className="p-button-success" />
                        <Button label="Close" icon="pi pi-times" onClick={handleDialogClose} className="p-button-secondary" />
                    </div>
                }
                onHide={handleDialogClose}
            >
                <form id="weinForm" onSubmit={handleSubmit}>
                    <div className="p-fluid">
                        <div className="p-field" style={{ display: 'flex', alignItems: 'center', marginBottom: '1rem' }}>
                            <label htmlFor="name" style={{ marginRight: '1rem', width: '150px' }}>Name</label>
                            <input id="name" name="name" value={newWein.name} onChange={handleInputChange} className="p-inputtext p-component" style={{ flex: 1 }} />
                        </div>
                        
                        <div className="p-field" style={{ display: 'flex', alignItems: 'center', marginBottom: '1rem' }}>
                            <label htmlFor="beschr" style={{ marginRight: '1rem', width: '150px' }}>Beschreibung</label>
                            <input id="beschr" name="beschr" value={newWein.beschr} onChange={handleInputChange} className="p-inputtext p-component" style={{ flex: 1 }} />
                        </div>

                        <div className="p-field" style={{ display: 'flex', alignItems: 'center', marginBottom: '1rem' }}>
                            <label htmlFor="preis" style={{ marginRight: '1rem', width: '150px' }}>Preis</label>
                            <input id="preis" name="preis" value={newWein.preis} onChange={handleInputChange} className="p-inputtext p-component" style={{ flex: 1 }} />
                        </div>

                        <div className="p-field" style={{ display: 'flex', alignItems: 'center', marginBottom: '1rem' }}>
                            <label htmlFor="weingut_id" style={{ marginRight: '1rem', width: '150px' }}>Weingut ID</label>
                            <input id="weingut_id" name="weingut_id" value={newWein.weingut_id} onChange={handleInputChange} className="p-inputtext p-component" style={{ flex: 1 }} />
                        </div>

                        <div className="p-field" style={{ display: 'flex', alignItems: 'center', marginBottom: '1rem' }}>
                            <label htmlFor="typ_id" style={{ marginRight: '1rem', width: '150px' }}>Typ ID</label>
                            <input id="typ_id" name="typ_id" value={newWein.typ_id} onChange={handleInputChange} className="p-inputtext p-component" style={{ flex: 1 }} />
                        </div>

                        <div className="p-field" style={{ display: 'flex', alignItems: 'center', marginBottom: '1rem' }}>
                            <label htmlFor="art_id" style={{ marginRight: '1rem', width: '150px' }}>Art ID</label>
                            <input id="art_id" name="art_id" value={newWein.art_id} onChange={handleInputChange} className="p-inputtext p-component" style={{ flex: 1 }} />
                        </div>
                    </div>
                </form>
            </Dialog>

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

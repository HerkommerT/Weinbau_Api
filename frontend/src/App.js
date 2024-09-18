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

    // useEffect wird verwendet, um die Daten beim Laden der Komponente zu holen
    useEffect(() => {
        fetch('http://127.0.0.1:5000/wein')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setWeingueter(data);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
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
            .then(data => {
                setWeingueter([...wein, data]);
                handleDialogClose();
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    };

    const startToolbarTemplate = () => {
        return (
            <Button label="Add Wein" icon="pi pi-plus" onClick={handleDialogOpen} />
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

            <Dialog header="Add New Wein" visible={dialogVisible} style={{ width: '50vw' }} footer={<Button label="Close" icon="pi pi-times" onClick={handleDialogClose} />} onHide={handleDialogClose}>
                <form onSubmit={handleSubmit}>
                    <div className="p-field">
                        <label htmlFor="name">Name</label>
                        <input id="name" name="name" value={newWein.name} onChange={handleInputChange} />
                    </div>
                    <div className="p-field">
                        <label htmlFor="beschr">Beschreibung</label>
                        <input id="beschr" name="beschr" value={newWein.beschr} onChange={handleInputChange} />
                    </div>
                    <div className="p-field">
                        <label htmlFor="preis">Preis</label>
                        <input id="preis" name="preis" value={newWein.preis} onChange={handleInputChange} />
                    </div>
                    <div className="p-field">
                        <label htmlFor="weingut_id">Weingut ID</label>
                        <input id="weingut_id" name="weingut_id" value={newWein.weingut_id} onChange={handleInputChange} />
                    </div>
                    <div className="p-field">
                        <label htmlFor="typ_id">Typ ID</label>
                        <input id="typ_id" name="typ_id" value={newWein.typ_id} onChange={handleInputChange} />
                    </div>
                    <div className="p-field">
                        <label htmlFor="art_id">Art ID</label>
                        <input id="art_id" name="art_id" value={newWein.art_id} onChange={handleInputChange} />
                    </div>
                    <Button type="submit" label="Submit" />
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

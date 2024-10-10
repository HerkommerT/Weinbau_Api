import React, { useState } from 'react';
import { Button } from 'primereact/button';
import { Dialog } from 'primereact/dialog';

const initialWeinState = {
    name: '',
    beschr: '',
    preis: '',
    weingut_id: '',
    typ_id: '',
    art_id: ''
};

const WeinForm = ({ visible, onClose, fetchWeinList }) => {
    const [newWein, setNewWein] = useState(initialWeinState);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setNewWein({ ...newWein, [name]: value });
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
            fetchWeinList();
            onClose();
        })
        .catch(error => console.error('Error:', error));
    };

    return (
        <Dialog 
            header="Add New Wein" 
            visible={visible} 
            style={{ width: '50vw' }} 
            footer={
                <div>
                    <Button type="submit" form="weinForm" label="Submit" className="p-button-success" />
                    <Button label="Close" icon="pi pi-times" onClick={onClose} className="p-button-secondary" />
                </div>
            }
            onHide={onClose}
        >
            <form id="weinForm" onSubmit={handleSubmit}>
                <div className="p-fluid">
                    <div className="p-field">
                        <label htmlFor="name">Name</label>
                        <input id="name" name="name" value={newWein.name} onChange={handleInputChange} className="p-inputtext p-component" />
                    </div>
                    <div className="p-field">
                        <label htmlFor="beschr">Beschreibung</label>
                        <input id="beschr" name="beschr" value={newWein.beschr} onChange={handleInputChange} className="p-inputtext p-component" />
                    </div>
                    <div className="p-field">
                        <label htmlFor="preis">Preis</label>
                        <input id="preis" name="preis" value={newWein.preis} onChange={handleInputChange} className="p-inputtext p-component" />
                    </div>
                    <div className="p-field">
                        <label htmlFor="weingut_id">Weingut ID</label>
                        <input id="weingut_id" name="weingut_id" value={newWein.weingut_id} onChange={handleInputChange} className="p-inputtext p-component" />
                    </div>
                    <div className="p-field">
                        <label htmlFor="typ_id">Typ ID</label>
                        <input id="typ_id" name="typ_id" value={newWein.typ_id} onChange={handleInputChange} className="p-inputtext p-component" />
                    </div>
                    <div className="p-field">
                        <label htmlFor="art_id">Art ID</label>
                        <input id="art_id" name="art_id" value={newWein.art_id} onChange={handleInputChange} className="p-inputtext p-component" />
                    </div>
                </div>
            </form>
        </Dialog>
    );
};

export default WeinForm;

import React, { useState } from 'react';
import { Button } from 'primereact/button';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { Toolbar } from 'primereact/toolbar';
import { Link } from 'react-router-dom';
import { useWeinData } from '../hooks/useWeinData'; 
import WeinForm from './WeinForm';  

const Wein = () => {
    const { wein, fetchWeinList } = useWeinData();
    const [dialogVisible, setDialogVisible] = useState(false);

    const handleDialogOpen = () => {
        setDialogVisible(true);
    };

    const handleDialogClose = () => {
        setDialogVisible(false);
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

            <WeinForm 
                visible={dialogVisible} 
                onClose={handleDialogClose} 
                fetchWeinList={fetchWeinList} 
            />

            <Link to="/">
                <Button label="Go to Home" />
            </Link>
        </div>
    );
};

export default Wein;

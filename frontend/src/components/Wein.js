import React, { useState } from 'react';
import { Button } from 'primereact/button';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { Toolbar } from 'primereact/toolbar';
import { Link } from 'react-router-dom';
import { useWeinData } from '../hooks/useWeinData'; 
import { Card } from 'primereact/card';
import WeinForm from './WeinForm';  
import DropdownMenu from './Dropdownmenu';

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
            <DropdownMenu />
            <Card title="Wein Table"></Card>
            <Toolbar start={startToolbarTemplate} />

            <DataTable value={wein}>
                <Column field="wein_id" header="Wein ID" />
                <Column field="jahrgang" header="Jahrgang" />
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
        </div>
    );
};

export default Wein;

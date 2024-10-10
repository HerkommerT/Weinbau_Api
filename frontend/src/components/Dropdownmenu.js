import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Menubar } from 'primereact/menubar';

const DropdownMenu = () => {
    const navigate = useNavigate();

    const dataItems = [
        {
            label: 'Home',
            icon: 'pi pi-home',
            command: () => navigate('/')
        },
        {
            label: 'Tables',
            icon: 'pi pi-table',
            items: [
                {
                    label: 'Wein Table',
                    icon: 'pi pi-fw pi-list',
                    command: () => navigate('/wein')
                },
                {
                    label: 'Finanzen Table',
                    icon: 'pi pi-fw pi-dollar',
                    command: () => navigate('/finanzen')
                }
            ]
        }
    ];

    return <Menubar model={dataItems} />;
};

export default DropdownMenu;
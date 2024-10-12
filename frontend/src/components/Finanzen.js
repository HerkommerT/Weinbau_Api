import React from 'react';
import { InputText } from 'primereact/inputtext';
import { Button } from 'primereact/button';
import { Card } from 'primereact/card';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { Message } from 'primereact/message';
import 'primereact/resources/themes/saga-blue/theme.css';
import 'primereact/resources/primereact.min.css';
import 'primeicons/primeicons.css';
import DropdownMenu from './Dropdownmenu';
import { useFin } from '../hooks/useFin';

const Fin = () => {
  const {
    password,
    setPassword,
    authenticated,
    error,
    fins,
    handleAuthentication,
  } = useFin();

  return (
    <div className="p-d-flex p-jc-center p-ai-center" style={{ height: '100vh' }}>
      <DropdownMenu />
      <Card title="Finanzen" style={{ width: '50rem' }}>
        {!authenticated ? (
          <form onSubmit={handleAuthentication} className="p-d-flex p-flex-column">
            <div className="p-field">
              <label htmlFor="password" className="p-d-block">Password</label>
              <InputText
                id="password"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="p-d-block"
                style={{ marginLeft: '10px' }}
              />
            </div>
            <Button type="submit" label="Authenticate" className="p-mt-2" />
          </form>
        ) : (
          <div>
            <DataTable value={fins} scrollable>
              <Column field="id" header="ID" />
              <Column field="wein_id" header="Wein ID" />
              <Column field="typ_id" header="Typ ID" />
              <Column field="art_id" header="Art ID" />
              <Column field="stückzahl" header="Stückzahl" />
              <Column field="preis" header="Preis" />
              <Column field="absatz" header="Absatz" />
            </DataTable>
          </div>
        )}
        {error && <Message severity="error" text={error} className="p-mt-2" />}
      </Card>
    </div>
  );
};

export default Fin;

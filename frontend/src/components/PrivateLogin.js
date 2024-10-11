import React, { useState } from 'react';
import { InputText } from 'primereact/inputtext';
import { Button } from 'primereact/button';
import { Card } from 'primereact/card';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { Message } from 'primereact/message';
import 'primereact/resources/themes/saga-blue/theme.css';
import 'primereact/resources/primereact.min.css';
import 'primeicons/primeicons.css';

const App = () => {
  const [password, setPassword] = useState('');
  const [authenticated, setAuthenticated] = useState(false);
  const [fins, setFins] = useState([]);
  const [error, setError] = useState('');

  const handleAuthentication = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/auth', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ password }),
        credentials: 'include',
      });
      if (response.ok) {
        setAuthenticated(true);
        setError('');
        fetchFins();
      } else {
        throw new Error('Authentication failed');
      }
    } catch (error) {
      setError('Authentication failed. Please try again.');
    }
  };

  const fetchFins = async () => {
    try {
      const response = await fetch('http://localhost:5000/private/fins', {
        credentials: 'include',
      });
      if (response.ok) {
        const data = await response.json();
        setFins(data);
      } else {
        throw new Error('Failed to fetch fins');
      }
    } catch (error) {
      setError('Failed to fetch fins. Please try again.');
    }
  };

  return (
    <div className="p-d-flex p-jc-center p-ai-center" style={{ height: '100vh' }}>
      <Card title="Fin Management System" style={{ width: '50rem' }}>
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
              />
            </div>
            <Button type="submit" label="Authenticate" className="p-mt-2" />
          </form>
        ) : (
          <div>
            <h2>Fins</h2>
            <DataTable value={fins} responsiveLayout="scroll">
              <Column field="wein_id" header="Wein ID" />
              <Column field="typ_id" header="Typ ID" />
              <Column field="art_id" header="Art ID" />
              <Column field="stückzahl" header="Stückzahl" />
            </DataTable>
          </div>
        )}
        {error && <Message severity="error" text={error} className="p-mt-2" />}
      </Card>
    </div>
  );
};

export default App;
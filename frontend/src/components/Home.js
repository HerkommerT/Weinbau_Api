import React from 'react';
import { Link } from 'react-router-dom';
import { Button } from 'primereact/button';

const Home = () => (
    <div>
        <h1>Home Page</h1>
        <Link to="/menu">
            <Button label="Go to Menu" />
        </Link>
    </div>
);

export default Home;

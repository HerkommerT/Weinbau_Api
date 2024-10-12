import { useState } from 'react';

export const useFin = () => {
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

  return {
    password,
    setPassword,
    authenticated,
    error,
    fins,
    handleAuthentication,
  };
};

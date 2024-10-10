import { useState, useEffect } from 'react';

export const useWeinData = () => {
    const [wein, setWeingueter] = useState([]);

    const fetchWeinList = () => {
        fetch('http://127.0.0.1:5000/wein')
            .then(response => response.json())
            .then(data => setWeingueter(data))
            .catch(error => console.error('Error fetching wine list:', error));
    };

    useEffect(() => {
        fetchWeinList();
    }, []);

    return { wein, fetchWeinList };
};

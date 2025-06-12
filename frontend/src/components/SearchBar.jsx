import React, { useState } from 'react';
import './SearchBar.css'; 

const SearchBar = ({ onSearch }) => {
    const [query, setQuery] = useState('');
    
    const handleChange = (event) => {
        setQuery(event.target.value);
    };
    
    const handleSubmit = (event) => {
        event.preventDefault();
        const trimmed = query.trim().toUpperCase();
        if (trimmed){
            onSearch(trimmed);
        }
    };
    
    return (
        <form onSubmit={handleSubmit} className="search-bar">
        <input
            type="text"
            value={query}
            onChange={handleChange}
            placeholder="Enter stock ticker (e.g., AAPL)"
            className="search-input"
        />
        <button type="submit" className="search-button">Search</button>
        </form>
    );
    }
export default SearchBar;
import React from 'react';
import './LoadingSpinner.css';

const LoadingSpinner = () => {
  return (
    <div className="spinner-container">
      <div className="spinner" />
      <p>Fetching data...</p>
    </div>
  );
};

export default LoadingSpinner;

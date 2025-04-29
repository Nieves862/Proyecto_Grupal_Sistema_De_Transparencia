import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './app'; // Importa el componente App

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Opcional: Si quieres medir el rendimiento de tu app
// import reportWebVitals from './reportWebVitals';
// reportWebVitals();
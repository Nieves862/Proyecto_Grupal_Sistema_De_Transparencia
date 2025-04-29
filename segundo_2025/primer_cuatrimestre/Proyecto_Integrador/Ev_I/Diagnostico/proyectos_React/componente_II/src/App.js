import React from 'react';
import Saludo from './Saludo'; 
import Presentacion from './Presentacion'; 


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Saludo nombre="Martín" />
        <Presentacion nombre="Valeria Nieves" edad="45" profesion="Tec. en Ciencia de Datos e IA" />
      </header>
    </div>
  );
}

export default App;
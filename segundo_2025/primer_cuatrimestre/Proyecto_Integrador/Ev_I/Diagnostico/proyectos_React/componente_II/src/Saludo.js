import React from 'react';

function Saludo(props) {
  return (
    <div>
      <p>Hola {props.nombre}</p>
    </div>
  );
}

export default Saludo;
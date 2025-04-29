import React from 'react';

function saludo(props) {
  return (
    <div>
      <p>Hola {props.nombre}</p>
    </div>
  );
}

export default saludo;
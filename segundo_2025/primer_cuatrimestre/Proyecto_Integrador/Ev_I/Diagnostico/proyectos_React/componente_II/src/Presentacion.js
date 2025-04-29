import React from 'react';

function Presentacion(props) {
  return (
    <div>
      <p>Me llamo {props.nombre}, tengo {props.edad} años y soy {props.profesion}.</p>
    </div>
  );
}

export default Presentacion;
import React from 'react';
import ProductCard from './ProductCard';

const ProductList = ({ products, loading }) => {
  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-center">
          <p className="text-black mb-2">Cargando productos...</p>
          <div className="inline-block h-8 w-8 border-4 border-blue-500 border-t-transparent rounded-full animate-spin"></div>
        </div>
      </div>
    );
  }

  if (!products || products.length === 0) {
    return (
      <div className="text-center py-12">
        <div className="inline-block bg-gray-100 p-4 rounded-lg">
          <p className="text-black font-medium">No se encontraron productos</p>
          <p className="text-sm text-gray-600 mt-1">Prueba ajustando los filtros</p>
        </div>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 transition-opacity duration-300">
      {products.map(product => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
};

export default ProductList;
import React from 'react';

const ProductCard = ({ product }) => {
  return (
    <div className="border border-gray-200 rounded-lg overflow-hidden shadow-md hover:shadow-lg transition-all duration-300 bg-white">
      <div className="h-48 bg-gray-100 flex items-center justify-center">
        <img
          src={product.thumbnail}
          alt={product.title}
          className="object-cover h-full w-full"
        />
      </div>
      <div className="p-4">
        <h3 className="text-lg font-bold text-gray-800 truncate">{product.title}</h3>
        <p className="text-green-600 font-semibold mt-2">${product.price}</p>
        <p className="text-gray-500 text-sm mt-1 line-clamp-2">{product.description}</p>
        <div className="mt-3 flex justify-between items-center">
          <span className="text-xs bg-blue-100 text-blue-800 px-2 py-1 rounded">{product.category}</span>
          <span className="text-xs text-yellow-600">⭐ {product.rating}</span>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;